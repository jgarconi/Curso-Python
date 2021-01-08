# Aula 11: if, elif e esle + operadores relacionais

"""
Anotações:
* Tipos de operadores: retornam um valor booleano
    == -> igual á
    >  -> maior que
    >= -> maior ou igual à
    <  -> menor que
    <= -> menor ou igual à
   != -> diferente de
"""

# Exemplo 1: demonstração
nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))

# Limites de idade para pegar um empréstimo
idade_min = 18
idade_max = 30

if idade_min <= idade <= idade_max:
    print(f"{nome} pode pegar o empréstimo!")
else:
    print(f"{nome} NÃO pode pegar o empréstimo!")
