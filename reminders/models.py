from django.db import models
from django.contrib.auth.models import User

class Reminders(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    