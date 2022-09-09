"""Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um. """
cont = 1
soma = 0
qtd = int(input("Digite a Qtd de CDs :"))
while cont <= qtd:
  val = float(input(f"Valor do {cont}° CD = R$"))
  soma = soma + val
  cont += 1
med = soma / qtd
print(f"Valor medio e = R${med:.2f}")