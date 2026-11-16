from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Notice

def notice_list(request):
    """
    Public feed of library notices, circulars, and official orders.
    """
    category = request.GET.get('category', '').strip()
    query = request.GET.get('q', '').strip()

    notices = Notice.objects.filter(is_active=True)

    if category:
        notices = notices.filter(category=category)
    if query:
        notices = notices.filter(
            Q(title__icontains=query) |
            Q(short_summary__icontains=query) |
            Q(content__icontains=query)
        )

    paginator = Paginator(notices, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'notices/notice_list.html', {
        'page_obj': page_obj,
        'selected_category': category,
        'query': query,
        'categories': Notice.CATEGORY_CHOICES,
        'total_notices': paginator.count,
    })


def notice_detail(request, slug):
    """
    Individual notice view with official circular text and downloadable attachments.
    """
    notice = get_object_or_404(Notice, slug=slug, is_active=True)
    recent_notices = Notice.objects.filter(is_active=True).exclude(pk=notice.pk)[:5]

    return render(request, 'notices/notice_detail.html', {
        'notice': notice,
        'recent_notices': recent_notices,
    })

