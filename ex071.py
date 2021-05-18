
valor = 0

print('Notas disponíveis [ 50,00 / 20,00 / 10,00 / 1,00 ]')
valor = int(input('Qual valor você quer sacar: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced =+ 1
    else:

        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break





print(f'Total de {totced} cédulas de {ced}')
print('Dinheiro Sacado! Volte Sempre!')