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
        form.save()
    return render(request, 'add_reminder.html', {
        "form":form
    })