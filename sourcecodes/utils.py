import ast

is_python_type = lambda attribute : type(getattr(ast, attribute)) == type
is_ast_node = lambda attribute : issubclass(getattr(ast, attribute), ast.AST)


class AstCustomVisitor(ast.NodeVisitor):
    PYTHON_AST_ATTRIBUTES = ast.__dir__()
    PYTHON_AST_NODES = [
        attribute for attribute in PYTHON_AST_ATTRIBUTES
        if is_python_type(attribute) and is_ast_node(attribute)
    ]

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.ast_nodes_count = { node : 0 for node in self.PYTHON_AST_NODES }

    @property
    def encoding(self):
        return list(self.ast_nodes_count.values())
    
    def generic_visit(self, node):
        self.ast_nodes_count[node.__class__.__name__] = 1
        return super().generic_visit(node)
