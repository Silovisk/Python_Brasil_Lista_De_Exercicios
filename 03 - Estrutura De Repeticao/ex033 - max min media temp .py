"""O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas. """


qtd_temp = int(input("Digite a qtd de temperatura a informar :"))
soma = 0
temps = []

for i in range(qtd_temp): 
  temp = temps.append(float(input(f"Digite a temperatura {i+1}° :")))

print(f"A maior temperatura ",max(temps))
print(f"A menor temperatura ",min(temps))
print(f"A media da temperatura",round(sum(temps)/qtd_temp,2))
