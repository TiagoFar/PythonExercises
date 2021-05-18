#Dizer se as retas formam um triângulo
A = int(input('Digite o valor da 1a reta: '))
B = int(input('Digite o valor da 2a reta: '))
C = int(input('Digite o valor da 3a reta: '))
if A < B + C and B < A + B and C < B + A:
    print('O triângulo pode ser feito!')
else:
    print('O triãngulo não pode ser feito!')