from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from apps.departments.models import Department, Subject

class DigitalResource(models.Model):
    """
    Academic digital materials: Previous Year Papers, Syllabus, Notes, E-Books, and National Portals.
    """
    CATEGORY_CHOICES = [
        ('QUESTION_PAPER', 'Previous Year Question Paper'),
        ('SYLLABUS', 'Curriculum & Syllabus'),
        ('LECTURE_NOTES', 'Faculty Lecture Notes & PPT'),
        ('EBOOK', 'Academic E-Book'),
        ('JOURNAL', 'E-Journal / Periodical'),
        ('PROJECT_REPORT', 'Project Report / Lab Manual'),
        ('PORTAL', 'National Educational Portal'),
        ('OTHER', 'General Educational Resource'),
    ]

    SEMESTER_CHOICES = [
        (1, '1st Semester'),
        (2, '2nd Semester'),
        (3, '3rd Semester'),
        (4, '4th Semester'),
        (5, '5th Semester'),
        (6, '6th Semester'),
    ]

    ACCESS_CHOICES = [
        ('OPEN_ACCESS', 'Open Access (Public)'),
        ('INSTITUTIONAL', 'Institutional / Campus Network'),
        ('NDLI_PASSKEY', 'NDLI Club Passkey Required'),
        ('STUDENT_LOGIN', 'Registered Students Only'),
    ]

    FORMAT_CHOICES = [
        ('PDF', 'PDF Document'),
        ('PPT', 'PowerPoint Presentation (PPT/PPTX)'),
        ('DOC', 'Word Document (DOC/DOCX)'),
        ('ZIP', 'Archive (ZIP/RAR)'),
        ('LINK', 'Web Link / External Portal'),
    ]

    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=280, unique=True, blank=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='QUESTION_PAPER')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='digital_resources')
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True, related_name='digital_resources')
    semester = models.PositiveSmallIntegerField(choices=SEMESTER_CHOICES, null=True, blank=True)
    academic_year = models.CharField(max_length=20, blank=True, help_text="e.g. 2024-25, 2023-24")
    
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='resources/', blank=True, null=True)
    external_url = models.URLField(blank=True, help_text="External URL if hosted on NDLI, NPTEL, BTEUP, Drive etc.")
    
    author_or_faculty = models.CharField(max_length=150, blank=True, help_text="Author, Publisher, or Faculty In-Charge")
    access_type = models.CharField(max_length=20, choices=ACCESS_CHOICES, default='OPEN_ACCESS')
    file_format = models.CharField(max_length=10, choices=FORMAT_CHOICES, default='PDF')
    
    download_count = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', '-id']
        verbose_name = "Digital Resource"
        verbose_name_plural = "Digital Resources"

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:250]
            candidate = base
            counter = 1
            while DigitalResource.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                candidate = f"{base}-{counter}"
                counter += 1
            self.slug = candidate
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('resources:resource_detail', kwargs={'slug': self.slug})

    @property
    def has_file(self):
        return bool(self.file)

    @property
    def destination_url(self):
        if self.file:
            return self.file.url
        return self.external_url or '#'

