from time import sleep
def contador (i, f, p):
    if i < 0: # esses dois ifs tem q ter a checagem antes do print pra funcionar.
        p *= -1
    if p == 0:
        p = 1 # se for igual a Zero não vai contar, então troco por 1!
    print(f'Contando de  {i} até {f} de {p} em {p}')
    sleep(2.5)
    print('='*20)
    if i < f:
        cont = i # se for número negativo tem q ser 1
        while cont <= f: #cont é igual ao início na primeira tupla ( = 1 )
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p # contador receber contador + o passo da tupla, ( = 1)
        print('Fim')
    else: # se i > f # tiro um passo do contador!
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('Fim')


#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('='*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início:   '))
fim = int(input('Fim:      '))
pas = int(input('Passo:    '))
contador(ini, fim, pas)


