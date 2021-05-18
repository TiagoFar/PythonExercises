tot = soma = n = 0
while n != 999:
    n = int(input('Digite um número: '))
    tot += 1
    soma += n
if n == 999:
        tot -= 1
        soma -= n
print('Você digitou {} e o programa terminou!'.format(n))
print('---------------------------------------')
print('Foram digitados {} números'.format(tot))
print('---------------------------------------')
print('A SOMA DE TODOS OS NÚMEROS FOI {}'.format(soma))
