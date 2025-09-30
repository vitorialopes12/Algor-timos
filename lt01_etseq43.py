#Vitoria Bezerra Lopes
#Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 m e cresce 2 cm ao ano.

ana_altura = 1.10
ana_crescimento = .03

maria_altura = 1.5
maria_crescimento = .02

anos = 0

while maria_altura>ana_altura:
  anos+=1
  ana_altura+=ana_crescimento
  maria_altura+=maria_crescimento

print(f'Sao necessarios {anos} anos para que Ana seja maior que Maria')
print(f'Altura de Ana; {ana_altura:.2f}')
print(f'Altura de Maria: {maria_altura:.2f}')
