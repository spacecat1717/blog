from django.urls import path
from django.conf import settings
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.to_do_notes, name='noteslist'),
    path('notes/<note_id>', views.to_do_note, name='note'),
    path('notes/new_todo/', views.to_do_new, name='new_todo'),
]