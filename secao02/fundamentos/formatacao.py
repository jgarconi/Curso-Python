"""
    Aula 17: Formatando valores em Python
    @author: Jgarconi

    Exemplos de formatações de valores usando modificadores em Python
"""

# Exemplo 1: preencher números (ou texto) na direção desejada
num_1 = 1
print("Exemplo 1:")
print(f"{num_1:0>9}")    # Esquerda
print(f"{num_1:0<9}")    # Direita
print(f"{num_1:0^9}\n")  # Centro

# Exemplo 2: formatação de str
print("Exemplo 2:")
nome = "JuLiAnA GaRçOnI"
print("Justifica à esquerda: ", nome.ljust(20, "#"))
print("Justifica à direita: ", nome.rjust(20, "#"))
print("Tudo maiúsculo: ", nome.upper())
print("Tudo minúsculo: ", nome.lower())
print("Primeiras letras maiúsculas: ", nome.title())
