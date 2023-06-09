from django.contrib import admin

from .models import SourceCode

class SourceCodeAdmin(admin.ModelAdmin):
    readonly_fields = ["location", "vector"]


admin.site.register(SourceCode, SourceCodeAdmin)
