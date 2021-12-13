def jogar():
    print("***********************************")
    print("****Bem vindo ao jogo de Forca!****")
    print("***********************************")

    palavra_secreta = "banana".upper()
    letras_acertada = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertada)

    while (not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertada[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertada
        print(letras_acertada)

    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim de jogo!")



# Caso o arquivo forca.py seja executado diretamente, ele executa a função jogar()
# Caso o arquivo forca.py seja executado por outro arquivo, ele chama a função jogar()
if (__name__ == "__main__"):
    jogar()
