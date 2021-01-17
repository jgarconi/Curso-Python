"""
    Aula 12: if, elif e esle + operadores lógicos
    @author: Jgarconi

    Exemplo de condicionais com operadores lógicos
    (and, or, not, in, not in)
"""

usuario = input("Nome do usuário: ")
senha = input("Senha do usuário: ")

usuario_bd = "juliana"
senha_bd = "060799"

if usuario_bd == usuario and senha_bd == senha:
    print(f"Bem vindo(a), {usuario_bd}!")
else:
    print("Usuário ou senha incorretos, tente novamente!")
