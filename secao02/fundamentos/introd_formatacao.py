"""
    Aula 7: Introdução à formatação de strings
    @author: Jgarconi

    Exemplos de formatações de strings em Python
"""

nome = "Juliana"
idade = 21
altura = 1.80
maioridade = idade > 18
peso = 112
imc = peso / altura**2

print("Sem formatação:",nome, "tem", idade, "anos e seu IMC é", imc)
print("F-string:", f"{nome} tem {idade} anos e seu IMC é {imc:.2f}")
print("Format:", "{} tem {} anos e seu IMC é {:2f}".format(nome, idade, imc))
print("Format com parametros numerados:", "O IMC de {0} é {2:.2f}, e ela tem {1} anos.".format(nome, idade, imc))
print("Format com parametros nomeados:", "O IMC de {n} é {c:.2f}, e ela tem {i} anos.".format(n=nome, i=idade, c=imc))
