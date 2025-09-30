#Vitoria Bezerra Lopes
#Receba o número de voltas, a extensao do circuito (em metros) e o tempo de duracao (minutos). Calcule e mostre a velocidade média em km/h.

voltas = int(input('Digite o número de voltas: '))
tamanho = int(input('Digite o tamanho do circuito em metros: '))/1000
duracao = float(input('Digite a duracao do circuito em minutos: '))/60

km = ((tamanho/duracao)*voltas)
print(f'{km:.2f}Km/h')
