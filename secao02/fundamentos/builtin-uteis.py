"""
    Aula 14: Funções built-in úteis
    @author: Jgarconi

    Exemplos de built-ins úteis para evitar que o programa seja
    interrompido por erros
"""

# Exemplo 1: Uso de string methodes
print("Exemplo 1:")
num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

# Verifia se o que foi digitado foram números:
if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(f"A soma deu {num1 + num2}")
# Caso não sejam, indica um erro:
else:
    print("Não foi possível realizar a conta.\n")

# Exemplo 2: Uso de try e except
print("Exemplo 2:")
num3 = input("Digite um número: ")
num4 = input("Digite outro número: ")

# Tenta essa operação:
try:
    num3 = int(num3)
    num4 = int(num4)
    print(num3 + num4)
# Caso não funcione, indica um erro:
except:
    print("Não foi possível realizar a conta!")

