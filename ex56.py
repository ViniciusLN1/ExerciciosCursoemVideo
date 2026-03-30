soma_idade = 0
nome_homemvelho = ""
quantidade_mulhermenos20 = 0
idade_homemvelho = 0
for c in range(1, 5):
    print(f"-----{c}ºpessoa-----")
    nome = str(input("Digite o seu nome: ")).strip()
    idade = int(input("Digite a sua idade: "))
    sexo = str(input("SEXO [F|M]: ")).strip()
    soma_idade = idade + soma_idade
    if c == 1 and sexo in 'Mm':
        nome_homemvelho = nome
        idade_homemvelho = idade
    if sexo in 'Mm' and idade > idade_homemvelho:
        idade_homemvelho = idade
        nome_homemvelho = nome
    if sexo in 'Ff' and idade < 20:
        quantidade_mulhermenos20 = quantidade_mulhermenos20 + 1
mediatotal = soma_idade / 4
print(f'A media total das quatro pessoas é {mediatotal} anos')
print(f'O nome do homem mais velho do grupo é {nome_homemvelho} e ele tinha {idade_homemvelho} anos!')
print(f'Há {quantidade_mulhermenos20} mulheres com menos de 20 anos!')
