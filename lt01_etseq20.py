#Vitoria Bezerra Lopes
#Receba 3 coeficientes A,B e C de uma equaçao do 2º grau. Verifique e mostre a existencia de raizes reais e se caso exista, calcule e mostre.

A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))
C = int(input('Digite o valor de C: '))        
delta = (B**2)-((4*A)*C)

if delta == 0:
  raiz = -B/(2*A)
  print(f'A raiz real é {raiz}')
elif delta<0:
  print(f'O resultado de delta é: {delta}, delta negativo nao possui raiz real')
else:
  x1 = (B+(delta**0.5))/2*A
  x2 = (B-(delta**0.5))/2*A
  print(f'A primeira raiz é: {x1:.2f}')
  print(f'A segunda raiz é: {x2:.2f}')
  
  
  
