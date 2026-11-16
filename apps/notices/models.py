from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone

class Notice(models.Model):
    """
    Official institutional library notices, circulars, and announcements.
    """
    CATEGORY_CHOICES = [
        ('CIRCULAR', 'Official Circular / Order'),
        ('ACADEMIC', 'Academic & Curriculum'),
        ('ORIENTATION', 'Orientation & Freshers'),
        ('MEMBERSHIP', 'Library Membership & Cards'),
        ('BOOK_BANK', 'Book Bank Distribution'),
        ('EXAMINATION', 'Exam Prep & Question Bank'),
        ('DONATION', 'Book Donations & Acknowledgements'),
        ('GENERAL', 'General Notice'),
    ]

    PRIORITY_CHOICES = [
        ('LOW', 'Low Priority'),
        ('NORMAL', 'Standard Notice'),
        ('HIGH', 'Important / High Priority'),
        ('URGENT', 'Urgent / Alert'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280, unique=True, blank=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='CIRCULAR')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='NORMAL')
    short_summary = models.CharField(max_length=300, blank=True, help_text="Brief 1-2 line summary for homepage previews")
    content = models.TextField(help_text="Full text content of the notice")
    attachment = models.FileField(upload_to='notices/', blank=True, null=True, help_text="Optional signed PDF notice circular")
    
    is_pinned = models.BooleanField(default=False, help_text="Pin to top notice ticker and homepage banners")
    is_active = models.BooleanField(default=True)
    
    publish_date = models.DateField(default=timezone.now)
    expiry_date = models.DateField(null=True, blank=True, help_text="Leave blank if permanent")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_pinned', '-publish_date', '-id']
        verbose_name = "Notice & Circular"
        verbose_name_plural = "Notices & Circulars"

    def __str__(self):
        return f"[{self.priority}] {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:250]
            candidate = base
            counter = 1
            while Notice.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                candidate = f"{base}-{counter}"
                counter += 1
            self.slug = candidate
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('notices:notice_detail', kwargs={'slug': self.slug})

    @property
    def is_expired(self):
        if self.expiry_date:
            return self.expiry_date < timezone.now().date()
        return False

