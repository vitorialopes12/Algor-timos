#Vitoria Bezerra Lopes
#Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto – desconto). A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber.

def calcular_salario():
  horas_trabalhadas = int(input('Digite o número de horas trabalhadas: '))
  valor_hora = float(input('Digite o valor por hora: R$'))
  desconto = float(input('Digite o percentual de desconto (apenas número): '))/100
  numero_dependentes = int(input('Digite o número de dependentes: '))

salario = horas_trabalhadas*valor_hora
salario_liquido = (salario-(salario*desconto)) + (100*numero_dependentes)

print(f'O salário a receber é de R${salario_liquido})
