from django.db import models

class Feedback(models.Model):
    """
    Public student and faculty suggestions, reviews, and library feedback.
    """
    USER_TYPE_CHOICES = [
        ('STUDENT', 'Diploma Student'),
        ('FACULTY', 'Faculty Member'),
        ('STAFF', 'Staff Member'),
        ('VISITOR', 'Visitor / Other'),
    ]

    CATEGORY_CHOICES = [
        ('GENERAL', 'General Feedback'),
        ('COLLECTION', 'Book Collection & Availability'),
        ('READING_HALL', 'Reading Hall & Infrastructure'),
        ('DIGITAL_RESOURCES', 'Digital Library & E-Resources'),
        ('SERVICES', 'Circulation & Staff Assistance'),
        ('PORTAL_IMPROVEMENT', 'Website & Portal Suggestion'),
    ]

    RATING_CHOICES = [
        (5, '★★★★★ - Excellent'),
        (4, '★★★★☆ - Very Good'),
        (3, '★★★☆☆ - Good / Satisfactory'),
        (2, '★★☆☆☆ - Needs Improvement'),
        (1, '★☆☆☆☆ - Poor'),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField()
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='STUDENT')
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='GENERAL')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=5)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    
    is_reviewed = models.BooleanField(default=False)
    admin_response = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Feedback Submission"
        verbose_name_plural = "Feedback Submissions"

    def __str__(self):
        return f"{self.name} [{self.get_category_display()}] - {self.rating}★"

