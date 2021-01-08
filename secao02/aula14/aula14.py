# Aula 14: Documentação e funções built-in úteis

"""
Anotações:
* Built-in: https://docs.python.org/3/library/stdtypes.html
* Resolve o problema de float não ser considerado número:
            https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py
* Funções para str: isnumeric() -> checa se os caracteres são números
                    isdigit()   -> checa se os caracteres sao digitos
"""

# Exemplo 1: alternativa para não parar o programa com um erro
print("Exemplo 1:")
num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    p = 3.14

    print(num1 + num2)
else:
    print("Não foi possível realizar a conta!\n")

# Exemplo 2: try e except
print("Exemplo 2:")
num3 = input("Digite um número: ")
num4 = input("Digite outro número: ")

try:
    num3 = int(num3)
    num4 = int(num4)

    print(num3 + num4)
except:
    print("Não foi possível realizar a conta!")
