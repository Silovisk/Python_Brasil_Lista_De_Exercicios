n1 = float(input("Digite a 1° nota :"))
n2 = float(input("Digite a 2° nota :"))

soma = n1+n2
media = soma/2

if media == 10:
  msg = 'Aprovado_com_Distinçao'
elif media >= 7:
  msg = 'Aprovado'
elif media < 7:
  msg = 'Reprovado'
else:
  print("Invalido")

print("Resultado\n"
      f"{n1} + {n2} = {soma} \n"
      f"{soma} / {2} = {media}\n"
      f"Portanto sua mensagem e {msg}")