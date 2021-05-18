def fatorial(n, show=False):
    """
    -> Calculo de um Fatorial
    :param n: numero a ser calculado
    :param show: apresentar ou não o calculo
    :return: mostra o resultado do calculo
    """
    f = 1
    if show:
        for c in range(n, 0, -1):
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
            f *= c
    return f



print(fatorial(5))
help(fatorial))