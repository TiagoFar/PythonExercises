tot = soma = n = maior = menor = 0
resp = 'S'
while resp in 'S':
    n = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    tot += 1
    soma += n
    med = soma / tot
    if tot == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Você digitou {} e o programa terminou!'.format(n))
print('---------------------------------------')
print('Foram digitados {} números'.format(tot))
print('---------------------------------------')
print('A SOMA DE TODOS OS NÚMEROS FOI {}'.format(soma))
print('A MÉDIA ENTRE ELES FOI {:.2f}'.format(med))
print('O MAIOR VALOR DIGITADO FOI {}'.format(maior))
print('O MENOR VALOR DIGITADO FOI {}'.format(menor))
