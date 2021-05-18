d = int(input('Quantos dias alugados: '))
km = float(input('Quantos km foram rodados: '))
pkm = 60*d
dkm = 0.15*km
print('Você ficou {} dias e rodou {}km, '
      'então você deverá pagar {} reis'.format(d,km,(pkm+dkm)))
