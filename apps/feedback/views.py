from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Feedback
from .forms import FeedbackForm

def feedback_form_view(request):
    """
    Public student and faculty feedback submission form.
    """
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()
            messages.success(
                request,
                f"Thank you, {feedback.name}! Your feedback has been received. "
                "Our library administration constantly reviews user suggestions to enhance service quality."
            )
            return redirect('feedback:feedback')
        else:
            messages.error(request, "Please review the highlighted errors below.")
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback_form.html', {'form': form})

