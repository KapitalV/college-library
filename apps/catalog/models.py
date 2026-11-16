from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from apps.departments.models import Department, Subject

class Category(models.Model):
    """
    Book Categories (e.g., Core Textbooks, Reference Titles, Book Bank, Handbooks, Donated Books)
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=110, unique=True, blank=True)
    description = models.TextField(blank=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'name']
        verbose_name = "Book Category"
        verbose_name_plural = "Book Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Book(models.Model):
    """
    Bibliographic metadata for a book title in the catalog.
    """
    LANGUAGE_CHOICES = [
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('Bilingual', 'Bilingual (Hindi & English)'),
    ]

    title = models.CharField(max_length=255, db_index=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=280, unique=True, blank=True)
    author = models.CharField(max_length=255, db_index=True)
    co_authors = models.CharField(max_length=255, blank=True)
    isbn = models.CharField(max_length=30, blank=True, db_index=True, help_text="ISBN-10 or ISBN-13")
    publisher = models.CharField(max_length=200, blank=True)
    edition = models.CharField(max_length=50, blank=True, help_text="e.g. 3rd Edition, Revised Edition")
    publication_year = models.PositiveIntegerField(null=True, blank=True)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, default='English')
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='books')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='books')
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True, related_name='books')
    
    classification_number = models.CharField(
        max_length=100,
        blank=True,
        help_text="DDC or Call Number, e.g. 005.133 / TAN"
    )
    pages = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, help_text="Comma-separated keywords")
    
    # Flags
    is_featured = models.BooleanField(default=False)
    is_new_arrival = models.BooleanField(default=False)
    is_donated = models.BooleanField(default=False)
    donor_name = models.CharField(max_length=150, blank=True, help_text="Faculty / Alumnus donor name")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_new_arrival', '-id']
        verbose_name = "Book"
        verbose_name_plural = "Books"
        indexes = [
            models.Index(fields=['title', 'author']),
            models.Index(fields=['isbn']),
        ]

    def __str__(self):
        return f"{self.title} - {self.author}"

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(f"{self.title}-{self.author}")[:250]
            candidate = base
            counter = 1
            while Book.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                candidate = f"{base}-{counter}"
                counter += 1
            self.slug = candidate
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('catalog:book_detail', kwargs={'slug': self.slug})

    @property
    def total_copies(self):
        return self.copies.count()

    @property
    def available_copies(self):
        return self.copies.filter(status='AVAILABLE').count()

    @property
    def is_available(self):
        return self.available_copies > 0


class BookCopy(models.Model):
    """
    Physical inventory copy linked to a Book title with a unique accession number.
    """
    STATUS_CHOICES = [
        ('AVAILABLE', 'Available on Shelf'),
        ('ISSUED', 'Issued to Student/Staff'),
        ('REFERENCE_ONLY', 'Reference Section Only (No Loan)'),
        ('RESERVED', 'Reserved'),
        ('REPAIR', 'In Binding / Maintenance'),
        ('LOST', 'Lost / Written Off'),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='copies')
    accession_number = models.CharField(
        max_length=50,
        unique=True,
        db_index=True,
        help_text="Unique institutional accession identifier, e.g. GPM-B-00412"
    )
    barcode = models.CharField(max_length=100, blank=True)
    shelf_location = models.CharField(
        max_length=100,
        default="Rack 1 - Shelf A",
        help_text="Exact physical stack rack and shelf location"
    )
    acquisition_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='AVAILABLE')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    remarks = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['accession_number']
        verbose_name = "Book Copy (Accession)"
        verbose_name_plural = "Book Copies (Accessions)"

    def __str__(self):
        return f"{self.accession_number} ({self.book.title[:30]}) - {self.get_status_display()}"

