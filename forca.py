def jogar():
    print("***********************************")
    print("****Bem vindo ao jogo de Forca!****")
    print("***********************************")

    palavra_secreta = "banana"
    letras_acertada = ["_", "_", "_", "_", "_", "_",]
    enforcou = False
    acertou = False

    print(letras_acertada)

    while (not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertada[index] = letra
            index += 1

        print(letras_acertada)

    print("Fim de jogo!")


# Caso o arquivo forca.py seja executado diretamente, ele executa a função jogar()
# Caso o arquivo forca.py seja executado por outro arquivo, ele chama a função jogar()
if (__name__ == "__main__"):
    jogar()
