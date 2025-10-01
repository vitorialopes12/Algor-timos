#Vitoria Bezerra Lopes
#Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente. 

def organizar_em_crescente()
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

if valor2>valor1:
  print(f'Em ordem crescente os valores ficam: {valor1}, {valor2}')
else: 
  print(f'Em ordem crescente os valores ficam: {valor2}, {valor1}')
organizar_em_crescente()  

