from django import forms
from .models import Tasks

class AddTaskForm(forms.ModelForm):
    # title = forms.CharField(label="Title", max_length=20),
    # deadline = forms.DateField()
    # description = forms.CharField(widget=forms.Textarea)
    # importance = forms.CharField(max_length=6)
    class Meta:
        model = Tasks
        fields = "__all__"