time = []
atletas = {}
partidas = []
while True:
    atletas.clear() # limpo os dados a cada laço feito
    atletas['nome'] = str(input('Digite o nome do Atleta: '))
    tot = int(input(f'Quantas partidas {atletas["nome"]} jogou: '))
    partidas.clear()
    for c in range(1, tot+1):
        partidas.append(int(input(f'  > Quantos pontos no Jogo {c}?:  ')))
    atletas['pontos'] = partidas[:]
    atletas['tot'] = sum(partidas) #'sum' é soma
    time.append(atletas.copy()) #coloco o dicionário aprov dentro da lista time, não pode fazer fatiamento dentro de dicionário (ex: [:])
    while True:
        resp = str(input('Quer continuar [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N': #identado no while.
        break
print('-'*30) # aqui começa o cabeçalho para mostrar os resultados
print('cod', end='')
for i in atletas.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*30)
while True:
    busca = int(input('Mostrar dados de qual atleta?[999 para parar]: '))
    if busca == 999: # não pode ser entrar aspas! é um número e não uma string.
        break
    if busca > len(time):
        print(f'Erro. Não existe atleta com código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO ATLETA {time[busca]["nome"]} -- ')
        for i, g in enumerate(time[busca]["pontos"]):
            print(f'   No jogo {i+1} fez {g} pontos.')
    print('-'*40)
print('FIM')









