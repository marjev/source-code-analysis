from django.db import models

from sourcecodes.models import SourceCode


class UserRequirement(models.Model):
    edges = models.JSONField("Edges", blank=True)
    nodes = models.JSONField("Nodes")
    source_code = models.ForeignKey(SourceCode, on_delete=models.CASCADE)
