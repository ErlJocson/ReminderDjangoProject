from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReminderForm
from .models import Reminders
from datetime import datetime

@login_required
def index_view(request):
    reminders = Reminders.objects.all()
    for reminder in reminders:
        if reminder.date < datetime.date(datetime.now()):
            messages.warning(request, 'You missed a reminder!')
    return render(request, 'index.html', {
        "reminders":reminders,
        "title":"Home"
    })

@login_required
def add_reminder_view(request):
    form = ReminderForm(request.POST or None)
    if form.is_valid():
        if form.cleaned_data['date'] < datetime.date(datetime.now()):
            messages.warning(request, 'Invalid date')
            return redirect('add-reminder')
        Reminders.objects.create(
            title=form.cleaned_data["title"],
            content=form.cleaned_data["content"],
            date=form.cleaned_data['date'],
            user_id=request.user
        )
        messages.success(request, 'Reminder added.')
        return redirect('index')
    return render(request, 'add_reminder.html', {
        "form":form,
        "title":"Add reminders"
    })

@login_required
def delete_reminder(request, id):
    obj = get_object_or_404(Reminders, id = id)
    obj.delete()
    messages.warning(request, 'Reminder deleted.')
    return redirect('index')