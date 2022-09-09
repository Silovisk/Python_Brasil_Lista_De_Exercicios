habitantes_a = 80000
habitantes_b = 200000
ano = 0

while habitantes_a <= habitantes_b:
    habitantes_a += habitantes_a * 0.03
    habitantes_b += habitantes_b * 0.015
    ano += 1

print(f"O pais 'A' Ultrapassa ou iguale a populaçao do pais 'B' em {ano} anos")