"""
    Aula 19: While - estrutura de repetição em Python
    @author: Jgarconi

    Atividade: Desenvolvimento de uma calculadora simples com 4 operações
               (+ - * /) utilizando o laço de repetição While
"""

while True:
    print()
    num_1 = input("Digite um número: ")
    num_2 = input("Digite outro número: ")
    operador = input("Digite um operador: ")

    if not num_1.isnumeric() or not num_2.isnumeric():
        print("Você precisa digitar um número ou sair!")
        sair = input("Você deseja sair? [s/n] ")
        if sair == "s":
            break
    else:
        num_1 = int(num_1)
        num_2 = int(num_2)
        if operador == "+":
            print(f"O resultado é {num_1 + num_2}")
        elif operador == "-":
            print(f"O resultado é {num_1 - num_2}")
        elif operador == "*":
            print(f"O resultado é {num_1 * num_2}")
        elif operador == "/":
            print(f"O resultado é {num_1 / num_2}")
        else:
            print(f"Operador inválido")

        sair = input("Você deseja sair? [s/n] ")
        if sair == "s":
            break
