from django import forms
from .models import JobTrackerEntry


class JobTrackerEntryForm(forms.ModelForm):
    class Meta:
        model = JobTrackerEntry
        fields = '__all__'