
def _visit(self, node):
    # [...] (código existente para Assign, If, Compare)
    
    elif isinstance(node, ast.BoolOp):
        # Ex: `A and B` ou `A or B`
        op = self._visit(node.op)
        values = [self._visit(v) for v in node.values]
        return f" {op} ".join(values)  # Retorna "A and B" ou "A or B"
    
    elif isinstance(node, ast.And):
        return "and"
    
    elif isinstance(node, ast.Or):
        return "or"