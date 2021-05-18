lista = []
# PRA RESOLVER ESSE EXERCICIO, NAO COLOCO O APPEND DIRETO PRA LISTA, PRIMEIRO IDENTIFICO SE É REPETIDO.
while True:
    num = int(input('Digite o valor: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Valor duplicado! Número não inserido!')
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
    else:
        print('#'*30)

print(sorted(lista))


