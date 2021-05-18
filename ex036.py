c = float(input('Qual o valor da casa?: '))
s = float(input('Qual o seu salário?: '))
p = int(input('Em quantos anos pretende pagar?: '))
print('O valor da casa é {:.3f} reais, o seu salário é de {:.3f} reais, '
      'e você pretende pagar em {} anos.'.format(c, s, p))
valp = c/ (p*12)
sal30 = s*0.30
if sal30 >= valp:
    print('Parabéns,o valor da parcela ficou em '
          '{:.3f} reais e você poderá contratar o empréstimo!'.format(valp))
else:
    print('Infelizmente o valor da parcela ficou '
          '{:.3f} reais e não será possível contratar o empréstimo!'.format(valp))