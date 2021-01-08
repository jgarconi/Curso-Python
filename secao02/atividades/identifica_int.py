"""
    Aula 16: Desafio prático
    @author: Jgarconi

    Atividade 1: Faça um programa que peça ao usuário para digitar 
                 um número inteiro, informe se este número é par ou 
                 ímpar. Caso o usuário não digite um número inteiro, 
                 informe que não é um número inteiro
"""

num = input("Digite um número inteiro: ")

try:
    num = int(num)
    if num % 2 == 0:
        print(f"{num} é par!")
    else:
        print(f"{num} é ímpar!")
except:
    print("{num} não é um número inteiro. Tente novamente.")

