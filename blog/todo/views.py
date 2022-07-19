from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.conf import settings
from .models import ToDo, ToDoEntry
from .forms import ToDoEntryForm, ToDoForm

@login_required
def todos(request):
    todos = ToDo.objects.all()
    return render(request, 'todos/todos.html', {'todos': todos}) #create a template!!!!!!

@login_required
def new_todo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            new_todo = form.save(commit=False)
            new_todo.owner = request.user
            new_todo.save()
            return redirect('todo:todos')
    form = ToDoForm()
    return render(request, 'todo/new_todo.html', {'form': form})

@login_required
def todo_edit(request, todo_id):
    pass
    


