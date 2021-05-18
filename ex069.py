maior18 = masc = totmulher20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' ' # tem q ficar no laço
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
            break


print(f'EXISTEM {maior18} PESSOA(S) COM MAIS DE 18 ANOS')
print(f'FORAM CADASTRADOS {masc} HOMEM(NS)')
print(f'EXISTEM {totmulher20} MULHER(ES) COM MENOS DE 20')
print('Terminou')