"""
    Aula 1: Funções - def
    @author: Jgarconi

    Atividades:
    1 - Criar uma função que recebe outra como parâmetro e a execute

    2 - Criar uma função que recebe outras duas como parâmetro e as execute.
        Essas funções devem ter quantidades diferentes de parâmetros.

"""

def helloworld():
    return 'Hello World!'

def principal(funcao):
    """
    Recebe: uma função
    Retorna: a execução da função recebida
    """
    return funcao()

saudacao = principal(helloworld)
print('Atividade 1:')
print(saudacao)
print()

def diz_ola(nome):
    return f'Olá {nome}'

def ola_mundo(nome, saudacao1):
    return f'{saudacao1} {nome}'

def func_princ(funcao, *args, **kwargs):
    """
    Recebe: uma função e seus argumentos (quantidade indefinida)
    Retorna: a execução da função recebida usando os argumentos dados
    """
    return funcao(*args, **kwargs)

saudacao2 = func_princ(ola_mundo, 'Juliana', 'Hello')
saudacao3 = func_princ(diz_ola, 'Juliana')
print('Atividade 2:')
print(saudacao2)
print(saudacao3)
