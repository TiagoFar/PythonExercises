vel = float(input('Digite a velocidade do carro (km/h): '))
if vel <= 80:
    print('Você esta a {} km/h e está dentro da velocidade permitida!'.format(vel))
else:
    print('Você está a {} km/h e ultrapassou o limite de velociada via!'.format(vel))
    print('Você receberá uma multa de {} reais!'.format((vel-80)*7))