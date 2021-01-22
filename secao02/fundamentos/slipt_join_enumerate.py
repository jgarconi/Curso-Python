"""
    Aula 25: Funções split, join e enumerate em Python
    @author: Jgarconi

    Exemplos de uso das funções split, join e enumerate em Python
"""

# Exemplo 1: função split - separa uma str e a transforma em lista
print("Exemplo 1:")
frase_1 = "Juliana é brasileira, Juliana tem 21 anos."
lista_1 = frase_1.split(" ")    # Separa a str a cada espaço
lista_2 = frase_1.split(",")    # Separa a str a cada vírgula

print(lista_1)
print(lista_2, "\n")

# Exemplo 2: contagem de palavras com o uso das funções split e count
print("Exemplo 2:")

palavra_recorrente = ""
maximo = 0
# Verifica quantas vezes a palavra atual apareceu
for palavra in lista_1:
    quantidade = lista_1.count(palavra)
    # Se ela apareceu mais vezes que o máximo estabelecido
    if quantidade > maximo:
        # Ela é a nova palavra mais recorrente
        maximo = quantidade
        palavra_recorrente = palavra
print(f'A palavra que apareceu mais vezes foi "{palavra_recorrente}". '
      f'Ela apareceu {maximo} vezes.\n')

# Exemplo 3: função join - junta uma lista e a transforma em str
print("Exemplo 3:")

# Transforma a str em elementos de uma lista
frase_2 = "O Brasil é penta."
lista_3 = frase_2.split(" ")
print(lista_3)

# Transforma a lista em str
frase_3 = "-".join(lista_3)
print(frase_3, "\n")

# Exemplo 4: função enumerate - enumera os elementos da lista
print("Exemplo 4:")
lista_4 = ["João", "Maria", "José"]

# Ocorre o mesmo se existissem outras listas dentro da lista_4,
# o "indice" armazena a primeira coluna e o "nome" a segunda
for indice, nome in enumerate(lista_4):
    print(indice, nome)
