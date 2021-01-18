"""
    Aula 22: For in - Estrutura de repetição em Python
    @author: Jgarconi

    Exemplos utilizando a estrutura de repetição for in
"""

# Exemplo 1: iterando strings com o for
texto = "Python"
print("Exemplo 1:")

# letra = "" : faz a leitura da str e exibe o resultado a cada iteração
for letra in texto:
    print(letra)

# Exemplo 2: uso da função range(start=0, stop, step=1)
print("\nExemplo 2:")

for i in range(5):
    print(i)
