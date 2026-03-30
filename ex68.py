from random import *

print("Vamos jogar  =-=-=PAR OU IMPAR=-=-=")
contador = 0
while True:
    botescolha = randint(1, 10)

    valor = int(input("Digite um valor: "))
    jogadorescolha = str(input("PAR ou IMPAR [ P / I ]: ")).strip().upper()


    if (botescolha + valor) % 2 == 0:
        parouimpar = "P"
    else:
        parouimpar = "I"


    if jogadorescolha == parouimpar:
        contador = contador + 1
        print(f"Você jogou {valor} e o computador jogou {botescolha}, total de {valor + botescolha} deu {parouimpar} ")
        print(f"Você venceu {contador} vezes! parabens")

    else:
        print("Você perdeu!")
        print(f"Você jogou {valor} e o computador jogou {botescolha}, total de {valor + botescolha} deu {parouimpar} ")
        print(f"Você ganhou {contador} vezes! ")
        break
