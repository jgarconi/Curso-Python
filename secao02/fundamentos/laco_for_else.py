"""
    Aula 24: Laço for/else em Python
    @author: Jgarconi

    Exemplo de uso do laço for/else em Python
"""

lista = ['Xuliana', 'Marlene', 'Carlos']

for nome in lista:
    # Checa a primeira letra maiúscula ou minúscula
    if nome.lower().startswith('j'):
        print("Existem nomes iniciados com J na lista.")
        break
else:
    print("Não existem nomes iniciados com J na lista.")
