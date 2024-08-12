from django.db import models
from django.contrib.auth.models import AbstractUser

class student(AbstractUser):
    rollno = models.CharField(max_length=50, unique=True)
    department = models.CharField(max_length=50)


class Event(models.Model):
    name = models.CharField(max_length=50)
    shortdescription = models.TextField(null=True)
    description = models.TextField()
    date = models.DateField()
    timing = models.CharField(max_length=50)
    imagepath = models.CharField(max_length=75)
    venue = models.CharField(max_length=50)

    limit = models.PositiveIntegerField()
    closed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Submission(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    teamname = models.CharField(max_length=100, null=True)
    
    participant1 = models.CharField(max_length=75)
    mail1 = models.EmailField()
    
    participant2 = models.CharField(max_length=75, null=True)
    mail2 = models.EmailField(null=True)
    
    participant3 = models.CharField(max_length=75, null=True)
    mail3 = models.EmailField(null=True)
    
    contact = models.CharField(max_length=25)
    
    def __str__(self):
        return self.event.name
    
    
