preços = ('Caneta', 1.99, 'Lápis', 1 , 'Régua', 2.50)
print('*'*30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('*'*30)
for pos in range(0, len(preços)):
    if pos % 2 == 0:
        print(f'{preços[pos]:.<20}', end=' ')
    else:
        print(f'R${preços[pos]:.2f}')
print('*'*30)
