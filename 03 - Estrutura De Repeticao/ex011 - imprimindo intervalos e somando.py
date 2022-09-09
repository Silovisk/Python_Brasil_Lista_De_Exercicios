n1 = int(input("Digite um numero : "))
n2 = int(input("Digite outro numero : "))

soma = 0

if n1 > n2:
  aux = n2
  n2 = n1
  n1 =aux

while n1 <= n2:
  print(n1)
  soma += n1
  n1 += 1
print(soma)