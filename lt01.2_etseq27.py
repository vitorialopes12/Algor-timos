#Vitoria Bezerra Lopes
#Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

def calcular_vel_media():
  voltas = int(input('Digite o número de voltas: '))
  tamanho = int(input('Digite o tamanho do circuito em metros: '))/1000
  duracao = int(input('Digite a duraçao do circuito em minutos: '))/60

km = ((tamanho/duracao)*voltas)
print(f'{km:.2f}Km/h)')
calcular_vel_media()
