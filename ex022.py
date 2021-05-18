nome = str(input('Digite seu nome completo: ').strip())
print('-----------------------------------')
print("Seu nome em letras minúsculas...")
print(nome.lower())
print('-----------------------------------')
print('Seu nome em letras maiúsculas')
print(nome.upper())
print('-----------------------------------')
print('Seu nome tem {} caracteres'.format(len(nome)-nome.count(' ')))
print('-----------------------------------')
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print("ou melhor..")
lista = nome.split()
print("Seu primeiro nome é {} e tem {} letras".format(lista[0], len(lista[0])))



