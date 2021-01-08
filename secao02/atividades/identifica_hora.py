"""
    Aula 16: Desafio prático
    @author: Jgarconi

    Atividade 2: Faça um programa que pergunte a hora ao usuário e, 
                 baseando-se no horário descrito, exiba a saudação  
                 apropriada (Bom dia, boa tarde ou boa noite)
"""

hora = input("Por favor, digite um horário entre 0 e 23: ")

if hora.isdigit():
    hora = int(hora)
    if 0 <= hora <= 11:
        print("Bom dia!\n")
    elif 12 <= hora <= 17:
        print("Boa tarde!\n")
    elif 18 <= hora <= 23:
        print("Boa noite!\n")
    else:
        print("O horário deve estar entre 0 e 23.\n")
else:
    print("Por favor, digite um horário válido.\n")


