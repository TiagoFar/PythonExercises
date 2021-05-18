from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome,'rt') # rt read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #write text, (escreve texto) se não tiver, ele cria ' + '
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao tentar ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';') # separo minha dentro da minha lista depois do ';'
            dado[1] = dado[1].replace('\n','') #troca a quebra de linha por nada
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') #append text > incluir
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()
