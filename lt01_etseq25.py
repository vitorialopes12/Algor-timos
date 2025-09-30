#Vitoria Bezerra Lopes
#Receba a hora de inicio, e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode comecar num dia e terminar noutro.

hora_inicio = int(input('Digite a hora de inicio do jogo: '))
minuto_inicio = int(input('Digite o minuto de inicio do jogo: '))

hora_fim = int(input('Digite a hora do fim do jogo: '))
minuto_fim = int(input('Digite o minuto final do jogo: '))

duracao_minuto = 0
duracao_hora = 0

if minuto_fim>=minuto_inicio:
  duracao_minuto = minuto_fim-minuti_inicio
else:
  duracao_hora -=1
  duracao_minutos = minuto_inicio-minuto_fim 

if hora_fim>hora_inicio:
  duracao_hora+=hora_fim-hora_inicio
else:
  duracao_hora += (hora_fim+24)-hora_inicio

print(f'O jogo teve duracao de {duracao_hora} horas e {duracao_minutos} minutos')
