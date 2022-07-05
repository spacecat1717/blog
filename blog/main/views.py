from django.shortcuts import render, redirect
from django.conf import settings
from .models import Topic, Note

def index(request):
    return render(request, 'main/index.html')

def topics(request):
    topics = Topic.objects.all()
    return render(request, 'main/topics.html', {'topics': topics})
