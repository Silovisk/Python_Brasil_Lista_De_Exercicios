n1 = float(input("Digite a 1° nota :"))
n2 = float(input("Digite a 2° nota :"))
n3 = float(input("Digite a 3° nota :"))

m = (n1+n2+n3)/3

print("Media = {:.2f}".format(m))

if m == 10:
  print("Aprovado com Distinção")
elif m < 7:
  print("Reprovado")
elif m >= 7:
  print("Aprovado")
else:
  print("Invalido")

