def cabecalho(texto): # Essa função defini cabeçalho personalizado
    tam = len(t) + 4
    print('-'* tam)
    print(f'  {texto}')
    print('-'* tam)

#Programa Principal
t = str(input('Digite um texto: '))
cabecalho(t)

