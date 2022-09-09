"""Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

    Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário. 
  
  """
salario_inicial = float(input("Digite o salario inicial :"))
ano_inicial = int(input("Ano inicial :"))
ano_final = int(input("Ano final :"))
aumento = 1.5 / 100

while ano_inicial <= ano_final:
  salario_atual = salario_inicial + (salario_inicial * aumento)
  print(f"Seu salario em {ano_inicial} = {salario_atual:.2f} com o aumento de {aumento:.3f}")
  aumento = aumento * 2
  ano_inicial += 1
print(f"Seu salario em {ano_final} = {salario_atual:.2f}")