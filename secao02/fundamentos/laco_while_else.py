"""
    Aula 20: While/Else - Repetição com acumuladores em Python
    @author: Jgarconi

    Exemplos utilizando a estrutura de repetição while
"""

# Exemplo 1: diferença entre contador e acumulador
print("Exemplo 1:")
contador = 0
acumulador = 0

while contador <= 10:
    print(contador, acumulador)

    acumulador += contador
    contador += 1

print("Fim do laço\n")

# Exemplo 2: uso do while/else
print("Exemplo 2:")
contador = 0
acumulador = 0

# É executado enquanto a condição for verdadeira
while contador <= 10:
    print(contador, acumulador)

    if contador > 5:  # Interrompe o laço quando a condição for satisfeita
        break

    acumulador += contador
    contador += 1
# É executado quando a condição passa a ser falsa
else:
    print("Cheguei no else")  # Não roda pois a condição ainda é verdadeira

print("Saí do laço")
