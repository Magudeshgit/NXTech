from django.contrib import admin
from .models import Event, student, Submission
from import_export.admin import ExportActionMixin   

admin.site.register(Event)


class submissionExport(ExportActionMixin, admin.ModelAdmin):
    pass

admin.site.register(Submission, submissionExport)