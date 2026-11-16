from django.db import models

class LibraryStaff(models.Model):
    """
    Library personnel and staff directory.
    """
    ROLE_CHOICES = [
        ('LIBRARIAN', 'Librarian & Officer In-Charge'),
        ('ASSISTANT', 'Assistant Librarian'),
        ('ATTENDANT', 'Library Attendant / Assistant'),
        ('ADVISOR', 'Library Advisory Member'),
    ]

    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    qualification = models.CharField(max_length=150, blank=True)
    role_type = models.CharField(max_length=20, choices=ROLE_CHOICES, default='LIBRARIAN')
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(upload_to='staff/', blank=True, null=True)
    bio = models.TextField(blank=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'name']
        verbose_name = "Library Staff Member"
        verbose_name_plural = "Library Staff Members"

    def __str__(self):
        return f"{self.name} - {self.designation}"


class LibraryCommitteeMember(models.Model):
    """
    College Library Advisory Committee members.
    """
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    committee_role = models.CharField(
        max_length=100,
        default="Committee Member",
        help_text="e.g. Chairman (Principal), Member Secretary (Librarian), Faculty Representative"
    )
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'id']
        verbose_name = "Committee Member"
        verbose_name_plural = "Committee Members"

    def __str__(self):
        return f"{self.name} ({self.committee_role})"


class Facility(models.Model):
    """
    Library facilities (Reading Hall, Digital Lab, Reference Section, Book Bank, Periodicals).
    """
    title = models.CharField(max_length=150)
    icon = models.CharField(max_length=50, default='bi-door-open', help_text="Bootstrap icon class")
    image = models.ImageField(upload_to='facilities/', blank=True, null=True)
    description = models.TextField()
    features = models.TextField(blank=True, help_text="One feature per line")
    capacity = models.CharField(max_length=100, blank=True, help_text="e.g. 100 Seater, 20 Computers")
    timings = models.CharField(max_length=100, blank=True, default="10:00 AM – 05:00 PM")
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'title']
        verbose_name = "Library Facility"
        verbose_name_plural = "Library Facilities"

    def __str__(self):
        return self.title

    def get_features_list(self):
        if not self.features:
            return []
        return [f.strip() for f in self.features.split('\n') if f.strip()]


class FAQ(models.Model):
    """
    Frequently asked questions about membership, borrowing, digital access, and exams.
    """
    CATEGORY_CHOICES = [
        ('GENERAL', 'General & Timings'),
        ('MEMBERSHIP', 'Library Cards & Membership'),
        ('CIRCULATION', 'Borrowing, Renewals & Fines'),
        ('DIGITAL', 'E-Library & NDLI Registration'),
        ('NO_DUES', 'Clearance & No-Dues Certificate'),
    ]

    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='GENERAL')
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'id']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question

