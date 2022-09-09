nome = input("Digite um nome :")
idade = int(input('Digite idade entre 0 e 150 :'))
salario = float(input('Digite o salario maior que 0 :'))
sexo = input("Digite sexo [M] or [F] :")
estado_civil = input("Digite seu estao civil s,c,v ou d :")

if nome > '   ':
  print('Nome valido')
else : 
  print('Nome invalido')

if idade > 0 and idade < 150:
  print("Idade valida")
else:
  print("Idade invalida")

if salario > 0:
  print("Salario valido")
else:
  print("Salario invalido")
  
if sexo != 'm' and sexo != 'f':
  print("Sexo invalido")
else:
  print("Sexo invalido")

if estado_civil == 's' or 'c' or 'v' or 'd':
  print('Estado civil valido')
else:
  print('Estado civil Invalido')