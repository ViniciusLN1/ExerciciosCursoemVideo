#aula16

lanche = ("Hamburguer", "Suco", "pizza", "pudim", "batata frita")
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-1])
print(lanche[1:3])
print(lanche[0:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])

for comida in lanche:
    print(f"Eu vou comer {comida}")

print (f"a tupla lanche tem {len(lanche)} lanches")

for cont in range(0, len(lanche)):
    print(lanche[cont])

for pos, comida in enumerate(lanche):
    print(f"eu vou comer {comida} na posicao {pos}")

print(sorted(lanche))

a = (2, 5, 4)

b = (5, 8, 1, 2)

print(a, b)

c = a + b

print(c)

print(len(c))

print(c.count(5))
print(c.count(9))
print(c.count(4))

print(c.index(8))

print(c.index(5))
print(c.index(5, 2))

pessoa = ("Gustavo", 39, "M", 99.88) #recebe elementos de varios tipos
print(pessoa)
#del(pessoa)
print(pessoa)#da erro por causa da delecao da tupla pessoa


extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input("Digite um numero de 0 a 20: "))

while numero < 0 or numero > 20:
    numero = int(input("Tente novamente, digite um numero de 0 a 20: "))

print(f"Voce digitou o numero {extenso[numero]}")


