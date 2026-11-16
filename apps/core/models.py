from django.db import models
from django.urls import reverse

class SiteSettings(models.Model):
    """
    Singleton model for College Institutional and Library branding and contact info.
    """
    college_name = models.CharField(
        max_length=255,
        default="Government Polytechnic Madhogarh"
    )
    library_name = models.CharField(
        max_length=255,
        default="Central Library"
    )
    short_name = models.CharField(
        max_length=50,
        default="GP Madhogarh Library"
    )
    institution_code = models.CharField(
        max_length=20,
        default="3318",
        help_text="BTEUP / URISE Institution Code"
    )
    affiliation_info = models.CharField(
        max_length=255,
        default="Approved by AICTE New Delhi & Affiliated to Board of Technical Education Uttar Pradesh (BTEUP)"
    )
    tagline = models.CharField(
        max_length=255,
        default="Central Library & Digital Resource Portal"
    )
    
    # Address details
    campus_location = models.CharField(max_length=255, default="Kailor, Madhogarh")
    district = models.CharField(max_length=100, default="Jalaun")
    state = models.CharField(max_length=100, default="Uttar Pradesh")
    postal_code = models.CharField(max_length=20, default="285126")
    
    # Contact & Helpline
    contact_phone = models.CharField(max_length=50, default="9305574396")
    library_email = models.EmailField(default="govt.polytechnic.madhogarh@gmail.com")
    principal_email = models.EmailField(default="govt.polytechnic.madhogarh@gmail.com")
    college_website_url = models.URLField(default="https://gpmadhogarh.ac.in/")
    erp_url = models.URLField(
        default="https://erp.bizby.io/",
        help_text="College Library ERP Portal"
    )
    
    # Operating Timings
    opening_hours_weekday = models.CharField(
        max_length=100,
        default="Monday to Saturday: 10:00 AM – 05:00 PM"
    )
    opening_hours_weekend = models.CharField(
        max_length=100,
        default="Sunday & Gazetted Holidays: Closed"
    )
    reading_hall_hours = models.CharField(
        max_length=100,
        default="09:30 AM – 05:30 PM (Self-study area)"
    )
    
    # Visual assets
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    favicon = models.ImageField(upload_to='site/', blank=True, null=True)
    hero_image = models.ImageField(upload_to='site/', blank=True, null=True)
    
    # Hero text
    hero_title = models.CharField(
        max_length=255,
        default="Welcome to Government Polytechnic Madhogarh Library"
    )
    hero_subtitle = models.TextField(
        default="Central Library & Digital Resource Portal empowering diploma engineers and technical scholars with academic collections, BTEUP question banks, syllabus, and digital e-resources."
    )
    
    # About footer text
    footer_about = models.TextField(
        default="The Central Library of Government Polytechnic Madhogarh, Jalaun (Uttar Pradesh) caters to the technical learning, research, and curriculum needs of diploma students and faculty."
    )
    
    # External system integration links verified from reference
    egranthalaya_url = models.URLField(
        default="http://eg4.nic.in/",
        help_text="National Informatics Centre e-Granthalaya Cloud Portal"
    )
    ndli_portal_url = models.URLField(
        default="https://ndl.iitkgp.ac.in/",
        help_text="National Digital Library of India"
    )
    ndli_club_reg_url = models.URLField(
        default="https://club.ndl.iitkgp.ac.in/sign-up",
        help_text="NDLI Club Join Link"
    )
    ekumbh_url = models.URLField(
        default="https://ekumbh.aicte-india.org/",
        help_text="AICTE e-KUMBH Indian Language Technical Books"
    )
    swayam_url = models.URLField(
        default="https://swayam.gov.in/",
        help_text="SWAYAM & NPTEL MOOC Platform"
    )
    
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return f"{self.short_name} Configuration"

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class MenuItem(models.Model):
    """
    Configurable multi-level institutional navigation menu item.
    """
    title = models.CharField(max_length=100)
    url = models.CharField(
        max_length=255,
        help_text="Can be an absolute path (e.g. /about/), named route (e.g. catalog:search), or external URL"
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True
    )
    order = models.PositiveIntegerField(default=0)
    icon = models.CharField(max_length=50, blank=True, help_text="Bootstrap icon class, e.g. bi-book")
    is_active = models.BooleanField(default=True)
    open_in_new_tab = models.BooleanField(default=False)
    staff_only = models.BooleanField(default=False)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"

    def __str__(self):
        if self.parent:
            return f"{self.parent.title} -> {self.title}"
        return self.title

    def get_resolved_url(self):
        if self.url.startswith(('http://', 'https://', '/')):
            return self.url
        try:
            return reverse(self.url)
        except Exception:
            return f"/{self.url.lstrip('/')}"


class HeroSlide(models.Model):
    """
    Hero slideshow / carousel slides displayed between the navigation bar
    and the announcement ticker on the library portal.
    """
    title = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True, help_text="Brief description or highlight for this slide")
    badge_text = models.CharField(
        max_length=100,
        blank=True,
        default="Campus Overview",
        help_text="Tag pill displayed above title, e.g. 'Campus Overview', 'Digital Library'"
    )
    image = models.ImageField(upload_to='hero_slides/')
    order = models.PositiveIntegerField(default=0, help_text="Display order (lowest number first)")
    is_active = models.BooleanField(default=True, help_text="Toggle visibility on website")
    link_url = models.CharField(max_length=255, blank=True, help_text="Optional destination link, e.g. '/catalog/' or 'https://...'")
    link_text = models.CharField(max_length=60, blank=True, default="Explore More", help_text="Call to action button label")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Hero Slide"
        verbose_name_plural = "Hero Slides"

    def __str__(self):
        return self.title


