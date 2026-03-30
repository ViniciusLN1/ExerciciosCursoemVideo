print("Gerador de PA!")
print("-=" * 7, "|")
termo = int(input("Primeiro termo: "))
pa = int(input("Razão PA: "))
Ultimonumero = termo
contador = 1
while contador <= 10:
    print("{} -> ".format(Ultimonumero), end="")
    Ultimonumero = Ultimonumero + pa
    contador = contador + 1

print(" Fim")