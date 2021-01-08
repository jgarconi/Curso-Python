# Aula 10: if, elif e esle + booleans

"""
Anotações:
* Uma condição abaixo só é verificada se a condição acima for falsa.
"""

# Exemplo 1: demonstração
print("Exemplo 1:\n")
if False:
    print("É falso")
elif True:
    print("É verdadeiro")
    nome = input("Qual seu nome? ")
    print(f"Seu nome é {nome}")
elif False:
    print("Também é falso")
else:
    print("Todas são falsas")
