from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class LibraryEvent(models.Model):
    """
    Events, Orientations, Workshops, and Exhibitions.
    """
    EVENT_TYPE_CHOICES = [
        ('ORIENTATION', 'Orientation Programme'),
        ('WORKSHOP', 'Workshop & Digital Training'),
        ('BOOK_FAIR', 'Book Fair & Exhibition'),
        ('DONATION', 'Book Donation Drive'),
        ('SEMINAR', 'Academic Seminar'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280, unique=True, blank=True)
    event_type = models.CharField(max_length=30, choices=EVENT_TYPE_CHOICES, default='ORIENTATION')
    venue = models.CharField(max_length=200, default="Seminar Hall, MMIT Campus")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    summary = models.CharField(max_length=300, help_text="Short teaser for homepage")
    description = models.TextField()
    featured_image = models.ImageField(upload_to='events/', blank=True, null=True)
    
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date', '-id']
        verbose_name = "Library Event"
        verbose_name_plural = "Library Events"

    def __str__(self):
        return f"{self.title} ({self.start_date})"

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:250]
            candidate = base
            counter = 1
            while LibraryEvent.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                candidate = f"{base}-{counter}"
                counter += 1
            self.slug = candidate
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('events:event_detail', kwargs={'slug': self.slug})


class GalleryImage(models.Model):
    """
    Institutional Library Photo Gallery images.
    """
    event = models.ForeignKey(LibraryEvent, on_delete=models.SET_NULL, null=True, blank=True, related_name='gallery_photos')
    title = models.CharField(max_length=150)
    caption = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='gallery/')
    is_featured_home = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-id']
        verbose_name = "Gallery Photo"
        verbose_name_plural = "Gallery Photos"

    def __str__(self):
        return self.title

