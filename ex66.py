soma = 0
cont = 0

while True:
    numero = int(input("Digite um Valor (999 para parar): "))
    if numero == 999:
        break
    cont = cont + 1
    soma = soma + numero

print(f"A soma dos {cont} números foi de {soma}")
