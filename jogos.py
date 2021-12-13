import forca
import adivinhacao

def escolha_de_jogo():
    print("***********************************")
    print("********Escolha o seu jogo!********")
    print("***********************************")

    print("(1) Forca\n(2) Adivinhação")

    jogo = int(input("Qual o jogo desejado?\n"))

    if (jogo == 1):
        print("Jogando Forca\n")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhação\n")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolha_de_jogo()