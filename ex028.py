from random import randint
from time import sleep
computador = randint(0,5)  # Sorteia de 0 a 5 um número
jogador = (input('Pensei em um número entre 0 e 5, qual número eu pensei?: '))
print('Processando...')
sleep(3) # é um timer de 3s antes de soltar a resposta
if jogador == computador:
    print('Parabéns, você acertou!')
else:
    print('Não foi desta vez!')