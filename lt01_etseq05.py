#Vitoria Bezerra Lopes
#Receba os coeficientes A,B e C de uma equacÃo do 2º grau. Calcule e mostre as raízes reais (considerar que a equacao possue 2 raízes)

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

delta = (b**2)-(4*a)*c
x1 = (-b+(delta**0.5))/2*a
x2 = (-b-(delta**0.5))/2*a

print(delta)
print(x1)
print(x2)
