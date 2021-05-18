from time import sleep
maior = 0
somar = 0
menu = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
while menu != 5:
    print('''
    === MENU === 
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR 
    [ 4 ] NOVOS NÚMEROS 
    [ 5 ] SAIR''') # esse menu tem que estar identado! Pq está dentro do WHILE!
    menu = int(input('Escolha uma opção: '))
    if menu == 1:
        print(n1 + n2)
    if menu == 2:
        print(n1 * n2)
    if menu == 3:
        if n1 > n2:
            maior = maior + n1
            print('\33[32mO NÚMERO MAIOR É O {}\33[m'.format(maior))
        if n2 > n1:
            maior = maior + n2
            print('\33[32mO NÚMERO MAIOR É O {}\33[m'.format(maior))
        if n1 == n2:
            print('\33[31mOS NÚMEROS SÃO IGUAIS!\33[m')
    if menu == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    if menu == 5:
       print('.')
       sleep(1)
       print('.')
       sleep(1)
       print('.')
       sleep(1)
       print('TERMINOU!')
    else:
        print('Opção inválida! Tente novamente!')
        print('='*20) # aqui vai mostrar o divisor em cada parte pq está identado pra dentro!
print('FIM  =)')












