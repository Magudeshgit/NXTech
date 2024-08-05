from django.db import models
from django.contrib.auth.models import AbstractUser

class student(AbstractUser):
    rollno = models.CharField(max_length=50, unique=True)
    department = models.CharField(max_length=50)


class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    timing = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
