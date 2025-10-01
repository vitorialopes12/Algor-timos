#Vitoria Bezerra Lopes
#Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.

def calcular_distancia(t, vm):
  distancia_viajada = t*vm
  print(f'O veículo gasta {distancia_viajada/12:.2}litros em uma viagem de {distancia_viajada}km'})
tempo = float(input('Digite o número de horas viajadas: '))
velocidade_media = float(input('Digite a velocidade média da viagem em km/h: '))
clcular_distancia(tempo, velocidade_media)
