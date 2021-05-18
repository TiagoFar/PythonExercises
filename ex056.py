#LER O NOME , IDADE E SEXO DE 4 PESSOAS. MOSTRAR A MEDIA DE IDADE DO GRUPO, QUAL É O HOMEM MAIS VELHO E QUANTAS MULHERES COM MENOS DE 20 ANOS
somaidade = 0
media = 0
maioridadehomem = 0
maisvelho = '' # aqui é nome! está vazio, "zerado".
totmulher20 = 0

for c in range(1, 5):
    print(' '*10 ,'{}ªPESSOA'.format(c))
    nome = str(input('Qual o nome: '))
    idade = int(input('Qual a idade: '))
    sexo = str(input('Qual o sexo [F/M]: '))
    somaidade += idade
    if c == 1 and sexo in 'Mm': #primeira pessoa digitada do sexo masculino vai ser a mais velha e o nome também.
        maioridadehomem = idade
        maisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        maisvelho = nome
    if sexo in 'Ff' and idade < totmulher20:
        totmulher20 += 1
media = somaidade/4
print('A média de idade do grupo é {}'.format(media))
print('O nome do mais velho tem {} anos e se chama {}'.format(maioridadehomem, maisvelho))
print('Ao todo são {} mulher(es) com menos de 20 anos'.format(totmulher20))


