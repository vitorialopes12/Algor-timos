#Vitoria Bezerra Lopes
#Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.

def calcular_duracao(hora_inicio, hora_fim, minuto_inicio, minuto_fim):
  duracao_hora = 0
  duracao_minuto = 0

if minuto_fim>=minuto_inicio:
  duracao_minutos = minuto_fim-minuto_inicio
else:
  duracao_hora -=1
  duracao_minutos = minuto_inicio-minuto_fim
if hora_fim>hora_inicio:
  duracao_hora += hora_fim-hora_inicio
else: 
  duracao_hora += (hora_fim+24)-hora_inicio
  print(f'O jogo teve duraçao de {duracao_hora] horas e {duracao_minutos} minutos')

hora_inicio = int(input('Digite a hora inicial do jogo: '))
minuto_inicio = int(input('Digite o minuto inicial do jogo: '))

hora_fim = int(input('Digite a hora final do jogo: '))
minuto_fim = int(inou('Digite o minuto final do jogo: '))

calcular_duracao(hora_inicio, hora_fim, minuto_inicio, minuto_fim)
