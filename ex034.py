#Aumento de Salário
sal = float(input('Digite o seu salário para saber quanto irá ficar: '))
if sal >= 1.250:
    print('Seu salário {:.3f} reais, terá um aumento de 10% e ficará {:.3f} reais '.format(sal, (sal*0.10) + sal))
else:
    print('Seu salário {:.3f} reais, terá um aumento de 15% e ficará {:.3f} reais '.format(sal, (sal*0.15) + sal))
