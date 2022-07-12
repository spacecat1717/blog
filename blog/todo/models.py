from django.db import models
from account.models import Account
import datetime

class ToDoNote(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    date = date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

