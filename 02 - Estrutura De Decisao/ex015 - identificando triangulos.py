l1 = int(input("Digite o lado 1 do triangulo :"))
l2 = int(input("Digite o lado 2 do triangulo :"))
l3 = int(input("Digite o lado 3 do triangulo :"))

if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
  if l1 == l2 and l1 == l3 and l2 == l3:
    print("Triangulo Equilatero")
  elif l1 == l2 or l1 == l3 and l2 == l3:
    print("Triangulo Isosceles")
  elif l1 != l2 and l1 != l3 and l2 != l3:
    print("Triangulo Escaleno")
else:
  print("Nao e um triangulo")
