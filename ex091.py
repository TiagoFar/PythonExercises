from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1': randint(1, 6),'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
ranking = []
print('Os valores sorteados foram: ')
for k, v in jogo.items():
        print(f'O {k} tirou o {v}')
        sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #key=itemgetter(1) , 1 ordena por ordem de valor, 0 por ordem de chave.
print('='* 30, 'Ranking', '='*30)
for i, v in enumerate(ranking):
        print(f'{i+1}º lugar: {v[0]} com {v[1]}')
        sleep(1)





