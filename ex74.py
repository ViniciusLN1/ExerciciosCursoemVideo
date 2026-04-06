from random import *

tupla = (randint(1,9), randint(1,9), randint(1,9), randint(1,9), randint(1,9))
maior = 0
menor = tupla[0]

for c in range(len(tupla)):
    for i in tupla:
        if i > maior:
            maior = i
        if i < menor:
            menor = i

print(tupla)
print(f'Maior: {maior}')
print(f'Menor: {menor}')