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

def principal(funcao):  # Recebe uma funcao e
    return funcao()     # retorna a execução dela

saudacao = principal(helloworld)
print('Atividade 1:')
print(saudacao)
print()


def diz_ola(nome):
    return f'Olá {nome}'

def ola_mundo(nome, saudacao):
    return f'{saudacao} {nome}'

def func_princ(funcao, *args, **kwargs):  # Recebe uma função pra ser executada
    return funcao(*args, **kwargs)        # e os parametros dessa função

saudacao = func_princ(ola_mundo, 'juliana', 'Oi')
saudacao2 = func_princ(diz_ola, 'juliana')
print('Atividade 2:')
print(saudacao)
print(saudacao2)
