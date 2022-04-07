from django import forms
from .models import Reminders

class DateInput(forms.DateInput):
    input_type = 'date'

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
            "date":DateInput(attrs={"class":"form-control"}),
        }
