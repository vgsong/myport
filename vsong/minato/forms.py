from django import forms
from .models import JobTrackerEntry
from .models import GuestBookEntry


class JobTrackerEntryForm(forms.ModelForm):
    class Meta:
        model = JobTrackerEntry
        fields = '__all__'

class GuestBookForm(forms.ModelForm):
    class Meta:
        model = GuestBookEntry
        fields = '__all__'