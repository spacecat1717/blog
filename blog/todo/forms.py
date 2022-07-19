from django import forms
from .models import ToDoEntry, ToDo

class ToDoEntryForm(forms.ModelForm):
    class Meta:
        model = ToDoEntry
        fields = ['text']

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title']
    


    
        
    
