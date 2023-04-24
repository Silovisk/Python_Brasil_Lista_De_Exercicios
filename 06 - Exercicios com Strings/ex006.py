meses = [
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
]

data_nascimento = input("Informe sua Data de nascimento (dd/mm/aaaa) :")

dia, mes, ano = map(int, data_nascimento.split("/"))
print(f"""
Data de Nascimento: {data_nascimento}    

Voce nasceu em {dia} de {meses[mes-1]} de {ano}
""")
