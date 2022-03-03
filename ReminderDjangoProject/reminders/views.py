from django.shortcuts import render
from .forms import ReminderForm
from .models import Reminders

def index_view(request):
    reminders = Reminders.objects.all()
    return render(request, 'index.html', {
        "reminders":reminders
    })

def add_reminder_view(request):
    form = ReminderForm(request.POST or None)
    if form.is_valid():
        # Reminders.objects.create(
        #     title=form.cleaned_data["title"],
        #     content=form.cleaned_data["content"],
        #     date=form.cleaned_data['date'],
        #     user_id=request.user.id
        # )
        form = ReminderForm

    return render(request, 'add_reminder.html', {
        "form":form
    })