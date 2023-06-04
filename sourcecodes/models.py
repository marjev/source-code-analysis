from django.db import models

class SourceCode(models.Model):
    source = models.TextField()

    def __str__(self):
        return self.source

