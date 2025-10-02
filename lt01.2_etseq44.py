#Vitoria Bezerra Lopes
#Receba o número da base e do expoente. Calcule e mostre o valor da potência.

def potenciacao(base, expoente):
  resultado_potencia = base**expoente
  print(f'O valor da potencia é: {resultado_potencia}')
  base = int(input('Digite o valor da base: '))
  expoente = int(input('Digite o valor do expoente: '))
  potenciacao(base, expoente)
