from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100, help_text='Your task')
    description = models.TextField(max_length=300, help_text='Description of the task')

    def __str__(self):
        return self.title