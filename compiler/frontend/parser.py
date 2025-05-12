
import ast

class Py2DNA_Parser:
    def __init__(self):
        self.dna_vars = {}  # Armazena variáveis do tipo DNA

    def parse(self, code: str) -> str:
        tree = ast.parse(code)
        return self._visit(tree)

    def _visit(self, node):
        if isinstance(node, ast.Assign):
            # Ex: `input_A = DNA("ACG")`
            var_name = node.targets[0].id
            dna_seq = node.value.args[0].value
            self.dna_vars[var_name] = dna_seq
            return f"DEFINED {var_name} = {dna_seq}"

        elif isinstance(node, ast.If):
            # Ex: `if A != B: output = DNA("CTAA")`
            condition = self._visit(node.test)
            then_block = [self._visit(n) for n in node.body]
            else_block = [self._visit(n) for n in node.orelse]
            return f"IF {condition} THEN {then_block} ELSE {else_block}"

        elif isinstance(node, ast.Compare):
            # Ex: `A != B`
            left = self._visit(node.left)
            right = self._visit(node.comparators[0])
            op = self._visit(node.ops[0])
            return f"{left} {op} {right}"

        elif isinstance(node, ast.NotEq):
            return "!="

        # [...] Adicione mais regras para `==`, `and`, etc.
        else:
            raise ValueError(f"Unsupported node: {type(node)}")