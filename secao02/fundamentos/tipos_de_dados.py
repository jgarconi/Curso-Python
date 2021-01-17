"""
    Aula 4: Tipos de dados "primitivos"
    @author: Jgarconi

    Exemplos de tipos de dados em Pyhton
"""

# Exemplo 1: Identificar a classe/tipo de um dado
print("Exemplo 1:")
print('Juliana', type('Juliana'))
print(1999, type(1999))
print(19.99, type(19.99))
print(True, type(True))
print('j' == 'J', type('j' == 'J'), "\n")

# Exemplo 2: Str vaiza = falso, qualquer outra coisa = true
print("Exemplo 2:")
print(bool(''))
print('Juliana', type('Juliana'), bool('Juliana'), "\n")

# Exemplo 3: Converter um tipo de dado em outro -> typecasting
print("Exemplo 3:")
print('10', type('10'), type(int('10')), "\n")
