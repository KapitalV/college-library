from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import LibraryEvent, GalleryImage

def event_list(request):
    """
    List of institutional library events, orientations, book fairs, and workshops.
    """
    event_type = request.GET.get('type', '').strip()
    events = LibraryEvent.objects.filter(is_active=True)
    if event_type:
        events = events.filter(event_type=event_type)

    paginator = Paginator(events, 9)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'events/event_list.html', {
        'page_obj': page_obj,
        'selected_type': event_type,
        'event_types': LibraryEvent.EVENT_TYPE_CHOICES,
    })


def event_detail(request, slug):
    """
    Detailed event coverage with program schedule, description, and attached photos.
    """
    event = get_object_or_404(LibraryEvent, slug=slug, is_active=True)
    photos = event.gallery_photos.all()
    other_events = LibraryEvent.objects.filter(is_active=True).exclude(pk=event.pk)[:4]

    return render(request, 'events/event_detail.html', {
        'event': event,
        'photos': photos,
        'other_events': other_events,
    })


def gallery_list(request):
    """
    Photo gallery showcasing library reading halls, stack areas, orientation sessions,
    book exhibitions, and campus activities.
    Replaces the broken Blogger gallery page.
    """
    photos = GalleryImage.objects.all().select_related('event')
    paginator = Paginator(photos, 16)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'events/gallery_list.html', {
        'page_obj': page_obj,
    })

