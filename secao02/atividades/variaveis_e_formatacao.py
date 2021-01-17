"""
    Aula 8: Desafio prático
    @author: Jgarconi

    Atividade: Criar variáveis para nome (str), idade (int),
               altura (float) e o peso (float) de uma pessoa
               Criar uma variável com o ano atual (int)
               Obter o ano de nascimento da pessoa (usar idade e o ano
               atual)
               Obter o IMC da pessoa com 2 casas decimais (usar peso e
               altura)
               Exibir um texto com todos os valores na tela
"""

# Atribuição das variáveis
nome = "Juliana"
idade = 21
altura = 1.80
peso = 112.00
ano = 2020
nascimento = ano - idade
imc = peso / altura ** 2

# Exibição do texto no formato indicado
print(f"{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.")
print(f"O IMC de {nome} é {imc:.2f}.")
print(f"{nome} nasceu em {nascimento}.")
