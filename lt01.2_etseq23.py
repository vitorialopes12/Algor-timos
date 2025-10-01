#Vitoria Bezerra Lopes
#Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.

def organizador_de_num(valor_seq1, valor_seq2, valor_seq3,valor_outro):
  if valor_outro>valor_seq3:
    print(valor_seq1, vaolor_seq2, valor_seq3, valor_outro)
  elif valor_outro>valor_seq2:
    print(valor_seq1, valor_seq2, valor_outro, valor_seq3)
  elif valor_outro>valor_seq1:
    print(valor_seq1, valor_outro, valor_seq2, valor_seq3)
  else: 
    print(valor_outro, valor_seq1, valor_seq2, valor_seq3)

valor1 = int(input('Digite o primeiro valor: '))|
valor2 = int(input('Digite o segundo valor: '))

while valor2<valor1:
   valor2 = int(input('Digite o segundo valor: '))
  valor3 = int(input('Digite o terceiro valor: '))
while valor3<valor2:
  valor3 = int(input('Digite o terceiro valor: '))
 valor4 = int(input('Digite um valor qualquer: '))

organizador_de_num(valor1, valor2, valor3, valor4) 
    
