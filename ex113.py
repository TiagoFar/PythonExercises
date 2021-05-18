def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número válido.')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\n\033[31mErro: por favor, digite um número real válido.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um valor inteiro:  ')
n2 = leiaFloat('Digite um valor real:   ')
print(f'O valor inteiro digitado foi {n1} e valor real digitado foi {n2}')

