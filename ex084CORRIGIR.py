num = []
# dados = []
maior = 0
menor = 0

for c in range(0, 5):
    num.append(int(input(f'Digite um número na posição {c}: ')))
    if c == 0:
        maior = num[c] # vou varrendo os números dentro da lista num>>  num[c]
        menor = num[c] # igual maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            num[c] = menor
print('#'*40)
print(f'Você digitou os seguintes valores: {num}')
print(f'O maior valor digitado foi o {maior} na posição ', end='') #não quebro a linha para mostrar o número de baixo na sequência!
for i, v in enumerate(num):
    if v == maior: # se valor da lista for igual o maior valor...
        print(f'{i}', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}', end='')
print()
print('FIM')




