import pandas as pd 

def formatar_data(data):
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

    try:
        if data[2] == "/" and data[5] == "/" and len(data) == 10:

            dia, mes, ano = map(int, data.split('/'))

            return f"{dia} de {meses[int(mes)-1].capitalize()} de {ano}"
        else:
            return "NULL Data Invalida"
    except:
            return "NULL Data Invalida"

# Lendo tabela
df = pd.read_excel("Planilhas pra testes\datas.xlsx")

# Excluindo coluna lista
df = df.drop('Lista', axis=1)

# Transformando coluna em formato de data e depois alterando formataçao
df['Datas'] = pd.to_datetime(df['Datas'])
df['Datas'] = df['Datas'].dt.strftime(r'%d/%m/%Y')

'''
data = input("Informe uma data no seguinte formato: DD/MM/AAAA: ")

formatar_data(data)
'''

for index, row in df.iterrows():
    print(f"{formatar_data(row['Datas'])}")

