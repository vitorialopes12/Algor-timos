#Vitoria Bezerra Lopes
#Receba 2 valores reias. Calcule e mostre o maior deles. 

def idenificador_maior(valor1, valor2):
  if valor1>valor2:
    print(f'O {valor1} é o maior número digitado')
  else: 
  print(f'O {valor2} é o maior número digitado')

num1 = float(input('Digite um valor real: '))
num2 = float(input('Digite um outro valor real: '))
identificar_maior(num1, num2)
