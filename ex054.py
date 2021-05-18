# ler ano de nascimento de 7 pessoas, quantas atingiram a maioridade e quantas não atingiram.
from datetime import date
anoatual = date.today().year
maior = 0
menor = 0
for c in range(1, 3):
    nasc = int(input('Em que ano a {}ª pessoa nasceu: '.format(c)))
    idade = anoatual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Existem {} maior(es) de idade e {} menor(es) de idade!'.format(maior, menor))