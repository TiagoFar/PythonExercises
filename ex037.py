n = int(input('Digite um número para conversão: '))
print('''Escolha uma das bases numéricas para conversão
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
opção = int(input('Digite uma opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é {}'.format(n, bin(n)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é {}'. format(n, oct(n)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é {}'. format(n, hex(n)[2:]))
else:
    print('Opção inválida!')