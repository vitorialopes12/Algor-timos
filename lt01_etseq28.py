#Vitoria Bezerra Lopes
#Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que: Venda Mensal	Preço Atual	Preço Novo < 500	< 30	+ 10% >= 500 e < 1000	>= 30 e < 80	+15% >= 1000	>= 80	- 5% Obs.: para outras condições, preço novo será igual ao preço atual.

media = int(input('Digite a média de venda mensal do produto: '))
preco = float(input('Digite o preco atual do produto: '))

if media<500 and preco <30:
  novo = preco*1.10
elif 500<=media<1000 and 30<=preco<80:
  novo =preco*1.15
elif media >=1000 and preco>80:
  novo = peco*0.95
else:
  print(f'O novo preco é: R${novo:.2f}')
  
