from django.shortcuts import render, get_object_or_404
from .models import Department, Subject
from apps.catalog.models import Book
from apps.resources.models import DigitalResource

def department_list(request):
    """
    Directory of all active academic departments and polytechnic disciplines.
    """
    departments = Department.objects.filter(is_active=True).prefetch_related('subjects')
    return render(request, 'departments/department_list.html', {
        'departments': departments
    })


def department_detail(request, slug):
    """
    Department Resource Hub:
    Displays department overview, subjects per semester, available books,
    previous year question papers, syllabus, and lecture notes.
    """
    department = get_object_or_404(Department, slug=slug, is_active=True)
    
    # Selected semester filter (default 0 means show overview of all)
    semester = request.GET.get('semester')
    try:
        semester = int(semester) if semester else None
    except ValueError:
        semester = None

    subjects = department.subjects.filter(is_active=True)
    if semester:
        subjects = subjects.filter(semester=semester)

    # Related books in catalog
    books = Book.objects.filter(department=department).select_related('category')[:12]
    
    # Related digital resources
    resources_qs = DigitalResource.objects.filter(department=department, is_published=True)
    if semester:
        resources_qs = resources_qs.filter(semester=semester)
        
    question_papers = resources_qs.filter(category='QUESTION_PAPER')[:10]
    syllabus_items = resources_qs.filter(category='SYLLABUS')[:5]
    lecture_notes = resources_qs.filter(category='LECTURE_NOTES')[:10]

    context = {
        'department': department,
        'selected_semester': semester,
        'subjects': subjects,
        'books': books,
        'question_papers': question_papers,
        'syllabus_items': syllabus_items,
        'lecture_notes': lecture_notes,
        'semesters_range': range(1, 7),
    }
    return render(request, 'departments/department_detail.html', context)


def semester_resources(request, slug, semester):
    """
    Direct route shortcut to semester-specific resources for a department.
    """
    department = get_object_or_404(Department, slug=slug, is_active=True)
    subjects = department.subjects.filter(is_active=True, semester=semester)
    resources = DigitalResource.objects.filter(department=department, semester=semester, is_published=True)
    
    context = {
        'department': department,
        'semester': semester,
        'subjects': subjects,
        'resources': resources,
    }
    return render(request, 'departments/semester_resources.html', context)

