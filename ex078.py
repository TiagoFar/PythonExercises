valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite o valor na posição {cont}: ')))
for pos, val in enumerate(valores):


    print(f'Na posição {pos} você digitou o valor {val}')
print(f'Você digitou os seguintes valores {valores}')
print(f'O maior valor digitado foi {max(valores)}')
print(f'O menor valor digitado foi {min(valores)}')




