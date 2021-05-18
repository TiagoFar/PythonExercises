from datetime import date
def funcao(a):
    if a < 16:
        print('Ainda não pode votar!')
    if a >= 16 and a < 18:
        print('Voto não obrigatório')
    if a >= 18 and a < 65:
        print('Voto Obrigatório')
    if a > 65:
        print('Voto Opcional')
anoatual = date.today().year
print(f'Ano: {anoatual}')
resp = int(input('Em que ano você nasceu?: '))
idade = anoatual - resp
print(f'A sua idade é {idade}')
funcao(idade)

