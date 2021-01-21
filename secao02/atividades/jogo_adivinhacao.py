"""
    Aula 23: Listas em Python
    @author: Jgarconi

    Atividade: Usar os conhecimentos de listas para desenvolver
               um joguinho de adivinhação
"""

palavra = "perfume"
digitado = []
chance = 3
print("Olá, você tem 3 chances para acertar a palavra secreta!")

while True:
    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Ei, isso não vale! Digite APENAS uma letra.")
        continue

    # Salva temporariamente a letra digitada em uma lista
    digitado.append(letra)

    # Verifica se a letra digitada está na palavra secreta
    if letra in palavra:
        # Se estiver, mantém a letra na lista
        print(f'Boa! A letra "{letra}" está na palavra secreta!')
        print(f"Você ainda tem {chance} chances!")
    else:
        # Caso contrário, a descarta e retira uma chance do jogador
        print(f'Poxa! A letra "{letra}" não está na palavra secreta.')
        digitado.pop()
        chance -= 1
        if chance == 0:
            print("Você perdeu! Reinicie o jogo.")
            break
        print(f"Você ainda tem {chance} chance(s)!")

    # Mostra ao usuário na posição das letras descobertas
    resultado = ""
    for letra_tmp in palavra:
        if letra_tmp in digitado:
            resultado += letra_tmp
        else:
            resultado += "*"

    print(resultado)

    if resultado == palavra:
        print(f'Parabéns, você ganhou! A palavra secreta era "{palavra}"!')
        break
    else:
        continue
