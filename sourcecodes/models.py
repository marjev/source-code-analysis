from django.contrib.postgres.fields import ArrayField
from django.db import models

import ast

from .utils import AstCustomVisitor

class SourceCode(models.Model):
    source = models.TextField()
    vector = ArrayField(models.IntegerField())

    def __str__(self):
        return self.source
    
    @property
    def ast_tree(self):
        return ast.parse(self.source)

    @property
    def ast_encoding(self):
        ast_visitor = AstCustomVisitor()
        ast_visitor.visit(self.ast_tree)
        return ast_visitor.encoding

    def save(self, *args, **kwargs):
        self.vector = self.ast_encoding
        super(SourceCode, self).save(*args, **kwargs)

