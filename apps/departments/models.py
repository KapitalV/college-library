from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Department(models.Model):
    """
    Academic Engineering and Polytechnic Departments.
    """
    name = models.CharField(max_length=150, unique=True)
    code = models.CharField(max_length=20, unique=True, help_text="Short code, e.g. CSE, EE, ECE")
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    branch_code = models.CharField(max_length=20, blank=True, help_text="BTEUP Branch Code, e.g. 355")
    lateral_code = models.CharField(max_length=20, blank=True, help_text="BTEUP Lateral Entry Code, e.g. 389")
    description = models.TextField()
    icon = models.CharField(max_length=50, default='bi-mortarboard', help_text="Bootstrap icon class")
    image = models.ImageField(upload_to='departments/', blank=True, null=True)
    head_of_department = models.CharField(max_length=150, blank=True, help_text="Name of HOD or in-charge")
    intake_capacity = models.PositiveIntegerField(default=60, help_text="Approved student intake per year")
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'name']
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return f"{self.name} ({self.code})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.code or self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('departments:department_detail', kwargs={'slug': self.slug})


class Subject(models.Model):
    """
    Subjects taught under specific departments and semesters according to BTEUP syllabus.
    """
    SEMESTER_CHOICES = [
        (1, '1st Semester'),
        (2, '2nd Semester'),
        (3, '3rd Semester'),
        (4, '4th Semester'),
        (5, '5th Semester'),
        (6, '6th Semester'),
    ]

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, blank=True, help_text="Subject / Paper code, e.g. CS-201")
    semester = models.PositiveSmallIntegerField(choices=SEMESTER_CHOICES, default=1)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['department', 'semester', 'name']
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        unique_together = ('department', 'code', 'semester')

    def __str__(self):
        return f"{self.name} ({self.department.code} Sem {self.semester})"

