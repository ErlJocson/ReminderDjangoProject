from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html', {})

def add_reminder_view(request):
    return render(request, 'add_reminder.html', {})