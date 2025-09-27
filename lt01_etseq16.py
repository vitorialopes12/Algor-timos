#Vitoria Bezerra Lopes
#Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. Calcule o salário que serao as horas trabalhadas x o valor por hora. Calcule o salário liquído. A cada dependente será acrescido R$100 no salário. Exiba o salário a receber

horas_trabalhadas = float(input('Digite o valor de horas trabalhadas:'))
valor_hora = float(input('Digite o valor por hora: R$ '))
desconto = float(input('Digite o percentual de desconto: '))/100
num_dependentes = float(input('Digite o número de dependentes: '))
salario = horas_trabalhadas*valor_hora 
salario_liquido = (salario-(salario*desconto)) + (100*num_dependentes)

print(f'O salário a receber é de: R${salario_liquido}')
