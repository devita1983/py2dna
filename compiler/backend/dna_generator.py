
from compiler.utils.constants import ENZYMES

class DNA_Generator:
    def __init__(self):
        self.output = []

    def generate(self, parsed_code: str) -> str:
        if "!=" in parsed_code:
            self.output.append("SEQUENCE: ACG + CAT")
            self.output.append(f"ENZYME: {ENZYMES['EcoRI']}")
            self.output.append("OUTPUT: CTAA")
        elif "==" in parsed_code:
            self.output.append("SEQUENCE: ACG + TGC")
            self.output.append(f"ENZYME: {ENZYMES['DNA_ligase']}")
            self.output.append("OUTPUT: TAGG")
        return "\n".join(self.output)