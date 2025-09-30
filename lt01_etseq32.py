#Vitoria Bezerra Lopes
#Receba um número inteiro. Calcule e mostre o seu fatorial.

num = int(input('Digite um número: 0'))
resultado = 1
for num in range(numero,1,-1):
  resultado*=num
print(f'O fatorial de {num} é {resultado}')
