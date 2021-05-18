n = 0
c = 0

while True:
    print('-' * 15)
    tab = int(input('Digite um valor para exibir a sua tabuada: '))
    print('-' * 15)
    if tab < 0:
        break
    for c in range(0, 11):
        print(f'{tab} x {c} = {tab*c}')
print('FIM')
