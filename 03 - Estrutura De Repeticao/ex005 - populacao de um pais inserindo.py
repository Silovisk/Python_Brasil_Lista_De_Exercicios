habitantes_a = int(input("informe a Quantidade de habitantes do pais 'A': "))
habitantes_b = int(input("informe a Quantidade de habitantes do pais 'B': "))
taxa_pais_a = float(input("informe a taxa do pais 'A': "))
taxa_pais_b = float(input("informe a taxa do pais 'B': "))

ano = 0

while habitantes_a <= habitantes_b:
    habitantes_a += habitantes_a * taxa_pais_a
    habitantes_b += habitantes_b * taxa_pais_b
    ano += 1

print(f"O pais 'A' Ultrapassa ou iguale a populaçao do pais 'B' em {ano} anos")