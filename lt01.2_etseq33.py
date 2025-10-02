#Vitoria Bezerra Lopes
#Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.

def calcular_serie(n)
soma = 0
for i in range(1, n+1):
  soma +=1/i
print('Resultado da série:', soma)
n = int(input('Digite um número: '))
calcular_serie(n)
