contador = 2
anterior = 0
atual = 1
proximo = 0

print("-----------------------")
print("Sequencia de Fibonacci")
print("-----------------------")
quantidade = int(input("Quantos termos você quer mostrar? "))

print("0 -> 1 -> ", end="")

while contador < quantidade:
    proximo = atual + anterior
    print(proximo, "->", end="")
    anterior = atual
    atual = proximo
    contador = contador + 1

print("Fim")