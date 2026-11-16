from django import forms
from apps.catalog.models import Book, BookCopy, Category
from apps.resources.models import DigitalResource
from apps.notices.models import Notice
from apps.core.models import SiteSettings, MenuItem

class DashboardBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'subtitle', 'author', 'co_authors', 'isbn',
            'publisher', 'edition', 'publication_year', 'language',
            'category', 'department', 'subject', 'classification_number',
            'pages', 'description', 'cover_image', 'tags',
            'is_featured', 'is_new_arrival', 'is_donated', 'donor_name'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'co_authors': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control'}),
            'edition': forms.TextInput(attrs={'class': 'form-control'}),
            'publication_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'language': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'classification_number': forms.TextInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'donor_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DashboardBookCopyForm(forms.ModelForm):
    class Meta:
        model = BookCopy
        fields = ['accession_number', 'barcode', 'shelf_location', 'acquisition_date', 'status', 'price', 'remarks']
        widgets = {
            'accession_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. MMIT-B-00501'}),
            'barcode': forms.TextInput(attrs={'class': 'form-control'}),
            'shelf_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Rack 2 - Shelf C'}),
            'acquisition_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'remarks': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DashboardResourceForm(forms.ModelForm):
    class Meta:
        model = DigitalResource
        fields = [
            'title', 'category', 'department', 'subject', 'semester',
            'academic_year', 'description', 'file', 'external_url',
            'author_or_faculty', 'access_type', 'file_format',
            'is_published', 'is_featured'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'semester': forms.Select(choices=[('', '-- Select Semester --')] + [(i, f"Semester {i}") for i in range(1, 7)], attrs={'class': 'form-select'}),
            'academic_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 2024-25'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'external_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'author_or_faculty': forms.TextInput(attrs={'class': 'form-control'}),
            'access_type': forms.Select(attrs={'class': 'form-select'}),
            'file_format': forms.Select(attrs={'class': 'form-select'}),
        }


class DashboardNoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = [
            'title', 'category', 'priority', 'short_summary',
            'content', 'attachment', 'is_pinned', 'is_active',
            'publish_date', 'expiry_date'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'short_summary': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'attachment': forms.FileInput(attrs={'class': 'form-control'}),
            'publish_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class DashboardSiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = [
            'college_name', 'library_name', 'short_name', 'affiliation_info',
            'tagline', 'campus_location', 'district', 'state', 'postal_code',
            'contact_phone', 'library_email', 'principal_email', 'college_website_url',
            'opening_hours_weekday', 'opening_hours_weekend', 'reading_hall_hours',
            'hero_title', 'hero_subtitle', 'footer_about',
            'egranthalaya_url', 'ndli_portal_url', 'ndli_club_reg_url', 'ekumbh_url', 'swayam_url'
        ]
        widgets = {
            'college_name': forms.TextInput(attrs={'class': 'form-control'}),
            'library_name': forms.TextInput(attrs={'class': 'form-control'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control'}),
            'affiliation_info': forms.TextInput(attrs={'class': 'form-control'}),
            'tagline': forms.TextInput(attrs={'class': 'form-control'}),
            'campus_location': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'library_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'principal_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'college_website_url': forms.URLInput(attrs={'class': 'form-control'}),
            'opening_hours_weekday': forms.TextInput(attrs={'class': 'form-control'}),
            'opening_hours_weekend': forms.TextInput(attrs={'class': 'form-control'}),
            'reading_hall_hours': forms.TextInput(attrs={'class': 'form-control'}),
            'hero_title': forms.TextInput(attrs={'class': 'form-control'}),
            'hero_subtitle': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'footer_about': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'egranthalaya_url': forms.URLInput(attrs={'class': 'form-control'}),
            'ndli_portal_url': forms.URLInput(attrs={'class': 'form-control'}),
            'ndli_club_reg_url': forms.URLInput(attrs={'class': 'form-control'}),
            'ekumbh_url': forms.URLInput(attrs={'class': 'form-control'}),
            'swayam_url': forms.URLInput(attrs={'class': 'form-control'}),
        }


class CsvImportForm(forms.Form):
    csv_file = forms.FileField(
        label="Select CSV File",
        help_text="CSV must contain headers: Title, Author, ISBN, Publisher, Year, Department, Category, AccessionNumber, ShelfLocation",
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.csv'})
    )

