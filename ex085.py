lista = []
par = lista[:]
imp = lista[:]
for c in range(1, 8):
    val = int(input(f'Digite o {c}º valor: '))
    lista.append(val)
    if val % 2 == 0:
        par.append(val)
    else:
        imp.append(val)
lista.sort()
par.sort()
imp.sort()
print('#'*40)
print(f'Os valores digitados foram {lista}')
print(f'Os valores pares são {par}')
print(f'Os valores ímpares são {imp}')
print('#'*40)


