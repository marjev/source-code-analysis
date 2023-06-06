import ast

from django.contrib.postgres.fields import ArrayField
from django.db import models

from .utils import AstCustomVisitor, PYTHON_AST_NODES
from selforganizingmap.self_organizing_map import SomGenerator

class SourceCode(models.Model):
    location = ArrayField(models.IntegerField(), size=2)
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

    def get_som_location(self, ast_nodes):
        print(len(self.ast_encoding))
        return SomGenerator(ast_nodes).som.winner(self.ast_encoding)

    def save(self, *args, **kwargs):
        self.location = self.get_som_location(PYTHON_AST_NODES)
        self.vector = self.ast_encoding
        super(SourceCode, self).save(*args, **kwargs)

