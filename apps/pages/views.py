from django.shortcuts import render
from .models import LibraryStaff, LibraryCommitteeMember, Facility, FAQ
from apps.core.models import SiteSettings

def about_library(request):
    """
    Overview, history, infrastructure, and operating hours of MMIT Central Library.
    Replaces /p/about-library.html from Blogger.
    """
    settings_obj = SiteSettings.load()
    facilities = Facility.objects.filter(is_active=True).order_by('display_order')[:4]
    librarian = LibraryStaff.objects.filter(role_type='LIBRARIAN', is_active=True).first()

    return render(request, 'pages/about.html', {
        'settings': settings_obj,
        'facilities': facilities,
        'librarian': librarian,
    })


def vision_mission(request):
    """
    Vision, Mission, and Core Objectives of the Institutional Library.
    """
    settings_obj = SiteSettings.load()
    return render(request, 'pages/vision_mission.html', {'settings': settings_obj})


def rules_regulations(request):
    """
    Library Rules and Regulations, including general discipline, borrowing limits,
    loss/damage terms, and clearance procedure.
    Replaces /p/rules-regulations.html from Blogger.
    """
    settings_obj = SiteSettings.load()
    return render(request, 'pages/rules.html', {'settings': settings_obj})


def library_staff_list(request):
    """
    Directory of library officers, staff members, and Advisory Committee members.
    """
    staff_members = LibraryStaff.objects.filter(is_active=True).order_by('display_order')
    committee = LibraryCommitteeMember.objects.all().order_by('display_order')

    return render(request, 'pages/staff.html', {
        'staff_members': staff_members,
        'committee': committee,
    })


def facilities_list(request):
    """
    Comprehensive presentation of library facilities: Reading Hall, Stack Area,
    Digital Lab, Reference Section, Book Bank, and Periodicals.
    """
    facilities = Facility.objects.filter(is_active=True).order_by('display_order')
    return render(request, 'pages/facilities.html', {'facilities': facilities})


def faq_list(request):
    """
    Frequently Asked Questions for students, freshers, and faculty.
    """
    category = request.GET.get('category', '').strip()
    faqs = FAQ.objects.filter(is_active=True)
    if category:
        faqs = faqs.filter(category=category)

    return render(request, 'pages/faq.html', {
        'faqs': faqs,
        'selected_category': category,
        'categories': FAQ.CATEGORY_CHOICES,
    })

