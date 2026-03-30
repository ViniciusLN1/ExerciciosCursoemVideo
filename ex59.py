 numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
print("")
print(f'''NÚMERO 1 = {numero1}, NÚMERO 2 = {numero2}
[ 1 ] - SOMAR
[ 2 ] - MULTIPLICAR
[ 3 ] - MAIOR
[ 4 ] - ADICIONAR OUTROS 2 NUMEROS
[ 5 ] - SAIR''')
print("")
escolha = int(input("Faça sua escolha: "))
print("")
while escolha != 5:
    if escolha == 1:
        soma = numero1 + numero2
        print(f"{numero1} + {numero2} = {soma}")
        print("")
    else:
        if escolha == 2:
            multi = numero1 * numero2
            print(f"{numero1} * {numero2} = {multi}")
            print("")
        else:
            if escolha == 3:
                if numero1 > numero2:
                    print(f"O numero {numero1} é o maior número!")
                    print("")
                else:
                    if numero2 > numero1:
                        print(f"O número {numero2} é o maior número!")
                    else:
                        if numero1 == numero2:
                            print("Os números são iguais!!")
    if escolha == 4:
        numero1 = int(input("Digite novamente o primeiro número: "))
        numero2 = int(input("Digite novamente o segundo número: "))
        print("")
    print(f'''NÚMERO 1 = {numero1}, NÚMERO 2 = {numero2}
    [ 1 ] - SOMAR
    [ 2 ] - MULTIPLICAR
    [ 3 ] - MAIOR
    [ 4 ] - ADICIONAR OUTROS 2 NUMEROS
    [ 5 ] - SAIR''')
    print("")
    escolha = int(input("Mais algo? "))





