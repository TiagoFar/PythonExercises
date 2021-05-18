import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.linkedin.com')
except urllib.error.URLError: #exceção padrão, sem ela tbm funciona!
    print('O site Linkedin não está acessível no momento.')
else:
    print('Consegui acessar o site no momento')
    #print(site.read()) <<== consegue ler o conteúdo do site