from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    TaskText = models.CharField('Описание дела', max_length=250)
    # author = models.CharField('Автор', max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.TaskText

    def get_absolute_url(self):
        return f'/tasks/'