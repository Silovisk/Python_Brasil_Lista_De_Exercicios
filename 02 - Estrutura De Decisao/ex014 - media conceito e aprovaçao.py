n1 = float(input("1° nota :"))
n2 = float(input("2° nota :"))

media = n1+n2/2

if media >= 9 and media <= 10:
  conceito = "A"
elif media >= 7.5 and media < 9:
  conceito = "B"
elif media >= 6 and media < 7.5:
  conceito = "C"
elif media >= 4 and media < 6:
  conceito = "D"
elif media < 4 and media >= 0:
  conceito = "E"
else:
  print("Invalido")

print("Conceito =",conceito)

if conceito == "A" or conceito == "B" or conceito == "C":
  print("Aprovado!")
elif conceito == "D" or conceito == "E":
  print("Reprovado!")
