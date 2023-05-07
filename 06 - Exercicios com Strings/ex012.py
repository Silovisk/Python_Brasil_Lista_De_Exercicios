
telefone = str(input("Informe um numero de telefone: "))

print(f"Telefone: {telefone}")

if len(telefone) == 7:
    print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")
    telefone = '3' + telefone

telefone_formatado = f"{telefone[0:4]}-{telefone[4:8]}"

print(f"""
Telefone corrigido sem formatação: {telefone}
Telefone corrigido com formatação: {telefone_formatado}
""")