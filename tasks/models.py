from django.db import models

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
