from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.conf import settings
from .models import Topic, Note
from .forms import TopicForm, NoteForm


"""basic views"""

def index(request):
    return render(request, 'main/index.html')

@login_required
def topics(request):
    topics = Topic.objects.all()
    for topic in topics:
        if topic.owner != request.user:
            raise Http404
    return render(request, 'main/topics.html', {'topics': topics})

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    notes = topic.note_set.order_by('-date')
    return render(request, 'main/topic.html', {'topic': topic, 'notes': notes})

@login_required
def new_topic(request):
    if request.method != 'POST': 
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('main:topics')
    return render (request, 'main/new_topic.html', {'form': form})

@login_required
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

