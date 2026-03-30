pessoamais18 = 0
quantidadehomem = 0
mulhermenos20 = 0
continuar = "S"
while continuar == "S":
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo: ")).upper().strip()

    if idade >= 18:
        pessoamais18 = pessoamais18 + 1

    if sexo == "M":
        quantidadehomem = quantidadehomem + 1

    if sexo == "F" and idade < 20:
        mulhermenos20 = mulhermenos20 + 1

    continuar = str(input("Deseja continuar? [S/N]")).upper().strip()[0]

print(f"{mulhermenos20}, {quantidadehomem}, {pessoamais18}")