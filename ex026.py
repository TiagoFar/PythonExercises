frase = str(input('Digite uma frase:  ')).strip()
print('A letra A aparece {} vez(es): '.format(frase.upper().count('A')))
print('A primeira letra A apareceu na posição: {}'.format(frase.upper().find('A')+1))
print('A última letra A apareceu pela última vez na posição {}'.format(frase.upper().rfind('A')+1))
#posso colocar o upper(). direto na string, na primeira linha, depois de strip().
