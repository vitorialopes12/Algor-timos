#Vitoria Bezerra Lopes
#Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos.

ano_nasc = int(input('Digite seu ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))

idade = ano_atual-ano_nasc
idade_futura = idade_atual+17

print(f'Sua idade atual é: {idade}')
print(f'Sua idade daqui 17 anos será: {idade+17}')
