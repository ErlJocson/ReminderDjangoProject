from django.shortcuts import render
from .forms import ReminderForm

def index_view(request):
    return render(request, 'index.html', {})

def add_reminder_view(request):
    form = ReminderForm(request.POST or None)
    return render(request, 'add_reminder.html', {
        "form":form
    })