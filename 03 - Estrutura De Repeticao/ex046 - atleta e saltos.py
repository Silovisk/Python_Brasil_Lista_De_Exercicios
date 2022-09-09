posicao = ["Primeiro","Segundo","Terceiro","Quarto","Quinto"]
saltos = []
atleta = str(input("Digite o nome do atleta :"))

for i in range(len(posicao)):
    saltos.append(float(input(f"{posicao[i]} salto :")))


melhor_salto = max(saltos)
pior_salto = min(saltos)
media_demais_saltos = sum(saltos)/len(saltos)
#Removendo maior e menor valor da lista de saltos
del(saltos[(saltos.index(melhor_salto))])
del(saltos[(saltos.index(pior_salto))])

print(f"""

Melhor Salto:            {melhor_salto}
Pior Salto:              {pior_salto}  
Media dos demais Saltos: {media_demais_saltos:.1f}

Resultado Final:
{atleta}: {media_demais_saltos}

""")