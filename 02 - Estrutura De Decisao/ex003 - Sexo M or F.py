sexo = input("Digite seu sexo :\n[F]-Feminino\n[M]-Masculino\n ")

if sexo == 'F' or sexo == 'f':
  print(F"Sexo informado e {sexo}-Feminino")
elif sexo == 'M' or sexo == 'm':
  print(F"Sexo informado e {sexo}-Masculino")
else:
  print(f"sexo {sexo}-Invalido")