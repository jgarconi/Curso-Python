"""
    Aula 19: While - estrutura de repetição em Python
    @author: Jgarconi

    Exemplos utilizando a estrutura de repetição while
"""

# Exemplo 1: realiza ações enquanto a condição for verdadeira
print("Exemplo 1:")
x = 0

while x < 5:
    print(x)
    x = x + 1
print("Terminou!")

# Exemplo 2: loop dentro de loop
print("Exemplo 2:")
colunas = 0

# A cada loop de "colunas"
while colunas < 5:
    linhas = 0

    # Acontecem 5 loops de "linhas"
    while linhas < 5:
        print(f"({colunas},{linhas})")
        linhas += 1

    colunas += 1
