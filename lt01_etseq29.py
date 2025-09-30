#Vitoria Bezerra Lopes
#Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.

tipo_investimento = int(input('Digite 1 para poupanca ou digite 2 para renda fixa: '))
valor = float(input('Digite o valor do investimento: '))

if tipo_investimento==1:
  print(f'Em 30 dias voce terá {valor*1.03:2.f}')
elif tipo_investimento==2:
  print(f'Em 30 dias voce tera {investimento*1.05:.2f}')
