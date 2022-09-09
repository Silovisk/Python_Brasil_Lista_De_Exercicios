nome = input("Digite seu nome :")
turno = input(f"Olá,{nome}, Qual turno voce estuda :\n"
              "M-Matutino\n"
              "V-Vespertino\n"
              "N-Noturno\n")
            
if turno == 'M' or turno == 'm':
  print(f"Bom Dia!,{nome}")
elif turno == 'V' or turno == 'v':
  print(f"Boa Tarde!,{nome}")
elif turno == 'N' or turno == 'n':
  print(f"Boa Noite!,{nome}")
else:
  print("Valor Inválido!")