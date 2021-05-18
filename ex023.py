num = int(input('Digite um número com 4 dígitos:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('o número {}, tem {} unidade(s),'
      '{} dezena(s),{} centena(s) e {} milhar(es)'.format(num, u, d, c, m))
