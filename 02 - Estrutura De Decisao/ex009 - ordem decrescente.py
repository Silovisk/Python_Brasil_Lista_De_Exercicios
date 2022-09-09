n1 = int(input("Digite o 1° numero :"))
n2 = int(input("Digite o 2° numero :"))
n3 = int(input("Digite o 3° numero :"))

if n1 < n3:
  n1, n3 = n3, n1
if n1 < n2:
  n1, n2 = n2, n1
if n2 < n3:
  n2, n3 = n3, n2

print(f'A ordem decrescente é {n1}, {n2} e {n3}')