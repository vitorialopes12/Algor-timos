#Vitoria Bezerra Lopes
#Mostre todas as possibilidades de 2 dados de forma que a soma tenha como resultado 7.

def calcular_resultados()
lados = 6
lista - []
for resultado_dado1 in range(lados+1):
  for resultado_dado2 in range(lados+1):
    if resultado_dado1 + resultado_dado2 == 7:
      lista.append((resultado_dado1, resultado_dado2))
print(lista)
calcular_resultados()
