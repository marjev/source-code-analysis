from django.db import models

from source_codes.models import SourceCode


class UserRequirement(models.Model):
    edges = models.JSONField("Edges", blank=True, null=True)
    nodes = models.JSONField("Nodes")
