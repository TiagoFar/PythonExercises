lista = []
for cont in range(0, 5):
    n = int(input('Digite um valor: '))
    if cont == 0 or n > lista[-1]:
        lista.append(n)
        print(f'O valor foi adicionado no final!')
    else:
        pos = 0
        while pos < len(lista): # varrer o vetor da posicao 0 até o ultimo VALOR
            if n <= lista[pos]: # numero for menor ou igual ao numero da sua respectiva posição
                lista.insert(pos, n) # insiro na posicao o número digitado
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1
print('=-'*30)
print(f'Os valores adicionados na ordem foram: {lista}')






