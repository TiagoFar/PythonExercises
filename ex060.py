#Fatorial
n = int(input('Digite um número para verificar o seu fatorial: '))
c = n
f = 1 #número 1 pq se for 0, o número q vai multiplicar por ele vai ser zero, para manter o número digitado precisa ser 1.
while c > 0:
    print('{}'.format(c), end='')
    print(' x' if c > 1 else ' =', end=' ')
    f *= c
    c -= 1
print(f)