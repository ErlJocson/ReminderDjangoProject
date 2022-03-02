from django.urls import path
from .views import *

urlpatterns = [
    path('home/', index_view, name='index'),
    path('add-reminder/', add_reminder_view, name='add-reminder')
]