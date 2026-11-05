tabuleiro = [
    "X", "X", "X",
    "0", " ", "0",
    "0", "X", "0"
]

for i in range(0, 9, 3):
    print(tabuleiro[i], "|", tabuleiro[i+1], "|", tabuleiro[i+2])
    if i < 6:
        print("--|---|--")


posicao = int(input("\nEscolha uma posição (0 a 8): "))

if tabuleiro[posicao] == " ":
    
    jogador = input("Digite X ou 0: ")
    
    tabuleiro[posicao] = jogador

    print("\nTabuleiro atualizado:\n")

    for i in range(0, 9, 3):
        print(tabuleiro[i], "|", tabuleiro[i+1], "|", tabuleiro[i+2])
        if i < 6:
            print("--|---|--")

else:
    print("Casa ocupada!")