from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


IMPORTANCE = {
    ('low', 'LOW'),
    ('medium', 'MEDIUM'),
    ('high', 'HIGH'),
}


class Tasks(models.Model):
    title = models.CharField(max_length=20)
    deadline = models.DateField()
    description = models.TextField()
    importance = models.CharField(max_length=6, choices=IMPORTANCE, default='medium')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_manager:home-page')
