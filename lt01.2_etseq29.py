#Vitoria Bezerra Lopes
#Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.

def calcular_investimento()
 tipo_investimento = int(input('Digite 1 para poupança e 2 para renda fixa: '))
   investimento = float(input('Digite o valor do investimento: '))
if tipo_investimento==1
print(f'Em 30 dias voce terá: {investimento*1.03;.2f})')
elif tipo_investimento==2
print(f'Em 30 dias voce terá {invesvestimento*1.05:.2f}')
calcular_investimento()
