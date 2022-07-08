from django.shortcuts import render, redirect
from django.conf import settings
from .models import Topic, Note
from .forms import TopicForm, NoteForm

def index(request):
    return render(request, 'main/index.html')

def topics(request):
    topics = Topic.objects.all()
    return render(request, 'main/topics.html', {'topics': topics})

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    notes = topic.note_set.order_by('-date')
    return render(request, 'main/topic.html', {'notes': notes})

def new_topic(request):
    if request.method != 'POST': 
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:topics')
    return render (request, 'main/new_topic.html', {'form': form})

def new_note(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method == 'POST':
        note_form = NoteForm(data=request.POST)
        if note_form.is_valid():
            note_form.save()
            return redirect('main:topic', topic_id=topic_id)
    note_form = NoteForm()
    return render (request, 'main/new_note.html', {'note_form': note_form})
