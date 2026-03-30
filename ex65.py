continuar = 'S'
soma = 0
contador = 0
maior = 0
menor = 0
numero = int(input("Digite um número: "))
contador = contador + 1
soma = soma + numero
maior = numero
menor = numero

escolha = str(input("Deseja continuar? [S/N] ")).upper().strip()
if escolha == 'S':
    while continuar == 'S':
        numero = int(input("Digite um número: "))
        contador = contador + 1
        soma = soma + numero
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
        continuar = str(input("Deseja continuar? [S/N] ")).upper().strip()

media = soma / contador
print(f"Você digitou {contador} números e a média foi {media}")
print(f"O maior valor foi {maior} e o menor valor foi {menor}")