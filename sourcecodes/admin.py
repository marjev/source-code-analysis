from django.contrib import admin

from .models import SourceCode

class SourceCodeAdmin(admin.ModelAdmin):
    readonly_fields = ["vector"]


admin.site.register(SourceCode, SourceCodeAdmin)
