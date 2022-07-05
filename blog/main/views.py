from django.shortcuts import render, redirect
from django.conf import settings
from .models import Topic, Note

def index(request):
    return render(request, 'main/index.html')

def topics(request):
    topics = Topic.objects.all()
    return render(request, 'main/topics.html', {'topics': topics})

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    notes = topic.note_set.order_by('-date')
    return render(request, 'main/topic.html', {'notes': notes})