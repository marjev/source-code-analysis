from django.db import models

from requirements.models import UserRequirement
from source_codes.models import SourceCode


class TeachingElement(models.Model):
    code = models.ForeignKey(SourceCode, blank=True, null=True, on_delete=models.SET_NULL)
    requirements = models.ForeignKey(UserRequirement, on_delete=models.CASCADE)

    @property
    def type(self):
        return 'exercise' if self.code and self.requirements else 'mission'
