matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
totpar = somacol = maiorv = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor [{l},{c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:^5}', end='')
        if matriz[l][c] % 2 == 0:
            totpar += matriz[l][c]
    print()  # print identado pra dentro para pular linha a cada 3 ( range 3
for l in range(0, 3):#soma da terceira coluna
    somacol += matriz[l][2]
for c in range(0, 3): #maior valor da segunda linha
    if c == 0: #primeiro elemento que vai começar
        maiorv = matriz[1][c]
    elif matriz[1][c] > maiorv:
        maiorv = matriz[1][c]
print(':'*40)
print(f'A soma de todos os valores pares é: {totpar}')
print(f'A soma dos valores da terceira coluna é: {somacol}')
print(f'O maior valor da segunda linha é: {maiorv}')









