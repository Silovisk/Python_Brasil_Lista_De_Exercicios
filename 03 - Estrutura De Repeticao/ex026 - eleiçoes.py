"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato. """

n_eleitores = int(input("Digite o total de eleitores :"))

vt_b = 0
vt_l = 0
vt_s = 0
print("[1] - Bolsominion\n"
      "[2] - Luladrao\n"
      "[3] - Saci de Patinete\n")

for i in range(n_eleitores):
  voto = int(input("Digite o seu voto :"))
  if voto == 1:
    print("Voto em Bolsominion computado")
    vt_b = vt_b + 1
  elif voto == 2:
    print("Voto em Luladrao computado")
    vt_l = vt_l + 1
  elif voto == 3:
    print("Voto em Saci de Patinete computado")
    vt_s = vt_s + 1
  else:
    print("invalido")
print(f"\nBolsominion = {vt_b}\n"
      f"Luladrao = {vt_l}\n"
      f"Saci de Patinete = {vt_s}\n")

if vt_b == vt_l and vt_b == vt_s:
  print("2° Turno")
elif vt_b > vt_l and vt_b > vt_s:
  print("Bolsominion ganhou")
elif vt_l > vt_b and vt_l > vt_s:
  print("Luladrao ganhou")
elif vt_s > vt_b and vt_s > vt_l:
  print("Saci de Patinete ganhou")