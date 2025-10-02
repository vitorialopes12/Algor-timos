#Vitoria Bezerra Lopes
#Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.

def fibonacci(numero)
n1 = 0
n2 = 0
for i in range(numero)
soma = n1+n2
if soma == 0:
  soma = 1
  n1 = soma
else: 
  if n1>=n2:
    n2 = soma
    print(soma)
 numero = int(input('Digite um número: '))
fibonacci(numero)
