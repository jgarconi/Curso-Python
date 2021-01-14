"""
    Aula 18: Índices e fatiamento de str em Python
    @author: Jgarconi

    Exemplos de manipulação de str em Python
"""

# Exemplo 1: acesso à um índice específico em uma str
nome = "Juliana"
print("Exemplo 1:")
print(nome[3])   # Índice positivo
print(nome[-4])  # Índice negativo

# Exemplo 2: fatiamento
print("Exemplo 2:")
print(nome[2:5])

# Exemplo 3: [início:fim:passo]
print(nome[::2])    # Não definir um início e um fim no fatiamento
print(nome[0:7:2])  # é interpretado como ínicio e fim da str
