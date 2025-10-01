#Vitoria Bezerra Lopes
#Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média: Se a média for >= 6,0 exibir “APROVADO”; Se a média for >= 3,0 E < 6,0 exibir “EXAME”; Se a média for < 3,0 exibir “RETIDO”.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Diite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1+nota2+nota3+nota4)/4

if media >=6:
  print('Aprovado')
elif media >=3:
  print('Exame')
else:
  print('Retido')
  
  
