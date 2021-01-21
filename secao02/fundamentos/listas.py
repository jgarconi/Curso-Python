"""
    Aula 23: Listas em Python
    @author: Jgarconi

    Exemplo de usos de listas em Python
"""

# Exemplo 1: operações e funções com listas

# Junta duas listas
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(f"Soma de listas: {l1} + {l2} = {l1 + l2}")

# Aumenta o tamanho da lista
l1.extend(l2)
print(f"Aumenta o tamanho da lista: {l1}")

# Adiciona os novos elementos ao fim da lista
# Nesse caso é o mesmo que l1 = [1, 2, 3, l2]
l1 = [1, 2, 3]
l1.append(l2)
print(f"Adiciona elementos ao fim da lista: {l1}")

# Adiciona um novo elemento na posição desejada
l2.insert(2, "olá")
print(f"Insere elementos na posição indicada: {l2}")

# Remove o último elemento da lista
l2.pop()
print(f"Elimina o último elemento da lista: {l2}")

# Remove os elementos selecionados da lista
l3 = [1, 2, 3, 4, 5, 6, 7]
del(l3[1:4])
print(f"Elimina os elementos escolhidos: {l3}")

# Identifica o maior e menor item da lista
l3 = [1, 2, 3, 4, 5, 6, 7]
print(f"Maior elemento da lista l3: {max(l3)}")
print(f"Menor elemento da lista l3: {min(l3)}")

# Lista elementos iteráveis
l4 = range(1, 6)
print(f"Não retorna a lista: {l4}")
l4 = list(range(1, 6))
print(f"Lista formada a partir das funções list e range: {l4}")
