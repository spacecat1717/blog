from django.db import models
from account.models import Account
import datetime

class ToDo(models.Model):
    title = models.CharField(max_length=150)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ToDoEntry(models.Model):
    todo = models.ForeignKey(ToDo, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
