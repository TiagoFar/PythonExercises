p = float(input('Digite o preço que está na etiqueta do produto: '))
d = (p*5)/100
np = p - d
print('O produto custava {} reais, mas você ganhou um desconto de 5% '
      'Equivalente a {:.2f} reais e com isso o seu novo preço é de {:.2f} reais. Parabéns!!'
      .format(p,d,np))
