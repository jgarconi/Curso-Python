"""
    Aula 11: if, elif e esle + operadores relacionais
    @author: Jgarconi

    Exemplo de condicionais com operadores relacionais
    (<, <=, ==, !=, >=, >)
"""

nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))

# Limites de idade para pegar um empréstimo
idade_min = 18
idade_max = 30

if idade_min <= idade <= idade_max:
    print(f"{nome} pode pegar o empréstimo!")
else:
    print(f"{nome} NÃO pode pegar o empréstimo!")

