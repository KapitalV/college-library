from django import forms
from .models import MembershipApplication, BookRecommendation, ResourceRequest

class MembershipApplicationForm(forms.ModelForm):
    class Meta:
        model = MembershipApplication
        fields = [
            'full_name', 'applicant_type', 'roll_number', 'enrollment_number',
            'department', 'semester', 'email', 'mobile_number', 'id_card_photo'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name as per College Records'}),
            'applicant_type': forms.Select(attrs={'class': 'form-select'}),
            'roll_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 2101010101 (BTEUP Roll Number / Staff ID)'}),
            'enrollment_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. E210101001 (Optional for freshers)'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'semester': forms.Select(choices=[(i, f"Semester {i}") for i in range(1, 7)], attrs={'class': 'form-select'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10-digit Mobile Number'}),
            'id_card_photo': forms.FileInput(attrs={'class': 'form-control'}),
        }


class BookRecommendationForm(forms.ModelForm):
    class Meta:
        model = BookRecommendation
        fields = [
            'title', 'author', 'publisher', 'isbn', 'edition',
            'department', 'recommender_name', 'recommender_role',
            'recommender_email', 'reason'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author(s) Name'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Publisher (e.g. Khanna, S. Chand, Pearson)'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN (if known)'}),
            'edition': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 4th Edition / Latest'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'recommender_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'recommender_role': forms.Select(attrs={'class': 'form-select'}),
            'recommender_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Explain how this book will benefit the students and syllabus...'}),
        }


class ResourceRequestForm(forms.ModelForm):
    class Meta:
        model = ResourceRequest
        fields = [
            'requester_name', 'email', 'department', 'semester',
            'subject_name', 'request_type', 'details'
        ]
        widgets = {
            'requester_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'semester': forms.Select(choices=[(i, f"Semester {i}") for i in range(1, 7)], attrs={'class': 'form-select'}),
            'subject_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject / Topic Name'}),
            'request_type': forms.Select(attrs={'class': 'form-select'}),
            'details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Specific exam year, topic notes, or question paper details needed...'}),
        }

