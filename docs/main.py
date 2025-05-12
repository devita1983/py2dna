

## Estrutura
   _  __    _    _    _ ____   _    ____  _   _    _    _   _ 
  | |/ /   / \  | |  | | __ ) / \  |  _ \| \ | |  / \  | \ | |
  | ' /   / _ \ | |  | |  _ \/ _ \ | | | |  \| | / _ \ |  \| |
  | . \  / ___ \| |__| | |_) / ___ \| |_| | |\  |/ ___ \| |\  |
  |_|\_\/_/   \_\____/|____/_/   \_\____/|_| \_/_/   \_\_| \_|
  :: Codificando o Futuro com Biologia Quântica ::

##Estrutura do Projeto para Seguir

py2dna/                  # Pasta raiz
├── compiler/            # Código do compilador
│   ├── frontend/        # Análise léxica/sintática (Python → AST)
│   │   └── parser.py    # Implementa o parser usando `ast`
│   ├── backend/         # Tradução para DNA
│   │   └── dna_generator.py  # Gera sequências de DNA
│   └── utils/           # Ferramentas auxiliares
│       └── constants.py # Enzimas, sequências padrão
├── simulations/         # Testes e simulações
│   └── xor_example.ipynb  # Jupyter Notebook para XOR
├── protocols/           # Protocolos de laboratório
│   └── wetlab_protocol.md  # Como executar no mundo real
├── docs/                # Documentação
│   ├── grammar.md       # Especificação da linguagem
│   └── roadmap.md       # Cronograma de desenvolvimento
└── tests/               # Testes automatizados
    ├── test_parser.py
    └── test_dna_generator.py