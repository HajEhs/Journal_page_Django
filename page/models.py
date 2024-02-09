from django.db import models

class Journal(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return f'{self.name}'

class Note(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.date}'


