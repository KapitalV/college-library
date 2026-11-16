from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import MembershipApplication, BookRecommendation, ResourceRequest, DownloadableForm
from .forms import MembershipApplicationForm, BookRecommendationForm, ResourceRequestForm
from apps.core.models import SiteSettings

def service_list(request):
    """
    Overview of Central Library services, lending policies, and facilities.
    """
    settings_obj = SiteSettings.load()
    forms = DownloadableForm.objects.filter(is_active=True).order_by('order')
    return render(request, 'services/service_list.html', {
        'settings': settings_obj,
        'forms': forms,
    })


def membership_apply(request):
    """
    Student and faculty library membership card application.
    Replaces the external Google Form from the reference Blogger website.
    """
    if request.method == 'POST':
        form = MembershipApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()
            messages.success(
                request,
                f"Application submitted successfully! Your application reference number is #{application.id}. "
                "The library staff will verify your details and issue your card shortly."
            )
            return redirect('services:membership')
        else:
            messages.error(request, "Please correct the errors in the form below.")
    else:
        form = MembershipApplicationForm()

    return render(request, 'services/membership_apply.html', {'form': form})


def book_recommend(request):
    """
    Book recommendation submission for library acquisition.
    """
    if request.method == 'POST':
        form = BookRecommendationForm(request.POST)
        if form.is_valid():
            recommendation = form.save()
            messages.success(
                request,
                f"Thank you, {recommendation.recommender_name}! Your recommendation for '{recommendation.title}' "
                "has been submitted to the Library Advisory Committee for review."
            )
            return redirect('services:book_recommend')
        else:
            messages.error(request, "Please check the form fields and try again.")
    else:
        form = BookRecommendationForm()

    return render(request, 'services/book_recommend.html', {'form': form})


def resource_request(request):
    """
    Request study materials, specific question papers, or syllabus handouts.
    """
    if request.method == 'POST':
        form = ResourceRequestForm(request.POST)
        if form.is_valid():
            req_obj = form.save()
            messages.success(
                request,
                f"Your request for '{req_obj.subject_name}' ({req_obj.get_request_type_display()}) has been received. "
                "The librarian will review and upload the required material."
            )
            return redirect('services:resource_request')
        else:
            messages.error(request, "Please check the highlighted errors.")
    else:
        form = ResourceRequestForm()

    return render(request, 'services/resource_request.html', {'form': form})


def no_dues_info(request):
    """
    Guidelines and step-by-step instructions for obtaining a Library Clearance / No-Dues Certificate.
    """
    return render(request, 'services/no_dues.html')


def ndli_club_info(request):
    """
    National Digital Library of India (NDLI) Club membership instructions, passkey guidance,
    and regional directorate circular guidelines.
    """
    settings_obj = SiteSettings.load()
    return render(request, 'services/ndli_club.html', {'settings': settings_obj})


def downloadable_forms_list(request):
    """
    Official downloadable PDF forms.
    """
    forms = DownloadableForm.objects.filter(is_active=True).order_by('order')
    return render(request, 'services/forms_list.html', {'forms': forms})

