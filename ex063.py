#Sequencia de Fibonnacci
from time import sleep
t1 = 0
t2 = 1
n = int(input('Digite um valor para mostrar a sequencia de Fibonacci: '))
print('{} - {}'.format(t1, t2),end='')
cont = 3
while cont <= n:
    t3 = t2 + t1
    cont += 1
    sleep(0.5)
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
print(' Fim')


