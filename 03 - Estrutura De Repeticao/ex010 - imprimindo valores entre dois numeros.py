n1 = int(input("Digite um numero : "))
n2 = int(input("Digite outro numero : "))

if n1 > n2:
  aux = n2
  n2 = n1
  n1 =aux

while n1 <= n2:
  print(n1)
  n1 += 1
