#Soma de ímpares que são múltiplos de 3 entre 1 e 500.
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 # aqui é um contador!!!
        soma += + c # é a mesma coisa que soma = soma + c #aqui é um acumulador!!!
print('A soma de todos os {} valores é {}'.format(cont, soma))
