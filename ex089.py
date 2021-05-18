lista = []
resp = ' '
while True:
    nome = str(input('Digite seu nome: '))
    n1 = float(input('Digita a 1ª nota: '))
    n2 = float(input('Digite a 2ª nota: '))
    med = (n1 + n2) / 2
    lista.append([nome, [n1, n2], med])
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-'*30, 'Boletim', '-'*30)
print(f'{"nº":<4} {"Aluno":<10} {"Média":>10}')
for i, v in enumerate(lista):
    print(f'{i:<4} {v[0]:<10} {v[2]:>10.1f}')
while True:
    opc = int(input('Qual aluno você deseja ver as notas? '))
    if opc <= len(lista) -1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
    resp1 = str(input('Deseja Parar ou Continuar [P/C]: ')).strip().upper()[0]
    if resp1 == 'P':
        print('FIM')
        break



