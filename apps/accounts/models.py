from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.departments.models import Department

class StaffProfile(models.Model):
    """
    Profile extension for institutional librarians and editors.
    """
    ROLE_CHOICES = [
        ('ADMIN', 'Super Administrator'),
        ('LIBRARIAN', 'Librarian (Full Catalog & Resource Access)'),
        ('EDITOR', 'Content Editor (Notices, Events, Materials)'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='LIBRARIAN')
    designation = models.CharField(max_length=150, default="Librarian")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    is_active_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Staff Profile"
        verbose_name_plural = "Staff Profiles"

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} ({self.get_role_display()})"

    @property
    def is_librarian(self):
        return self.role in ['ADMIN', 'LIBRARIAN'] or self.user.is_superuser


@receiver(post_save, sender=User)
def create_or_update_staff_profile(sender, instance, created, **kwargs):
    if created:
        role = 'ADMIN' if instance.is_superuser else 'LIBRARIAN'
        StaffProfile.objects.create(user=instance, role=role)
    else:
        if hasattr(instance, 'staff_profile'):
            instance.staff_profile.save()
        else:
            role = 'ADMIN' if instance.is_superuser else 'LIBRARIAN'
            StaffProfile.objects.create(user=instance, role=role)

