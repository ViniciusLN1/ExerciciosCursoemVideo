contador = 0
soma = 0

numero = int(input("Digite um número [999 para parar]: "))
soma = numero
while numero != 999:
    numero = 0
    numero = int(input("Digite um número [999 para parar]: "))
    soma = soma + numero
    contador = contador + 1
soma = soma - 999
print(f"Você digitou {contador} números e a soma deles vai ser {soma}")