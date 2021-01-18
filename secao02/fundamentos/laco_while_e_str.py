"""
    Aula 21 While - Iteração de str com while em Python
    @author: Jgarconi

    Exemplo utilizando a estrutura de repetição while
"""

# Exemplo 1: manipulação de str com o uso do while
frase = "o rato roeu a roupa do rei de roma"
tam_frase = len(frase)
cont = 0
nova_frase = ""

entrada = input("Qual letra deseja colocar em maiúsculo? ")

while cont < tam_frase:                 # Enquanto a frase nao terminar
    letra = frase[cont]                 # faz a leitura da mesma
    if letra == entrada:                # Se a letra atual for a escolhida
        nova_frase += entrada.upper()   # deixa ela maiúscula
    else:                               # Caso contrário,
        nova_frase += letra             # copia a letra
    cont += 1                           # Passa para a próxima letra

print(nova_frase)
