"""
    Aula 13: Quantidade de carácteres (função len())
    @author: Jgarconi

    Exemplos de uso da função len() para identificar a quantidade
    de carácteres de uma str
"""

# Exemplo 1: Demonstração simples
print("Exemplo 1:")

usuario = "Juliana"
quant = len(usuario)

print(usuario, quant)

# Exemplo 2: len() + condições
print("Exemplo 2:")

user = input("Digite seu user: ")
quant2 = len(user)

if quant2 < 6:
    print("Você precisa digitar pelo menos 6 caracteres.")
else:
    print("Você foi cadastrado no sistema.")

# Exemplo 3: Soma do numero de caracteres
str1 = input("Digite algo: ")
str2 = input("Digite outra coisa: ")

print(f"A quantidade total de caracteres digitados foi {len(str1) + len(str2)}.")
