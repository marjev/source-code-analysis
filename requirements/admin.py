from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget

from .models import UserRequirement


@admin.register(UserRequirement)
class UserRequirementAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
