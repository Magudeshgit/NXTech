from django.contrib import admin
from .models import Event, student

admin.site.register([Event, student])