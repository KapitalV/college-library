import csv
import io
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponse
from django.utils.text import slugify

from apps.catalog.models import Book, BookCopy, Category
from apps.resources.models import DigitalResource
from apps.notices.models import Notice
from apps.departments.models import Department, Subject
from apps.library_services.models import MembershipApplication, BookRecommendation, ResourceRequest
from apps.feedback.models import Feedback
from apps.core.models import SiteSettings, MenuItem
from .forms import (
    DashboardBookForm, DashboardBookCopyForm, DashboardResourceForm,
    DashboardNoticeForm, DashboardSiteSettingsForm, CsvImportForm
)

def staff_required(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser or hasattr(user, 'staff_profile'))


@login_required
@user_passes_test(staff_required)
def dashboard_overview(request):
    """
    Librarian Administration Executive Dashboard.
    Provides real-time statistics and pending workflow items.
    """
    total_books = Book.objects.count()
    total_copies = BookCopy.objects.count()
    available_copies = BookCopy.objects.filter(status='AVAILABLE').count()
    issued_copies = BookCopy.objects.filter(status='ISSUED').count()
    total_resources = DigitalResource.objects.count()
    active_notices = Notice.objects.filter(is_active=True).count()
    
    pending_memberships = MembershipApplication.objects.filter(status='PENDING').count()
    pending_recommendations = BookRecommendation.objects.filter(status='SUBMITTED').count()
    pending_requests = ResourceRequest.objects.filter(status='PENDING').count()
    unread_feedback = Feedback.objects.filter(is_reviewed=False).count()

    recent_books = Book.objects.select_related('department', 'category').order_by('-id')[:5]
    recent_applications = MembershipApplication.objects.filter(status='PENDING').order_by('-created_at')[:5]
    recent_notices = Notice.objects.order_by('-publish_date')[:5]

    context = {
        'stats': {
            'total_books': total_books,
            'total_copies': total_copies,
            'available_copies': available_copies,
            'issued_copies': issued_copies,
            'total_resources': total_resources,
            'active_notices': active_notices,
            'pending_memberships': pending_memberships,
            'pending_recommendations': pending_recommendations,
            'pending_requests': pending_requests,
            'unread_feedback': unread_feedback,
        },
        'recent_books': recent_books,
        'recent_applications': recent_applications,
        'recent_notices': recent_notices,
    }
    return render(request, 'dashboard/overview.html', context)


# ---------------- BOOK CATALOG MANAGEMENT ----------------

@login_required
@user_passes_test(staff_required)
def dashboard_book_list(request):
    query = request.GET.get('q', '').strip()
    dept_id = request.GET.get('department', '').strip()
    cat_id = request.GET.get('category', '').strip()

    books = Book.objects.select_related('department', 'category').prefetch_related('copies').order_by('-id')

    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query) | books.filter(isbn__icontains=query)
    if dept_id:
        books = books.filter(department_id=dept_id)
    if cat_id:
        books = books.filter(category_id=cat_id)

    paginator = Paginator(books, 15)
    page_obj = paginator.get_page(request.GET.get('page'))

    departments = Department.objects.all()
    categories = Category.objects.all()

    return render(request, 'dashboard/book_list.html', {
        'page_obj': page_obj,
        'query': query,
        'selected_dept': dept_id,
        'selected_cat': cat_id,
        'departments': departments,
        'categories': categories,
        'total_books': paginator.count,
    })


@login_required
@user_passes_test(staff_required)
def dashboard_book_create(request):
    if request.method == 'POST':
        form = DashboardBookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, f"Book '{book.title}' created successfully! You can now add physical inventory copies.")
            return redirect('dashboard:book_copies', book_id=book.id)
    else:
        form = DashboardBookForm()
    return render(request, 'dashboard/book_form.html', {'form': form, 'title': 'Add New Book'})


@login_required
@user_passes_test(staff_required)
def dashboard_book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = DashboardBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f"Book '{book.title}' updated successfully.")
            return redirect('dashboard:book_list')
    else:
        form = DashboardBookForm(instance=book)
    return render(request, 'dashboard/book_form.html', {'form': form, 'book': book, 'title': f'Edit Book: {book.title}'})


@login_required
@user_passes_test(staff_required)
def dashboard_book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        title = book.title
        book.delete()
        messages.success(request, f"Book '{title}' and all associated accession records were deleted.")
        return redirect('dashboard:book_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': book, 'type': 'Book'})


@login_required
@user_passes_test(staff_required)
def dashboard_book_copies(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    copies = book.copies.all().order_by('accession_number')

    if request.method == 'POST':
        form = DashboardBookCopyForm(request.POST)
        if form.is_valid():
            copy = form.save(commit=False)
            copy.book = book
            copy.save()
            messages.success(request, f"Copy with Accession #{copy.accession_number} added successfully.")
            return redirect('dashboard:book_copies', book_id=book.id)
    else:
        form = DashboardBookCopyForm()

    return render(request, 'dashboard/book_copies.html', {
        'book': book,
        'copies': copies,
        'form': form,
    })


@login_required
@user_passes_test(staff_required)
def dashboard_copy_delete(request, pk):
    copy = get_object_or_404(BookCopy, pk=pk)
    book_id = copy.book.id
    if request.method == 'POST':
        acc = copy.accession_number
        copy.delete()
        messages.success(request, f"Accession #{acc} removed.")
        return redirect('dashboard:book_copies', book_id=book_id)
    return render(request, 'dashboard/confirm_delete.html', {'object': copy, 'type': 'Book Copy'})


# ---------------- CSV IMPORT / EXPORT ----------------

@login_required
@user_passes_test(staff_required)
def export_books_csv(request):
    """
    Exports the entire library book catalog and copy inventory as a CSV file.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mmit_library_catalog.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'AccessionNumber', 'Title', 'Author', 'ISBN', 'Publisher',
        'Year', 'Department', 'Category', 'Classification', 'ShelfLocation', 'Status'
    ])

    copies = BookCopy.objects.select_related('book', 'book__department', 'book__category').all()
    for c in copies:
        writer.writerow([
            c.accession_number,
            c.book.title,
            c.book.author,
            c.book.isbn,
            c.book.publisher,
            c.book.publication_year or '',
            c.book.department.code if c.book.department else '',
            c.book.category.name if c.book.category else '',
            c.book.classification_number,
            c.shelf_location,
            c.status,
        ])

    return response


@login_required
@user_passes_test(staff_required)
def import_books_csv(request):
    """
    Bulk import books and inventory copies from CSV with validation and database transactions.
    """
    if request.method == 'POST':
        form = CsvImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            try:
                decoded_file = csv_file.read().decode('utf-8-sig', errors='ignore')
                io_string = io.StringIO(decoded_file)
                reader = csv.DictReader(io_string)

                created_books = 0
                created_copies = 0
                errors = []

                with transaction.atomic():
                    for row_num, row in enumerate(reader, start=2):
                        title = row.get('Title', '').strip()
                        author = row.get('Author', '').strip()
                        if not title or not author:
                            errors.append(f"Row {row_num}: Missing Title or Author. Skipped.")
                            continue

                        isbn = row.get('ISBN', '').strip()
                        publisher = row.get('Publisher', '').strip()
                        dept_code = row.get('Department', '').strip()
                        cat_name = row.get('Category', '').strip()
                        shelf = row.get('ShelfLocation', '').strip() or 'Rack 1 - Shelf A'
                        acc_no = row.get('AccessionNumber', '').strip()

                        # Department lookup or create
                        dept = None
                        if dept_code:
                            dept = Department.objects.filter(code__iexact=dept_code).first()

                        # Category lookup or create
                        cat = None
                        if cat_name:
                            cat, _ = Category.objects.get_or_create(name=cat_name)

                        # Book lookup or create
                        book, b_created = Book.objects.get_or_create(
                            title=title,
                            author=author,
                            defaults={
                                'isbn': isbn,
                                'publisher': publisher,
                                'department': dept,
                                'category': cat,
                            }
                        )
                        if b_created:
                            created_books += 1

                        # Copy creation
                        if acc_no:
                            if not BookCopy.objects.filter(accession_number=acc_no).exists():
                                BookCopy.objects.create(
                                    book=book,
                                    accession_number=acc_no,
                                    shelf_location=shelf,
                                    status='AVAILABLE'
                                )
                                created_copies += 1

                msg = f"CSV Import complete! Created {created_books} books and {created_copies} accession copies."
                if errors:
                    msg += f" (Warnings: {len(errors)})"
                messages.success(request, msg)
                return redirect('dashboard:book_list')
            except Exception as e:
                messages.error(request, f"Error processing CSV: {str(e)}")
    else:
        form = CsvImportForm()

    return render(request, 'dashboard/import_csv.html', {'form': form})


# ---------------- DIGITAL RESOURCES MANAGEMENT ----------------

@login_required
@user_passes_test(staff_required)
def dashboard_resource_list(request):
    resources = DigitalResource.objects.select_related('department', 'subject').order_by('-id')
    paginator = Paginator(resources, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'dashboard/resource_list.html', {'page_obj': page_obj})


@login_required
@user_passes_test(staff_required)
def dashboard_resource_create(request):
    if request.method == 'POST':
        form = DashboardResourceForm(request.POST, request.FILES)
        if form.is_valid():
            res = form.save()
            messages.success(request, f"Resource '{res.title}' published successfully.")
            return redirect('dashboard:resource_list')
    else:
        form = DashboardResourceForm()
    return render(request, 'dashboard/resource_form.html', {'form': form, 'title': 'Upload Academic Resource'})


@login_required
@user_passes_test(staff_required)
def dashboard_resource_edit(request, pk):
    resource = get_object_or_404(DigitalResource, pk=pk)
    if request.method == 'POST':
        form = DashboardResourceForm(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            form.save()
            messages.success(request, f"Resource '{resource.title}' updated.")
            return redirect('dashboard:resource_list')
    else:
        form = DashboardResourceForm(instance=resource)
    return render(request, 'dashboard/resource_form.html', {'form': form, 'resource': resource, 'title': 'Edit Resource'})


@login_required
@user_passes_test(staff_required)
def dashboard_resource_delete(request, pk):
    resource = get_object_or_404(DigitalResource, pk=pk)
    if request.method == 'POST':
        title = resource.title
        resource.delete()
        messages.success(request, f"Resource '{title}' deleted.")
        return redirect('dashboard:resource_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': resource, 'type': 'Digital Resource'})


# ---------------- NOTICES MANAGEMENT ----------------

@login_required
@user_passes_test(staff_required)
def dashboard_notice_list(request):
    notices = Notice.objects.order_by('-publish_date', '-id')
    paginator = Paginator(notices, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'dashboard/notice_list.html', {'page_obj': page_obj})


@login_required
@user_passes_test(staff_required)
def dashboard_notice_create(request):
    if request.method == 'POST':
        form = DashboardNoticeForm(request.POST, request.FILES)
        if form.is_valid():
            n = form.save()
            messages.success(request, f"Notice '{n.title}' published successfully.")
            return redirect('dashboard:notice_list')
    else:
        form = DashboardNoticeForm()
    return render(request, 'dashboard/notice_form.html', {'form': form, 'title': 'Publish Notice / Circular'})


@login_required
@user_passes_test(staff_required)
def dashboard_notice_edit(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == 'POST':
        form = DashboardNoticeForm(request.POST, request.FILES, instance=notice)
        if form.is_valid():
            form.save()
            messages.success(request, f"Notice '{notice.title}' updated.")
            return redirect('dashboard:notice_list')
    else:
        form = DashboardNoticeForm(instance=notice)
    return render(request, 'dashboard/notice_form.html', {'form': form, 'notice': notice, 'title': 'Edit Notice'})


@login_required
@user_passes_test(staff_required)
def dashboard_notice_delete(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == 'POST':
        title = notice.title
        notice.delete()
        messages.success(request, f"Notice '{title}' deleted.")
        return redirect('dashboard:notice_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': notice, 'type': 'Notice'})


# ---------------- STUDENT SERVICES & WORKFLOWS ----------------

@login_required
@user_passes_test(staff_required)
def dashboard_memberships(request):
    status_filter = request.GET.get('status', '').strip()
    apps = MembershipApplication.objects.select_related('department').order_by('-created_at')
    if status_filter:
        apps = apps.filter(status=status_filter)

    paginator = Paginator(apps, 15)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'dashboard/memberships.html', {
        'page_obj': page_obj,
        'selected_status': status_filter,
    })


@login_required
@user_passes_test(staff_required)
def dashboard_membership_update(request, pk):
    app = get_object_or_404(MembershipApplication, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        card_no = request.POST.get('card_number', '').strip()
        remarks = request.POST.get('librarian_remarks', '').strip()
        if status:
            app.status = status
        if card_no:
            app.card_number = card_no
        app.librarian_remarks = remarks
        app.save()
        messages.success(request, f"Membership application #{app.id} for {app.full_name} updated to {app.get_status_display()}.")
    return redirect('dashboard:memberships')


@login_required
@user_passes_test(staff_required)
def dashboard_recommendations(request):
    recs = BookRecommendation.objects.select_related('department').order_by('-created_at')
    paginator = Paginator(recs, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'dashboard/recommendations.html', {'page_obj': page_obj})


@login_required
@user_passes_test(staff_required)
def dashboard_recommendation_update(request, pk):
    rec = get_object_or_404(BookRecommendation, pk=pk)
    if request.method == 'POST':
        rec.status = request.POST.get('status', rec.status)
        rec.librarian_notes = request.POST.get('librarian_notes', rec.librarian_notes)
        rec.save()
        messages.success(request, f"Recommendation for '{rec.title}' updated.")
    return redirect('dashboard:recommendations')


@login_required
@user_passes_test(staff_required)
def dashboard_requests(request):
    reqs = ResourceRequest.objects.select_related('department').order_by('-created_at')
    paginator = Paginator(reqs, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'dashboard/resource_requests.html', {'page_obj': page_obj})


@login_required
@user_passes_test(staff_required)
def dashboard_request_update(request, pk):
    req_obj = get_object_or_404(ResourceRequest, pk=pk)
    if request.method == 'POST':
        req_obj.status = request.POST.get('status', req_obj.status)
        req_obj.librarian_reply = request.POST.get('librarian_reply', req_obj.librarian_reply)
        req_obj.save()
        messages.success(request, f"Resource request #{req_obj.id} updated.")
    return redirect('dashboard:requests')


@login_required
@user_passes_test(staff_required)
def dashboard_feedback(request):
    feedbacks = Feedback.objects.order_by('-created_at')
    if request.method == 'POST':
        pk = request.POST.get('feedback_id')
        fb = get_object_or_404(Feedback, pk=pk)
        fb.is_reviewed = True
        fb.admin_response = request.POST.get('admin_response', '')
        fb.save()
        messages.success(request, "Feedback marked as reviewed.")
        return redirect('dashboard:feedback')

    paginator = Paginator(feedbacks, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'dashboard/feedback_list.html', {'page_obj': page_obj})


# ---------------- INSTITUTIONAL SETTINGS ----------------

@login_required
@user_passes_test(lambda u: u.is_superuser or (hasattr(u, 'staff_profile') and u.staff_profile.role == 'ADMIN'))
def dashboard_settings(request):
    settings_obj = SiteSettings.load()
    if request.method == 'POST':
        form = DashboardSiteSettingsForm(request.POST, request.FILES, instance=settings_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Institutional Site Settings successfully updated.")
            return redirect('dashboard:settings')
    else:
        form = DashboardSiteSettingsForm(instance=settings_obj)

    return render(request, 'dashboard/settings_form.html', {'form': form, 'settings': settings_obj})

