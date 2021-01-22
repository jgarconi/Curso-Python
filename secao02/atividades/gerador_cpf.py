"""
    Aula 29: Gerador de CPF
    @author: Jgarconi

    Atividade: construir um gerador de CPF utilizando o
               exercício do validador de CPF
"""

from random import randint

# Gera o número aleatório que será validado como CPF
cpf = str(randint(100000000, 999999999))

# Variáveis de apoio
produtos_1 = []
produtos_2 = []
soma_1 = 0
soma_2 = 0

# Gera números de 10 à 2 que serão multiplicados pelos dígitos do CPF
for indice, multi in enumerate(range(10, 1, -1)):
    # Realiza a multiplicação com o número gerado e dígito correspondentes
    produtos_1.append(int(cpf[indice]) * multi)
    # Soma todos resultados a cada iteração
    soma_1 += produtos_1[indice]

# Calcula o primeiro dígito verificador
validacao_1 = 11 - (soma_1 % 11)
if validacao_1 > 9:
    digito_1 = 0
else:
    digito_1 = validacao_1

# Inclui o dígito 1 calculado ao novo CPF
cpf += str(digito_1)

# Gera números de 11 à 2 que serão multiplicados pelos dígitos do CPF
for indice, multi in enumerate(range(11, 1, -1)):
    # Realiza a multiplicação com o número gerado e dígito correspondentes
    produtos_2.append(int(cpf[indice]) * multi)
    # Soma todos resultados a cada iteração
    soma_2 += produtos_2[indice]

# Calcula o segundo dígito verificador
validacao_2 = 11 - (soma_2 % 11)
if validacao_2 > 9:
    digito_2 = 0
else:
    digito_2 = validacao_2

# Inclui o dígito 2 calculado ao novo CPF
cpf += str(digito_2)

# Verifica se o CPF foi digitado corretamente
print(f"O CPF gerado foi: {cpf}")
