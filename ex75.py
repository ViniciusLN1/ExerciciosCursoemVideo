tupla = ((int(input('Digite um numero: '))), (int(input('Digite um numero: '))), (int(input('Digite um numero: '))), (int(input('Digite um numero: '))))
print(tupla)

print(f'O numero nove aparece {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O numero tres aparece pela primeira vez na posicao {tupla.index(3)}')
else:
    print('O numero 3 nao aparece na tupla')
for i in tupla:
    conta = i % 2
    if conta == 0:
        print(f'O numero {i} eh par')
    else:
        print(f'O numero {i} eh impar')
