from django import forms
from .models import Reminders

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminders
        fields = (
            "title",
            "content",
            "date",
        )

        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "content":forms.Textarea(attrs={"class":"form-control"}),
            "date":forms.DateInput(attrs={"class":"form-control"}),
        }
