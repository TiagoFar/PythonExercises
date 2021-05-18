l1 = float(input('Digite o tamanho em metros de um lado da parede:'))
l2 = float(input('Digite o outro lado: '))
a = l1*l2
t = a/2
print('Sua primeira parede mede {}m, a segunda {}m e você possue uma \n área de {}m, você precisará de {}l de tinta \n para pintar as paredes!'.format(l1,l2,a,t))