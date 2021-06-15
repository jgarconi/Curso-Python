"""
    Aula 1: Funções - def
    @author: Jgarconi

    Atividades:
    1 - helloworld(saudacao, nome) - Criar uma função que exibe uma saudação
        com os parâmetros "saudação e nome"

    2 - soma(n1, n2, n3) - Criar uma função que receba 3 números e retorne a
        soma entre eles

    3 - aumento_percentual(valor, aumento) - Crie uma função que receba 2
        números, um valor e um percentual, e retorne a soma desse valor com
        seu aumento percentual

    4 - fb(n) - Crie uma função que retorne Fizz caso o número seja divisível
        por 3, Buzz caso seja divisível por 5, FizzBuzz caso seja divisível por
        5 e 3, e que retorne o valor caso contrário.
"""

def helloworld(saudacao='Olá', nome='usuário!'):
    return f'{saudacao} {nome}'
print('Atividade 1:')
frase = helloworld('Hello', 'Juliana!')
print(frase)
frase = helloworld('Oi', 'Ju!')
print(frase)
frase = helloworld()
print(frase)
print()


def soma(n1, n2, n3):
    return n1 + n2 + n3
print('Atividade 2:')
print(soma(1, 2, 3))
print(soma(10, 44, 85))
print(soma(1, 10, 100))
print()


def aumento_percentual(valor, aumento):
    return valor + (valor*(aumento/100))
print('Atividade 3:')
print(aumento_percentual(40, 1))
print(aumento_percentual(40, 10))
print(aumento_percentual(40, 100))
print()


def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'FizzBuzz, {n} é divisível por 3 e por 5'
    if n % 3 == 0:
        return f'Fizz, {n} é divisível por 3'
    if n % 5 == 0:
        return f'Buzz, {n} é divisível por 5'
    return n
print('Atividade 4:')
print(fb(75))
print(fb(55))
print(fb(9))
print(fb(11))
