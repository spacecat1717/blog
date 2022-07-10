from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import Topic, Note
from .forms import TopicForm, NoteForm


"""basic views"""

def index(request):
    return render(request, 'main/index.html')

def topics(request):
    topics = Topic.objects.all()
    return render(request, 'main/topics.html', {'topics': topics})

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    notes = topic.note_set.order_by('-date')
    return render(request, 'main/topic.html', {'topic': topic, 'notes': notes})

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
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method != 'POST':
        note_form = NoteForm()
    else:
        note_form = NoteForm(request.POST, request.FILES)
        if note_form.is_valid():
            new_note = note_form.save(commit=False)
            new_note.topic = topic
            img_obj = note_form.instance
            new_note.save()
            return redirect('main:topic', topic_id=topic_id)
    return render (request, 'main/new_note.html', {'topic': topic, 'note_form': note_form})

