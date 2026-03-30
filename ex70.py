continuar = 'S'
soma = 0
maisdemil = 0
anterior = 0
nomeproduto = str(input("Digite o nome do produto: "))
preco = float(input("Preço: R$"))
nomebarato = nomeproduto
atual = preco
soma = soma + preco
if preco > 1000:
    maisdemil = maisdemil + 1

continuar = str(input('Deseja continuar? [S/N]')).upper().strip()

while continuar == "S":
    nomeproduto = str(input("Digite o nome do produto: "))
    preco = float(input("Preço: R$"))
    soma = soma + preco
    if preco > 1000:
        maisdemil = maisdemil + 1

    if preco < atual:
        atual = preco
        nomebarato = nomeproduto


    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()

print(f"{maisdemil} produtos, a soma vai ser R${soma:.2f} e o produto mais barato é o {nomebarato} custando R${atual:.2f}")