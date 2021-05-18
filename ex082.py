lista = []
par = []
imp = []
resp = ' '
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if 'N' in resp:
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        imp.append(v)
print(f'O números digitados foram {lista}')
print(f'Os números pares são: {par}')
print(f'Os números ímpares são: {imp}')

