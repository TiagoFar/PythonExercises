from random import randint
sorteio = (randint(1, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))
print(f'Soteados: {sorteio}', end='')
for n in sorteio:
    print(f'Maior valor = {max(n)}')
    print(f'Menor valor = {min(n)}')
print('FIM')
