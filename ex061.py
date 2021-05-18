termo = int(input('Digite o primeiro termo para a PA: '))
razão = int(input('Digite a razão para a PA: '))
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' > ')
    cont += 1
    termo += razão
print('Acabou')