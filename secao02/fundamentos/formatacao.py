"""
    Aula 17: Formatando valores em Python
    @author: Jgarconi

    Exemplos de formatações de valores usando modificadores em Python
"""

# Exemplo 1: preencher números na direção desejada
num_1 = 1
print(f"{num_1:0>9}")  # Esquerda
print(f"{num_1:0<9}")  # Direita
print(f"{num_1:0^9}")  # Centro

