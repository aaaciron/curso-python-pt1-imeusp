def computador_escolhe_jogada(n,m):
    cr = 1
    while cr != m:
        if (n - cr)%(m+1) == 0:
            return cr
        else:
            cr = cr+1
    return cr

def usuario_escolhe_jogada(n,m):
    jv = False
    while not jv:
        jr = int(input("Quantas peças você vai tirar? "))
        if jr > m or jr <= 0:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            jv = True
            return jr

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    vez_do_comp = False
    if n % (m+1) == 0:
        print()
        print("Você começa!")
    else:
        print()
        print("Computador começa!")
        vez_do_comp = True

    while n > 0:
        if vez_do_comp:
            cr = computador_escolhe_jogada(n,m)
            n = n - cr
            vez_do_comp = False
            if cr == 1:
                print()
                print("O computador tirou uma peça.")
                print("Agora restam",n,"peças no tabuleiro.")
            else:
                print()
                print("O computador tirou",cr,"peças.")
                print("Agora restam",n,"peças no tabuleiro.")
        else:
            jr = usuario_escolhe_jogada(n,m)
            n = n - jr
            vez_do_comp = True
            if jr == 1:
                print()
                print("Você tirou uma peça.")
                print("Agora restam",n,"peças no tabuleiro.")
            else:
                print()
                print("Você retirou",jr,"peças")
                print("Agora restam",n,"peças no tabuleiro.")
    print()
    print("Fim do jogo! O computador ganhou!")

def campeonato():
    print()
    print("**** Rodada 1 ****")
    partida()
    print()
    print("**** Rodada 2 ****")
    partida()
    print()
    print("**** Rodada 3 ****")
    partida()
    print()
    print("**** Final de campeonato! ****")
    print()
    print("Placar: Você 0 X 3 Computador")

print("Bem-vinddo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
g = int(input())
print()
if g == 1:
    print("Você escolheu uma partida isolada!")
    partida()
    print()
else:
    if g == 2:
        print("Você escolheu um campeonato!")
        campeonato()
