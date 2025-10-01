#Vitoria Bezerra Lopes
#Receba 3 coeficientes A, B e C de uma equação do 2º grau da fórmula AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.

def equacao_segundo_grau(A,B,C):
  delta = (B**2)-((4*A)*C)
 if delta == 0:
   raiz =-8/(2*A)
   print(f'A raiz real do coeficiente é {raiz})
  elif delta<0:
 print(f'Delta resultou em {delta}, deltas negativos nao possuem raizes reais')
 else:
 x1 = (B+(delta**0.5))/2*A)
 x2 = (B-(delta**0.5))/2*A)

 valorA = int(input('Digite o valor do coeficiente A: '))
 valorB = int(input('Digite o valor do coeficiente B: '))
 valorC = int(input('Digite o valor do coeficiente C: '))

 equacao_segundo_grau(valorA, valorB, valorC)
 
 
