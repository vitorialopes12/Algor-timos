#Vitoria Bezerra Lopes
#Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possue2 raízes).

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
 
 
