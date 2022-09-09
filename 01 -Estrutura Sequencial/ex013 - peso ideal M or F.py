h = float(input("Digite sua altura :"))
sexo = input("Digite seu sexo M ou F :")

if (sexo == 'M' or sexo == 'm'):
  peso_ideal =  (72.7*h) - 58
else:
  peso_ideal = (62.1*h) - 44.7

print(f"Com base na sua altura {h} e sexo {sexo} seu peso ideal e {peso_ideal}")