import math
a = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print('Ângulo {:.0f} graus'.format(a))
print('----------------')
print(' Seno {:^10.2f} \n Cosseno {:10.2f} \n Tangente {:^10.2f}'.format(sen,cos,tg))
print('----------------')
