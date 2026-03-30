from random import randint
tentativas = 0
numero_computador = randint(1, 10)
print('-=-' * 17)
print('Tente adivinhar qual numero eu estou pensando! De um a 10!!')
print('-=-' * 17)
numero_jogador = int(input('Qual numero eu estou pensando?: '))
while numero_jogador != numero_computador:
    numero_jogador = int(input("Número errado digite novamnte: "))
    tentativas = tentativas + 1
if numero_jogador == numero_computador:
    print(f"Você acertou! Foram {tentativas} tentativas!")
