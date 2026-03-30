valor = int(input('Digite o valor que você deseja sacar: '))
index = 0
calculo = valor
cinquenta = 0
vinte = 0
dez = 0
um = 0
while index != valor:
    if  calculo - 50 >= 0:
        index = index + 50
        cinquenta = cinquenta + 1
        calculo = calculo - 50
    elif calculo - 20 >= 0:
        index = index + 20
        vinte = vinte + 1
        calculo = calculo - 20
    elif calculo - 10 >= 0:
        index = index + 10
        dez = dez + 1
        calculo = calculo - 10
    elif calculo - 1 >= 0:
        index = index + 1
        um = um + 1
        calculo = calculo - 1
if cinquenta > 0:
    print(f"{cinquenta} notas de 50")
if vinte > 0:
    print(f"{vinte} notas de 20")
if dez > 0:
    print(f"{dez} notas de 10")
if um > 0:
    print(f"{um} moedas de 1 real")