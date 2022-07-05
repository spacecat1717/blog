from django.db import models
from django.conf import settings
import datetime

class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Note(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    photo1 = models.ImageField(upload_to = 'media/main/static/')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

