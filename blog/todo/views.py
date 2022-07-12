from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.conf import settings
from .models import ToDoNote
from .forms import ToDoNoteForm, ChangeStatus


@login_required
def to_do_notes(request):
    """showing list of to do note with to do entries"""
    notes = ToDoNote.objects.all()
    for note in notes:
        if note.owner!= request.user:
            raise Http404
    return render(request, 'todo/noteslist.html', {'notes': notes})

@login_required
def to_do_note(request, note_id):
    """showing one to do note"""
    note = ToDoNote.objects.get(id=note_id)
    return render(request, 'todo/note.html', {'note': note})

@login_required
def to_do_new(request):
    if request.method == 'POST':
        form = ToDoNoteForm(request.POST)
        new_todo = form.save(commit=False)
        new_todo.owner = request.user
        new_todo.save()
        return redirect('todo:noteslist')
    form = ToDoNoteForm()
    return render(request, 'todo/new_todo.html', {'form': form})

@login_required
def to_do_update(request, entry_id):
    #update status of enntries in to do
    pass

