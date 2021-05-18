import math
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
print('O triangulo de cateto oposto {} '
      'e cateto adjacente {} tem a '
      'Hipotenusa {:.2f}'.format(co, ca, math.hypot(co, ca)))


