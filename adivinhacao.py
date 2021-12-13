import random

def jogar():
    range_do_jogo = [1, 25]
    numero_secreto = random.randrange(range_do_jogo[0], range_do_jogo[1])
    total_de_tentativas = int(((range_do_jogo[1] + 1) - range_do_jogo[0]) / 5)
    pontos = range_do_jogo[1] * 4
    pontos_perdidos = 0
    # print(numero_secreto)

    print("****************************************************")
    print("*********Bem vindo ao jogo de Adivinhação!!*********\n")
    print("Adivinhe o número secreto em apenas algumas rodadas!")
    print("****************************************************")

    print("Qual o nível de dificuldade desejado?")
    print("(1) Fácil;\n(2) Médio;\n(3) Difícil.\n")

    nivel_do_jogo = int(input("Defina o nível: "))

    while ((nivel_do_jogo != 1) or (nivel_do_jogo != 2) or (nivel_do_jogo != 3)):
        if (nivel_do_jogo == 1):
            total_de_tentativas = total_de_tentativas + round(total_de_tentativas / 2)
            print("A quantidade de rodadas foi definida em: {} rodadas!!!!".format(total_de_tentativas))
            break
        elif (nivel_do_jogo == 2):
            total_de_tentativas = total_de_tentativas
            print("A quantidade de rodadas foi definida em: {} rodadas!!!!".format(total_de_tentativas))
            break
        elif (nivel_do_jogo == 3):
            total_de_tentativas = total_de_tentativas - round(total_de_tentativas / 2)
            print("A quantidade de rodadas foi definida em: {} rodadas!!!!".format(total_de_tentativas))
            break
        else:
            print("Por favor informe um nível válido!\n")
            print("***********************************")
            print("Qual o nível de dificuldade desejado?")
            print("(1) Fácil;\n(2) Médio;\n(3) Difícil.\n")

            nivel_do_jogo = int(input("Defina o nível: "))
            continue

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        print("Sua pontuação atual:", pontos)
        chute_str = input("Digite seu palpite (um número entre {} e {}): \n".format(range_do_jogo[0], range_do_jogo[1] - 1))
        print("Você digitou: ", chute_str)
        chute_int = int(chute_str)

        if (chute_int < range_do_jogo[0]):
            print("Hmmm...", chute_int, "é um número menor que ", range_do_jogo[0])
            print("Digite um número entre {} e {}".format(range_do_jogo[0], range_do_jogo[1] - 1), "!")
            print("")
            continue
        elif (chute_int > range_do_jogo[1] - 1):
            print("Hmmm...", chute_int, "é um número maior que ", range_do_jogo[1] - 1)
            print("Digite um número entre {} e {}".format(range_do_jogo[0], range_do_jogo[1] - 1), "!")
            print("")
            continue

        acertou = chute_int == numero_secreto
        maior = chute_int > numero_secreto
        menor = chute_int < numero_secreto

        if (acertou):
            print("Você acertou, PARABÉNS!!!")
            print("Sua pontuação final foi:", pontos)
            break
        else:
            if (maior):
                if (pontos > 0):
                    pontos_perdidos = chute_int - numero_secreto
                    pontos = pontos - pontos_perdidos
                    print("Você errou, seu palpite foi maior que o número secreto.")
                else:
                    print("Você perdeu, pois seus pontos terminaram! ;(")
                    print("Sua pontuação:", pontos)
                    break
            elif (menor):
                if (pontos > 0):
                    pontos_perdidos = numero_secreto - chute_int
                    pontos = pontos - pontos_perdidos
                    print("Você errou, seu palpite foi menor que o número secreto.")
                else:
                    print("Você perdeu! Seus pontos terminaram! ;(")
                    print("Sua pontuação:", pontos)
                    break

    print("Fim de jogo!!!")

# Caso o arquivo adivinhacao.py seja executado diretamente, ele executa a função jogar()
# Caso o arquivo adivinhacao.py seja executado por outro arquivo, ele chama a função jogar()
if (__name__ == "__main__"):
    jogar()