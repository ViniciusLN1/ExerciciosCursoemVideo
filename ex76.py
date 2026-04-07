produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.00, 'Canetas', 22.30, 'Livro', 34.90)

print('Listagem de preços')

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    if pos % 2 == 1:
        print(f'R${produtos[pos]:.2f}')
