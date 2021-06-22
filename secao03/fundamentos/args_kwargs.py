"""
    Aula 2: Funções - def
    @author: Jgarconi
"""

def func_args(*args):
    """
    Recebe: número indefinido de argumentos
    Retorna: os argumentos em uma tupla
    """
    print(args)

def func_kwargs(*args, **kwargs):
    """
    Recebe: número indefinido de argumentos e argumentos nomeados
    Retorna: os argumentos em uma tupla e os argumentos nomeados separadamente
    """
    print(args)  # Acessa todos os argumentos não nomeados
    print(kwargs['nome'])  # Acessa os argumentos nomeados

def dados(**kwargs):
    """
    Usar .get é uma forma de extrair os argumentos nomeados evitando o fim
    da execução do programa por erros caso um dos argumentos não seja passado
    pelo usuário
    """
    nome = kwargs.get('nome')
    sobrenome = kwargs.get('sobrenome')
    idade = kwargs.get('idade')

    if nome and sobrenome and idade:
        print(f'{nome} {sobrenome}, {idade} anos')
    else:
        print("Dados inválidos")

lista = [1, 2, 3, 4, 5]

print('Exemplo 1:')
func_args(lista)  # A lista inteira entra como um único argumento da tupla
func_args(*lista, 'oi')  # Cada elemento da lista entra como argumento da tupla
print()

print('Exemplo 2:')
func_kwargs(*lista, 'oi', nome='Juliana')
print()

print('Exemplo 3:')
dados(nome='Juliana', sobrenome='Garçoni', idade=21)
dados(nome='Juliana', sobrenome='Garçoni')
