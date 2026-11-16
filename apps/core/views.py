from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from apps.core.models import SiteSettings, HeroSlide
from apps.departments.models import Department
from apps.catalog.models import Book, BookCopy, Category
from apps.resources.models import DigitalResource
from apps.notices.models import Notice
from apps.events.models import LibraryEvent, GalleryImage
from apps.pages.models import Facility, FAQ

def home(request):
    """
    Homepage of Government Polytechnic Madhogarh Central Library.
    Aggregates hero, live catalog search, quick access cards, urgent notices,
    digital library gateways, department hubs, new arrivals, and live stats.
    """
    settings_obj = SiteSettings.load()
    
    # Live database statistics (no fictional numbers!)
    total_titles = Book.objects.count()
    total_copies = BookCopy.objects.count()
    total_resources = DigitalResource.objects.filter(is_published=True).count()
    total_question_papers = DigitalResource.objects.filter(is_published=True, category='QUESTION_PAPER').count()
    total_departments = Department.objects.filter(is_active=True).count()
    
    # Notices: priority notices, pinned notices and active circulars
    latest_notices = Notice.objects.filter(is_active=True).order_by('-is_pinned', '-publish_date')[:6]
    
    # New arrivals in library
    new_arrivals = Book.objects.filter(is_new_arrival=True).select_related('department', 'category')[:8]
    if not new_arrivals.exists():
        new_arrivals = Book.objects.all().select_related('department', 'category')[:8]
        
    # Featured facilities
    facilities = Facility.objects.filter(is_active=True).order_by('display_order')[:6]
    
    # Upcoming or featured events
    upcoming_events = LibraryEvent.objects.filter(is_active=True).order_by('-start_date')[:3]
    
    # Gallery photos for carousel / showcase
    featured_photos = GalleryImage.objects.filter(is_featured_home=True)[:6]

    # Responsive Hero Slideshow (query active slides ordered by order)
    slides = HeroSlide.objects.filter(is_active=True).order_by('order')

    context = {
        'settings': settings_obj,
        'slides': slides,
        'hero_slides': slides,
        'stats': {
            'total_titles': total_titles,
            'total_copies': total_copies,
            'total_resources': total_resources,
            'total_question_papers': total_question_papers,
            'total_departments': total_departments,
        },
        'latest_notices': latest_notices,
        'new_arrivals': new_arrivals,
        'facilities': facilities,
        'upcoming_events': upcoming_events,
        'featured_photos': featured_photos,
    }
    return render(request, 'core/home.html', context)


def global_search(request):
    """
    Unified institutional search engine searching across:
    Books, Digital Resources (Question papers, syllabus, notes), Notices, and Departments.
    """
    query = request.GET.get('q', '').strip()
    category = request.GET.get('cat', 'all').strip()
    
    books = Book.objects.none()
    resources = DigitalResource.objects.none()
    notices = Notice.objects.none()
    departments = Department.objects.none()
    
    if query:
        if category in ['all', 'books']:
            books = Book.objects.filter(
                Q(title__icontains=query) |
                Q(author__icontains=query) |
                Q(isbn__icontains=query) |
                Q(publisher__icontains=query) |
                Q(tags__icontains=query) |
                Q(classification_number__icontains=query)
            ).select_related('department', 'category').distinct()[:25]
            
        if category in ['all', 'resources', 'question_papers', 'notes', 'syllabus']:
            res_qs = DigitalResource.objects.filter(is_published=True)
            if category == 'question_papers':
                res_qs = res_qs.filter(category='QUESTION_PAPER')
            elif category == 'notes':
                res_qs = res_qs.filter(category='LECTURE_NOTES')
            elif category == 'syllabus':
                res_qs = res_qs.filter(category='SYLLABUS')
                
            resources = res_qs.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(author_or_faculty__icontains=query) |
                Q(academic_year__icontains=query)
            ).select_related('department', 'subject').distinct()[:25]
            
        if category in ['all', 'notices']:
            notices = Notice.objects.filter(
                is_active=True
            ).filter(
                Q(title__icontains=query) |
                Q(short_summary__icontains=query) |
                Q(content__icontains=query)
            ).distinct()[:15]
            
        if category in ['all', 'departments']:
            departments = Department.objects.filter(
                is_active=True
            ).filter(
                Q(name__icontains=query) |
                Q(code__icontains=query) |
                Q(description__icontains=query)
            )[:5]

    total_results = (
        (books.count() if hasattr(books, 'count') else len(books)) +
        (resources.count() if hasattr(resources, 'count') else len(resources)) +
        (notices.count() if hasattr(notices, 'count') else len(notices)) +
        (departments.count() if hasattr(departments, 'count') else len(departments))
    )

    context = {
        'query': query,
        'category': category,
        'books': books,
        'resources': resources,
        'notices': notices,
        'departments': departments,
        'total_results': total_results,
    }
    return render(request, 'core/search_results.html', context)


def contact(request):
    """
    Contact details, campus map location, operating hours, and helpline numbers.
    """
    settings_obj = SiteSettings.load()
    return render(request, 'core/contact.html', {'settings': settings_obj})


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /dashboard/",
        "Disallow: /accounts/",
        "Allow: /",
        "Sitemap: https://gpmadhogarh.ac.in/library/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def sitemap_xml(request):
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url><loc>https://gpmadhogarh.ac.in/library/</loc><priority>1.0</priority></url>
    <url><loc>https://gpmadhogarh.ac.in/library/about/</loc><priority>0.8</priority></url>
    <url><loc>https://gpmadhogarh.ac.in/library/catalog/</loc><priority>0.9</priority></url>
    <url><loc>https://gpmadhogarh.ac.in/library/digital-library/</loc><priority>0.9</priority></url>
    <url><loc>https://gpmadhogarh.ac.in/library/resources/question-papers/</loc><priority>0.9</priority></url>
    <url><loc>https://gpmadhogarh.ac.in/library/resources/syllabus/</loc><priority>0.8</priority></url>
    <url><loc>https://gpmadhogarh.ac.in/library/departments/</loc><priority>0.8</priority></url>
    <url><loc>https://gpmadhogarh.ac.in/library/rules/</loc><priority>0.7</priority></url>
    <url><loc>https://gpmadhogarh.ac.in/library/services/</loc><priority>0.8</priority></url>
    <url><loc>https://gpmadhogarh.ac.in/library/notices/</loc><priority>0.8</priority></url>
    <url><loc>https://gpmadhogarh.ac.in/library/contact/</loc><priority>0.7</priority></url>
</urlset>"""
    return HttpResponse(xml, content_type="application/xml")


def custom_404_view(request, exception=None):
    return render(request, 'core/404.html', status=404)


def custom_500_view(request):
    return render(request, 'core/500.html', status=500)

