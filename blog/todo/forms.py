from django import forms
from .models import ToDoNote

class ToDoNoteForm(forms.ModelForm):
    class Meta:
        model = ToDoNote
        fields = ['title', 'text', 'status']


class ChangeStatus(forms.Form):
    status = forms.BooleanField(required=False)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
