from ex115.lib.interface import * #importa tudo
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq): # se não existir o arquivo...
    criarArquivo(arq) # chamo a função criar arquivo

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa',
      'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Opção cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[0;31Erro: Digite uma opção válida!\033[m')
    sleep(2)


