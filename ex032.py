from datetime import date #importada para mostrar o ano da máquina caso digite 0
a = int(input('Digite o ano para descobrir se é bissexto ou coloque 0 para o ano atual: '))
if a == 0:
    ano = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 ==0:
    print('É um ano bissexto!')
else:
    print('Não é um ano bissexto!')
