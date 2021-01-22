"""
    Aula 28: Validador de CPF
    @author: Jgarconi

    Atividade: construir um validador de CPF utilizando os
               conhecimentos adquiridos durante o módulo
"""

while True:
    # Variáveis de apoio
    produtos_1 = []
    produtos_2 = []
    soma_1 = 0
    soma_2 = 0

    cpf = input("Digite seu CPF: ")

    # Não serão lidos símbolos ou CPFs com mais ou menos que 11 números
    if len(cpf) != 11 or not cpf.isdigit():
        print("Por favor, digite um CPF com 11 números.\n")
        continue
    elif cpf == str(cpf[0]) * len(cpf):
        print("Por favor, não digite sequências.\n")
        continue

    # Elimina os dois números verificadores digitados
    novo_cpf = cpf[:-2]

    # Gera números de 10 à 2 que serão multiplicados pelos dígitos do CPF
    for indice, multi in enumerate(range(10, 1, -1)):
        # Realiza a multiplicação com o número gerado e dígito correspondentes
        produtos_1.append(int(novo_cpf[indice]) * multi)
        # Soma todos resultados a cada iteração
        soma_1 += produtos_1[indice]

    # Calcula o primeiro dígito verificador
    validacao_1 = 11 - (soma_1 % 11)
    if validacao_1 > 9:
        digito_1 = 0
    else:
        digito_1 = validacao_1

    # Inclui o dígito 1 calculado ao novo CPF
    novo_cpf += str(digito_1)

    # Gera números de 11 à 2 que serão multiplicados pelos dígitos do CPF
    for indice, multi in enumerate(range(11, 1, -1)):
        # Realiza a multiplicação com o número gerado e dígito correspondentes
        produtos_2.append(int(novo_cpf[indice]) * multi)
        # Soma todos resultados a cada iteração
        soma_2 += produtos_2[indice]

    # Calcula o segundo dígito verificador
    validacao_2 = 11 - (soma_2 % 11)
    if validacao_2 > 9:
        digito_2 = 0
    else:
        digito_2 = validacao_2

    # Inclui o dígito 2 calculado ao novo CPF
    novo_cpf += str(digito_2)

    # Verifica se o CPF foi digitado corretamente
    if cpf == novo_cpf:
        print("CPF válido!\n")
    else:
        print(f"CPF inválido! Seu CPF deveria ser {novo_cpf}\n")
