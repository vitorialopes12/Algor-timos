#Vitoria Bezerra Lopes
#Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

def checar_divisibilidade(valor)
if valor%2==0:
  print(f'{valor} é divisível por 2')
else =:
  print(f'{valor} nao é divisível por 2')

if valor%3==0:
  print(f'{valor} é divisível por 3')
else: 
  print(f'{valor} nao é divisível por 3')

num = int(input('Digite um valor: '))

checar_divisibilidade(num)

