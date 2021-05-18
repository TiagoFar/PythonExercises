aluno = {}

aluno['nome'] = str(input('Digite seu nome: '))
aluno['media'] = float(input('Digite sua média: '))
if aluno['media'] < 5:
    print('Aluno Reprovado!')
    aluno = 'Reprovado!'
elif 5 <= aluno['media'] < 7:
    print('Aluno em Recuperação!')
    aluno['Situacao'] = 'Recuperação!' # aqui coloquei dentro do dicionário , aluno['situacao'] para guardar as palavras, aprovado, rep e rec.
elif aluno['media'] >= 7:
    print('Parabéns,você foi APROVADO!')
    aluno['Situacao'] = 'Aprovado!'
for k, v in aluno.items(): # vai mudar de acordo com o range. e mostra o ultimo adicionado de acordo com o 'IF'.
    print(f' - {k} é igual {v}')


