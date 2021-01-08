# Aula 15: atividades propostas
"""
TODO: escrever os comentários como nas outras aulas
"""

# Exercícío 1
print("Exercícío 1:")
num = input("Digite um número inteiro: ")

try:
    num = int(num)
    if num % 2 == 0:
        print("Esse número é par!\n")
    else:
        print("Esse número é ímpar!\n")
except:
    print("Isso não é um número inteiro. Tente novamente!\n")

# Exercícío 2
print("Exercícío 2:")
hora = input("Por favor, digite as horas: ")

try:
    hora = int(hora)

    if 0 <= hora <= 11:
        print("Bom dia!\n")
    elif 12 <= hora <= 17:
        print("Boa tarde!\n")
    elif 18 <= hora <= 23:
        print("Boa noite!\n")
    else:
        print("O horário deve estar entre 0 e 23.\n")
except:
    print("Por favor, digite um horário válido.\n")

# Exercícío 3
print("Exercícío 3:")
nome = input("Digite seu nome: ")
quant = len(nome)

if quant <= 4:
    print("Seu nome é curto!")
elif quant <= 6:
    print("Seu nome é normal!")
else:
    print("Seu nome é grande!")
