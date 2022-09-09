tot_votos = votos_1 = votos_2 = votos_3 = votos_4 = votos_5 = votos_6 = 0


resp = True
while resp == True:
    for i in range(resp):
        votos = int(input("""
        Informe o Numero do seu voto 
        1 - Bolsonaro
        2 - Lula
        3 - Simone
        4 - Simaria
        5 - Voto Nulo
        6 - Voto em Branco
        Informe: 
        """))   

    if(votos == 1):
        votos_1 += 1
    elif(votos == 2):
        votos_2 += 1
    elif(votos == 3):
        votos_3 += 1
    elif(votos == 4):
        votos_4 += 1
    elif(votos == 5):
        votos_5 += 1
    elif(votos == 6):
        votos_6 += 1
    else:
        print("Numero invalido!!")
    
    

    resp = input("Deseja votar novamente:  [y/n] :")
    resp = True if resp == "y" else False

tot_votos = votos_1 + votos_2 + votos_3 + votos_4 + votos_5 + votos_6 

porcent_tot_nulos = votos_5/tot_votos
porcent_tot_branc = votos_6/tot_votos

print(f""" 
------------ TABELA CANDIDATOS ------------

1 - Bolsonaro               {votos_1}
2 - Lula                    {votos_2}
3 - Simone                  {votos_3}
4 - Simaria                 {votos_4}
5 - Voto Nulo               {votos_5}
6 - Voto em Branco          {votos_6}

Total de votos              {tot_votos}
---------------- PORCENTAGENS ------------

1 - Porcentagem sobre votos nulos   {porcent_tot_nulos:.2f}%
2 - Porcentagem sobre votos Brancos {porcent_tot_branc:.2f}%
""")