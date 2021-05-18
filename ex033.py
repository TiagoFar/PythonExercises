#Programa que ler 3 números e diz qual é o maior e qual é o menor
a = int(input('Digite o 1o número: '))
b = int(input('Digite o 2o número: '))
c = int(input('Digite o 3o número: '))
# Verificando o menor número
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor número digitado é {}'.format(menor))
# Verificando o maior número
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior número digitado é {}'.format(maior))
