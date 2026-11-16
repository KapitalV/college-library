from django.db import models
from django.urls import reverse
from apps.departments.models import Department

class MembershipApplication(models.Model):
    """
    Online Student and Staff Library Membership Card applications.
    """
    STATUS_CHOICES = [
        ('PENDING', 'Pending Verification'),
        ('APPROVED', 'Approved (Ready to Collect)'),
        ('CARD_ISSUED', 'Card Issued'),
        ('REJECTED', 'Rejected'),
    ]

    APPLICANT_TYPE_CHOICES = [
        ('STUDENT', 'Diploma Student'),
        ('FACULTY', 'Faculty Member'),
        ('STAFF', 'Non-Teaching Staff'),
    ]

    full_name = models.CharField(max_length=150)
    applicant_type = models.CharField(max_length=20, choices=APPLICANT_TYPE_CHOICES, default='STUDENT')
    roll_number = models.CharField(max_length=50, help_text="BTEUP Roll Number or Staff ID")
    enrollment_number = models.CharField(max_length=50, blank=True, help_text="BTEUP Enrollment No.")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='membership_applications')
    semester = models.PositiveSmallIntegerField(default=1, help_text="1 to 6 for diploma students")
    
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    id_card_photo = models.ImageField(upload_to='id_proofs/', blank=True, null=True, help_text="College ID or Admission Receipt scan")
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    card_number = models.CharField(max_length=50, blank=True, help_text="Assigned Library Card Number")
    librarian_remarks = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Membership Application"
        verbose_name_plural = "Membership Applications"

    def __str__(self):
        return f"{self.full_name} ({self.roll_number}) - {self.get_status_display()}"


class BookRecommendation(models.Model):
    """
    Faculty and student book purchase recommendations.
    """
    STATUS_CHOICES = [
        ('SUBMITTED', 'Submitted'),
        ('UNDER_REVIEW', 'Under Committee Review'),
        ('APPROVED', 'Approved for Procurement'),
        ('ACQUIRED', 'Acquired in Library'),
        ('REJECTED', 'Not Feasible / Rejected'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=200, blank=True)
    isbn = models.CharField(max_length=50, blank=True)
    edition = models.CharField(max_length=50, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    
    recommender_name = models.CharField(max_length=150)
    recommender_role = models.CharField(
        max_length=20,
        choices=[('STUDENT', 'Student'), ('FACULTY', 'Faculty'), ('STAFF', 'Staff')],
        default='STUDENT'
    )
    recommender_email = models.EmailField()
    reason = models.TextField(help_text="Why should this book be added to the library collection?")
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SUBMITTED')
    librarian_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Book Recommendation"
        verbose_name_plural = "Book Recommendations"

    def __str__(self):
        return f"{self.title} by {self.author} (Req: {self.recommender_name})"


class ResourceRequest(models.Model):
    """
    Request for specific question paper, lecture notes, or syllabus copy not yet available.
    """
    STATUS_CHOICES = [
        ('PENDING', 'Pending Request'),
        ('FULFILLED', 'Uploaded / Fulfilled'),
        ('UNAVAILABLE', 'Unavailable'),
    ]

    requester_name = models.CharField(max_length=150)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    semester = models.PositiveSmallIntegerField(default=1)
    subject_name = models.CharField(max_length=150)
    request_type = models.CharField(
        max_length=30,
        choices=[
            ('QUESTION_PAPER', 'Previous Year Question Paper'),
            ('NOTES', 'Lecture Notes / PPT'),
            ('SYLLABUS', 'Detailed Syllabus'),
            ('EBOOK', 'E-Book / Reference Material'),
        ],
        default='QUESTION_PAPER'
    )
    details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    librarian_reply = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Resource Request"
        verbose_name_plural = "Resource Requests"

    def __str__(self):
        return f"{self.subject_name} ({self.request_type}) by {self.requester_name}"


class DownloadableForm(models.Model):
    """
    Official downloadable PDF forms (No-Dues Form, Book Bank Form, Loss of Book Declaration).
    """
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='library_forms/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Downloadable Form"
        verbose_name_plural = "Downloadable Forms"

    def __str__(self):
        return self.title

