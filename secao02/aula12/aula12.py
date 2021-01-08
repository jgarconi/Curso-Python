# Aula 12: if, elif e esle + operadores lógicos

"""
Anotações:
* Tipos de operadores: and, or, not, in, not in
"""

# Exemplo 1: demonstração
usuario = input("Nome do usuário: ")
senha = input("Senha do usuário: ")

usuario_bd = "juliana"
senha_bd = "060799"

if usuario_bd == usuario and senha_bd == senha:
    print("Bem vinda, Juliana!")
else:
    print("Usuário ou senha incorretos, tente novamente!")
