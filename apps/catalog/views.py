from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Book, BookCopy, Category
from apps.departments.models import Department

def catalog_search(request):
    """
    Public Online Public Access Catalogue (OPAC).
    Provides comprehensive multi-parameter search:
    Title, Author, ISBN, Publisher, Department, Category, Language, and Availability.
    """
    query = request.GET.get('q', '').strip()
    dept_id = request.GET.get('department', '').strip()
    cat_id = request.GET.get('category', '').strip()
    language = request.GET.get('language', '').strip()
    available_only = request.GET.get('available') == '1'
    sort_by = request.GET.get('sort', '-id')

    books = Book.objects.select_related('department', 'category', 'subject').prefetch_related('copies')

    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(isbn__icontains=query) |
            Q(publisher__icontains=query) |
            Q(tags__icontains=query) |
            Q(classification_number__icontains=query) |
            Q(copies__accession_number__icontains=query)
        ).distinct()

    if dept_id:
        books = books.filter(department_id=dept_id)

    if cat_id:
        books = books.filter(category_id=cat_id)

    if language:
        books = books.filter(language=language)

    if available_only:
        books = books.filter(copies__status='AVAILABLE').distinct()

    # Sorting
    if sort_by in ['title', '-title', 'author', 'publication_year', '-publication_year', '-id']:
        books = books.order_by(sort_by)
    else:
        books = books.order_by('-id')

    paginator = Paginator(books, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    departments = Department.objects.filter(is_active=True)
    categories = Category.objects.all()

    context = {
        'page_obj': page_obj,
        'query': query,
        'selected_dept': dept_id,
        'selected_cat': cat_id,
        'selected_language': language,
        'available_only': available_only,
        'sort_by': sort_by,
        'departments': departments,
        'categories': categories,
        'total_results': paginator.count,
    }
    return render(request, 'catalog/catalog_search.html', context)


def book_detail(request, slug):
    """
    Detailed bibliographic view for an individual book title.
    Displays cover, authors, publisher, classification, and live physical copy statuses.
    """
    book = get_object_or_404(
        Book.objects.select_related('department', 'category', 'subject').prefetch_related('copies'),
        slug=slug
    )
    copies = book.copies.all().order_by('accession_number')
    related_books = Book.objects.filter(
        Q(department=book.department) | Q(category=book.category)
    ).exclude(pk=book.pk).distinct()[:4]

    context = {
        'book': book,
        'copies': copies,
        'related_books': related_books,
    }
    return render(request, 'catalog/book_detail.html', context)


def new_arrivals(request):
    """
    Showcase page for recently acquired and catalogued library books.
    """
    arrivals = Book.objects.filter(is_new_arrival=True).select_related('department', 'category').order_by('-id')
    paginator = Paginator(arrivals, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalog/new_arrivals.html', {
        'page_obj': page_obj,
        'total_arrivals': paginator.count,
    })


def donations_list(request):
    """
    Special acknowledgement page for books donated by faculty members and patrons
    (Preserved from reference Blogger post regarding faculty donations).
    """
    donated_books = Book.objects.filter(is_donated=True).select_related('department').order_by('-id')
    return render(request, 'catalog/donations.html', {
        'donated_books': donated_books
    })

