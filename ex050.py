#Ler 6 números inteiros e fazer a soma somente dos pares
soma = 0
cont = 0
for c in range (1, 7):
    num = int(input('Digite o {}º valor:'.format(c)))
    if num % 2 == 0:
        cont += +1
        soma += num
print('Você informou {} númer(os) par(es) e a soma foi {}'.format(cont, soma))