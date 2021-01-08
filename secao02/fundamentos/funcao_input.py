"""
    Aula 9: Entrada de dados do usuário
    @author: Jgarconi

    Exemplo de uso de entrada de dados do usuário em Python
    (função input())
"""

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
nascimento = 2020 - int(idade)

print(f"{nome} tem {idade} anos e nasceu em {nascimento}.")

