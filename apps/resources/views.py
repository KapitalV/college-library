from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q, F
from django.http import HttpResponseRedirect
from .models import DigitalResource
from apps.departments.models import Department
from apps.core.models import SiteSettings

def resource_list(request):
    """
    Searchable and filterable directory of all published digital academic resources.
    """
    category = request.GET.get('category', '').strip()
    dept_id = request.GET.get('department', '').strip()
    semester = request.GET.get('semester', '').strip()
    query = request.GET.get('q', '').strip()

    resources = DigitalResource.objects.filter(is_published=True).select_related('department', 'subject')

    if category:
        resources = resources.filter(category=category)
    if dept_id:
        resources = resources.filter(department_id=dept_id)
    if semester:
        resources = resources.filter(semester=semester)
    if query:
        resources = resources.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(author_or_faculty__icontains=query)
        )

    paginator = Paginator(resources, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    departments = Department.objects.filter(is_active=True)

    context = {
        'page_obj': page_obj,
        'selected_category': category,
        'selected_dept': dept_id,
        'selected_semester': semester,
        'query': query,
        'departments': departments,
        'categories': DigitalResource.CATEGORY_CHOICES,
        'semesters_range': range(1, 7),
        'total_resources': paginator.count,
    }
    return render(request, 'resources/resource_list.html', context)


def resource_detail(request, slug):
    """
    Detailed page for a single digital document or external educational resource.
    """
    resource = get_object_or_404(
        DigitalResource.objects.select_related('department', 'subject'),
        slug=slug,
        is_published=True
    )
    related_resources = DigitalResource.objects.filter(
        department=resource.department,
        category=resource.category,
        is_published=True
    ).exclude(pk=resource.pk)[:4]

    context = {
        'resource': resource,
        'related_resources': related_resources,
    }
    return render(request, 'resources/resource_detail.html', context)


def download_resource(request, slug):
    """
    Tracks download counts and redirects to the media file or external URL.
    """
    resource = get_object_or_404(DigitalResource, slug=slug, is_published=True)
    DigitalResource.objects.filter(pk=resource.pk).update(download_count=F('download_count') + 1)
    
    if resource.file:
        return HttpResponseRedirect(resource.file.url)
    elif resource.external_url:
        return HttpResponseRedirect(resource.external_url)
    return redirect('resources:resource_detail', slug=resource.slug)


def question_papers(request):
    """
    Curated repository of BTEUP Board Examination Previous Year Question Papers.
    Organized by Engineering Department, Semester, and Academic Year.
    """
    dept_id = request.GET.get('department', '').strip()
    semester = request.GET.get('semester', '').strip()
    year = request.GET.get('year', '').strip()

    papers = DigitalResource.objects.filter(
        category='QUESTION_PAPER',
        is_published=True
    ).select_related('department', 'subject')

    if dept_id:
        papers = papers.filter(department_id=dept_id)
    if semester:
        papers = papers.filter(semester=semester)
    if year:
        papers = papers.filter(academic_year=year)

    paginator = Paginator(papers, 15)
    page_obj = paginator.get_page(request.GET.get('page'))

    departments = Department.objects.filter(is_active=True)
    academic_years = DigitalResource.objects.filter(
        category='QUESTION_PAPER', is_published=True
    ).values_list('academic_year', flat=True).distinct().exclude(academic_year='')

    context = {
        'page_obj': page_obj,
        'departments': departments,
        'academic_years': sorted(set(academic_years), reverse=True),
        'selected_dept': dept_id,
        'selected_semester': semester,
        'selected_year': year,
        'semesters_range': range(1, 7),
    }
    return render(request, 'resources/question_papers.html', context)


def syllabus_list(request):
    """
    Official BTEUP Diploma Curriculum and Subject-wise Syllabus Repository.
    """
    dept_id = request.GET.get('department', '').strip()
    syllabus_items = DigitalResource.objects.filter(
        category='SYLLABUS',
        is_published=True
    ).select_related('department', 'subject')

    if dept_id:
        syllabus_items = syllabus_items.filter(department_id=dept_id)

    departments = Department.objects.filter(is_active=True)

    return render(request, 'resources/syllabus_list.html', {
        'syllabus_items': syllabus_items,
        'departments': departments,
        'selected_dept': dept_id,
    })


def lecture_notes(request):
    """
    Faculty PPTs, Handouts, and Classroom Lecture Notes.
    """
    dept_id = request.GET.get('department', '').strip()
    semester = request.GET.get('semester', '').strip()

    notes = DigitalResource.objects.filter(
        category='LECTURE_NOTES',
        is_published=True
    ).select_related('department', 'subject')

    if dept_id:
        notes = notes.filter(department_id=dept_id)
    if semester:
        notes = notes.filter(semester=semester)

    departments = Department.objects.filter(is_active=True)

    return render(request, 'resources/lecture_notes.html', {
        'notes': notes,
        'departments': departments,
        'selected_dept': dept_id,
        'selected_semester': semester,
        'semesters_range': range(1, 7),
    })


def digital_library_home(request):
    """
    Digital Library & National E-Resource Portal Hub:
    NDLI, e-KUMBH (AICTE regional books), e-Granthalaya (EG4), SWAYAM/NPTEL, DOAJ, Shodhganga.
    """
    settings_obj = SiteSettings.load()
    ebooks = DigitalResource.objects.filter(category='EBOOK', is_published=True)[:6]
    journals = DigitalResource.objects.filter(category='JOURNAL', is_published=True)[:6]

    context = {
        'settings': settings_obj,
        'ebooks': ebooks,
        'journals': journals,
    }
    return render(request, 'resources/digital_library.html', context)


def digital_portals(request):
    """
    Detailed guide and access points for verified National Educational Portals.
    """
    settings_obj = SiteSettings.load()
    return render(request, 'resources/digital_portals.html', {'settings': settings_obj})

