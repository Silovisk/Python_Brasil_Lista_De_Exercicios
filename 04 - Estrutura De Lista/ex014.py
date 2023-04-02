perguntas = [
    'Telefonou para a vitima?',
    'Esteve no local do crime?',
    'Mora perto da vitima?',
    'Devia para a vitima?',
    'Ja trabalhou com a vitima?']

suspeito = 0

def verificar_suspeito(numero_positivas):
    if numero_positivas == 2:
        classificacao = "Suspeita"
    elif numero_positivas >= 3 and numero_positivas <= 4:
        classificacao = "Complice"
    elif numero_positivas == 5:
        classificacao = "Assassino"
    else:
        classificacao = "Inocente"
    
    return classificacao


print("""
--- Questionario de investigaçao ---
Reponda [S] para Sim e [N] Para Nao
""")
for p in perguntas:
    print(p)
    resposta = str(input("Responda: "))
    if resposta == "S":
        suspeito += 1

print(f"""
--- Classificaçao --- 

Resultado: {verificar_suspeito(suspeito)}
""")