"""
    Aula 2: Funções - def
    @author: Jgarconi

"""
def func_args(*args):  # Usar para número indefinido de argumentos na entrada
    print(args)

lista = [1, 2, 3, 4, 5]
func_args(lista)  # A lista inteira entra como um único argumento da tupla args
func_args(*lista, 'oi')  # Cada argumento da lista entra como um argumento da

def func_kwargs(*args, **kwargs):
    print(args)
    print(kwargs['nome'])  # Acessa os argumentos nomeados

func_kwargs(*lista, nome='Juliana')

def dados(**kwargs):
    """
    Forma de extrair os argumentos nomeados evitando o fim da execução do
    programa por erros caso um dos argumentos não seja passado pelo usuário
    """
    nome = kwargs.get('nome')
    sobrenome = kwargs.get('sobrenome')
    idade = kwargs.get('idade')

    if nome and sobrenome and idade:
        print(f'{nome} {sobrenome}, {idade} anos')
    else:
        print("Dados inválidos")

dados(nome='Juliana', sobrenome='Garçoni', idade=21)
