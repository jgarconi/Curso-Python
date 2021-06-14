"""
    Aula 26: Desempacotamento de listas em Python
    @author: Jgarconi

    Exemplo de como desempacotar listas em Python
"""

# Exemplo 1: desempacotamento de listas
print("Exemplo 1:")
lista = ["João", "Maria", "José", 1, 2, 3, 4, 5, 6]
elem_1, elem_2, *nova_lista, ultimo_elemento = lista

print(elem_1, elem_2, nova_lista, ultimo_elemento, "\n")

# Exemplo 2: troca de valores de variáveis
print("Exemplo 2:")
x = 21
y = "Juliana"
x, y = y, x

print(f"Novo x = {x} e novo y = {y}")
