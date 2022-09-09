gabarito_prova = ["A","B","C","D","E","E","D","C","B","A"]
todos_pontos = []
soma_pontos = ponto = cont_aluno = 0
resp = True
while resp:
    aluno = str(input("Digite seu nome: "))

    for i in range(len(gabarito_prova)):
        resposta = (str(input(f"Resposta da {i+1}° Questao :")))

        if (resposta == gabarito_prova[i]):
            ponto += 1

    todos_pontos.append(ponto)

    cont_aluno += 1    
    soma_pontos = ponto = 0
    resp = input("Ira utilizar o programa novamente [y/n] :")
    resp = True if resp == 'y' else False

print(end="-" *30)
print(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=- TABELA =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Maior acerto:       {max(todos_pontos)}
Menor acerto:       {min(todos_pontos)}
Total de alunos:    {cont_aluno}
Media das notas:    {sum(todos_pontos)/len(todos_pontos)}

=-=-=-=-=-=-=-=-=-=-=-= FIM =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""")


