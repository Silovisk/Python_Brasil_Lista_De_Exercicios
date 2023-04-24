def compara_tamanho(tamanho_str1, tamanho_str2):
    return "Possuem o mesmo comprimento" if tamanho_str1 == tamanho_str2 else "Não possuem o mesmo comprimento"
        
def mesmo_conteudo(str1, str2):
    return "Possuem o mesmo conteudo" if str1 == str2 else "Não possuem o mesmo conteudo"

string1 = str(input("Informe a 1° String: "))
string2 = str(input("Informe a 2° String: "))

tamanho_str1 = len(string1)
tamanho_str2 = len(string2)

comprimento_das_strings = compara_tamanho(tamanho_str1, tamanho_str2)
conteudo_das_strings = mesmo_conteudo(string1, string2)

print(f"""
Tamanho de string1 {string1}: {tamanho_str1}
Tamanho de string2 {string2}: {tamanho_str2}

{comprimento_das_strings}

{conteudo_das_strings}
""")

 