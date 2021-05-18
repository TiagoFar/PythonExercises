aprov = {}
partidas = []
aprov['nome'] = str(input('Digite o nome do Atleta: '))
tot = int(input(f'Quantas partidas {aprov["nome"]} jogou: '))
for c in range(1, tot+1):
    partidas.append(int(input(f'  > Quantos pontos no Jogo {c}?:  ')))
aprov['pontos'] = partidas[:]
aprov['tot'] = sum(partidas) #'sum' é soma
print(aprov)
print('~'*45)
for k, v in aprov.items():
    print(f'O campo {k} tem o valor {v} ')
print('~'*45)
print(f'O jogador {aprov["nome"]} jogou {len(partidas)} partidas')
for i, v in enumerate(aprov['pontos']):
    print(f'  -> Na partida {i+1} fez {v} gols ')
print(f'Foi um total de {aprov["tot"]} pontos!')






