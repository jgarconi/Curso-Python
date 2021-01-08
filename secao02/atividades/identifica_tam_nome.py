"""
    Aula 16: Desafio prático
    @author: Jgarconi

    Atividade 3: Faça um programa que peça o primeiro nome do usuário. 
                 Se o nome tiver 4 letras ou menos escreva "Seu nome é 
                 curto", se tiver entre 5 e 6 letras, escreva "Seu nome 
                 é normal"; maior que 6 escreva "Seu nome é grande". 
"""

nome = input("Digite seu nome: ")
quant = len(nome)

if quant <= 4:
    print("Seu nome é curto!")
elif quant <= 6:
    print("Seu nome é normal!")
else:
    print("Seu nome é grande!")

