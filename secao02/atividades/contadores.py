"""
    Aula 27: Desafio de contadores
    @author: Jgarconi

    Atividade: construir contadores usando as estruturas de repetição
"""
# Solução encontrada: exibe as respostas separadas
for crescente in range(0, 9):
    print(crescente)

for decrescente in range(10, 1, -1):
    print(decrescente)

print()

# Outra solução: exibe as respostas lado a lado
for c, d in enumerate(range(10, 1, -1)):
    print(c, d)
