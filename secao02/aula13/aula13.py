# Aula 13: Quantidade de caracteres

"""
Anotações:
* Função len: funciona com diversos tipos de dados menos com os numéricos.
"""

# Exemplo 1: demonstração
usuario = "Juliana"
quant = len(usuario)

print(usuario, quant)

# Exemplo 2: len + condições
user = input("Digite seu user: ")
quant2 = len(user)

if quant2 < 6:
    print("Você precisa digitar pelo menos 6 caracteres.")
else:
    print("Você foi cadastrado no sistema.")

# Exemplo 3: soma do numero de caracteres
str1 = input("Digite algo: ")
str2 = input("Digite outra coisa: ")

print(f"A quantidade total de caracteres digitados foi {len(str1) + len(str2)}.")
