#Vitoria Bezerra Lopes
#Calcule e mostre a série 1 + 2/3 + 3/5 + ... 50/99

reaultado = 1
for numero in range(2,51):
  resultado+= numero/((numero*2)-1)
  print(resultado)
