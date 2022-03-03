from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('reminders.urls')),
    path('auth/', include('auth.urls')),
    path('admin/', admin.site.urls),
]
