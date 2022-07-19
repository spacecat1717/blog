from django.urls import path
from django.conf import settings
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todos, name='todos'),
    path('new_todo/', views.new_todo, name='new_todo'),
    path('<todo_id>/edit/', views.todo_edit, name='todo_edit'),
    
    ]