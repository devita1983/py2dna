def generate(self, parsed_code: str) -> str:
    # [...] (código existente para !=, ==)
    
    if " and " in parsed_code:
        left, right = parsed_code.split(" and ")
        self.output.append(f"SEQUENCE: {self.dna_vars[left]} + {self.dna_vars[right]}")
        self.output.append(f"ENZYME: {ENZYMES['DNA_ligase']}")
        self.output.append("OUTPUT: TAGG")  # Exemplo: AND bem-sucedido
    
    elif " or " in parsed_code:
        left, right = parsed_code.split(" or ")
        self.output.append(f"SEQUENCE: {self.dna_vars[left]} | {self.dna_vars[right]}")
        self.output.append(f"ENZYME: {ENZYMES['Polymerase']}")
        self.output.append("OUTPUT: CTAA")  # Exemplo: OR bem-sucedido