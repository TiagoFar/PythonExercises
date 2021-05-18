from random import randint
from time import sleep
cores = {'verde':' \33[1;32m', 'vermelho':'\33[1;31m', 'limpa':'\33[m'}
print ('='*20, 'PEDRA, PAPEL OU TESOURA,' ,'='* 20)
pc = randint(1, 3)
print('''
[ 1 ] PEDRA
[ 2 ] PAPEL 
[ 3 ] TESOURA ''')
opção = int(input('Escolha a sua opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
if pc == opção:
    print('Você escolheu {} e o computador escolheu {}. Houve um EMPATE!'.format(opção, pc))
elif pc == 1 and opção == 2:
    print('Você escolheu {} e o computador escolheu {}. Você {}VENCEU!'.format(opção, pc, cores['verde']))
elif pc == 1 and opção == 3:
    print('Você escolheu {} e o computador escolheu {}. Você {}PERDEU!'.format(opção, pc, cores['vermelho']))
elif pc == 2 and opção == 3:
    print('Você escolheu {} e o computador escolheu {}. Você {}VENCEU!'.format(opção, pc, cores['verde']))
elif pc == 2 and opção == 1:
    print('Você escolheu {} e o computador escolheu {}. Você {}PERDEU!'.format(opção, pc, cores['vermelho']))
elif pc == 3 and opção == 1:
    print('Você escolheu {} e o computador escolheu {}. Você {}VENCEU!'.format(opção, pc, cores['verde']))
elif pc == 3 and opção == 2:
    print('Você escolheu {} e o computador escolheu {}. Você {}PERDEU!'.format(opção, pc, cores['vermelho']))

#pode colocar uma lista e escolher os valores da lista.
#itens = [ 'Pedra', 'Papel', 'Tesoura' ] . format(itens[computador])
#computador = randit(1, 3)
#jogador = a opção escolhida
