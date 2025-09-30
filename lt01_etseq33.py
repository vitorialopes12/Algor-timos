#Vitoria Bezerra Lopes
#Receba um número. Calcule e mostre a serie 1 + 1/2 + 1/3 + ... + 1/5

num = int(input('Digite um número: '))
resultado = 1
for num in range(2, num+1):
  resultado+=1/num
  print(resultado)
