# Aula 9: Entrada de dados do usuário

"""
Anotações:
* Função input(): o dado enviado pelo usuário sempre é interpretado como str.
"""

# Exemplo 1: demonstração simples do uso da função input
print("Exemplo 1:")
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
nascimento = 2020 - int(idade)

print(f"{nome} tem {idade} anos e nasceu em {nascimento}.\n")

# Exemplo 2: calculadora de soma
print("Exemplo 2:")
num_1 = input("Digite um número: ")
num_2 = input("Digite outro número: ")
result = int(num_1) + int(num_2)

print(f"A soma de {num_1} com {num_2} é igual à {result}.")
