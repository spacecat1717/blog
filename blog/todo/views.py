from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.conf import settings
from .models import ToDo, ToDoEntry
from .forms import ToDoEntryForm, ToDoForm

@login_required
def todos(request):
    todos = ToDo.objects.all()
    return render(request, 'todo/todos.html', {'todos': todos}) #create a template!!!!!!

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
def todo(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    entries = todo.todoentry_set.order_by('id')    
    return render(request, 'todo/todo.html', {'todo': todo, 'entries': entries})
    

@login_required
def todo_edit(request, todo_id):
    pass
    
@login_required
def new_entry(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = ToDoEntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.todo = todo
            new_entry.save()
            return redirect('todo:todos')
    form = ToDoEntryForm()
    return render(request, 'todo/new_entry.html', {'todo': todo, 'form':form})
            


