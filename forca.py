import random


def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = solicita_chute()

        if (chute in palavra_secreta):
            marcador_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_ganhador()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    print("Fim de jogo!")


def imprime_mensagem_abertura():
    print("***********************************")
    print("****Bem vindo ao jogo de Forca!****")
    print("***********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")

    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    indice_random = random.randrange(0, len(palavras))
    palavra_secreta = palavras[indice_random].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def solicita_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def marcador_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    ________________         ")
    print("   /                \       ")
    print("  /                  \      ")
    print("//                    \/\  ")
    print("\|   XXXXX     XXXXX  | /   ")
    print(" |   XXXXX     XXXXX   |/     ")
    print(" |    XXX       XXX   |      ")
    print(" |                    |      ")
    print(" \__       XXX      __/     ")
    print("   |\      XXX     /|       ")
    print("   | |            | |        ")
    print("   |  I I I I I I I |        ")
    print("   |   I I I I I I  |        ")
    print("   \_              _/       ")
    print("     \_          _/         ")
    print("       \________/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


# Caso o arquivo forca.py seja executado diretamente, ele executa a função jogar()
# Caso o arquivo forca.py seja executado por outro arquivo, ele chama a função jogar()
if (__name__ == "__main__"):
    jogar()
