from datetime import datetime

registro = {}
print('='*30,'> Carteira de Trabalho <','='*30)
registro['nome'] = str(input('Digite seu nome:'))
nasc = int(input('Digite seu ano de nascimento: '))
registro['idade'] = datetime.now().year - nasc
registro['ctps'] = int(input('Digite o número da sua carteira de trabalho(0 para não tem): '))
if registro['ctps'] != 0:
    registro['anocontrato'] = int(input('Digite o ano de contratação: '))
    registro['salario'] = float(input('Digite o seu salário: '))
    registro['aposentadoria'] = registro['idade'] + ((registro['anocontrato']+ 35) - datetime.now().year)
for k, v in registro:
    print(f'A sua {k} se dará em {v} anos ') #key(chave) value(valor)

print(registro)



