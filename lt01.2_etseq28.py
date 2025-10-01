#Vitoria Bezerra Lopes
#Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que: Venda Mensal	Preço Atual	Preço Novo < 500	< 30	+ 10% >= 500 e < 1000	>= 30 e < 80	+15% >= 1000	>= 80	- 5% Obs.: para outras condições, preço novo será igual ao preço atual.

def calcular_novo_preco(preco, vendas):
    if vendas < 500 and preco < 30:
        novo_preco * 1.10
    elif 500 <= vendas < 1000 and 30 <= preco < 80:
        novo_preco * 1.15
    elif vendas >= 1000 and preco >= 80:
        novo_preco * 0.95
    else:
        novo_preco = preco

preco = float(input("Preço atual: "))
vendas = int(input("Vendas mensais: "))
novo_preco = calcular_novo_preco(preco, vendas)
print(f"Novo preço: R$ {novo_preco:.2f}")
