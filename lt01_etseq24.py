#Vitoria Bezerra Lopes
#Receba o valor inteiro. Verifique e mostre se é divisivel por 2 e 3.

valor = int(input('Digite um valor:'))

if valor%2==0:
  print(f'{valor} é divisível por 2')
else: 
  print(f'{valor} nao é divisível por 2')

if valor%3==0:
  print(f'{valor} é divisível por 3')
else:
  print(f'{valor} nao é divisível por 3')
