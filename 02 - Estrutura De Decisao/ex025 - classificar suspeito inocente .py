print("Responde as perguntas abaixo com S ou N:>\n========================================")
p1 = input("Telefonou para a vítima ? ")
p2 = input("Esteve no local do crime ? ")
p3 = input("Mora perto da vítima ? ")
p4 = input("Devia para a vítima ? ")
p5 = input("Já trabalhou com a vítima ? ")

op = 0
if p1.upper() == 'S':
  op = op + 1
if p2.upper() == 'S':
  op = op + 1
if p3.upper() == 'S':
  op = op + 1
if p4.upper() == 'S':
  op = op + 1
if p5.upper() == 'S':
  op = op + 1

print(op)
if op == 2:
  print("Suspeita")
elif op >=3 and op <= 4:
  print("Cumplice")
elif op == 5:
  print("Assasino") 
else:
  print("Inocente")