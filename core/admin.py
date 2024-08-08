from django.contrib import admin
from .models import Event, student, Submission

admin.site.register([Event, student, Submission])