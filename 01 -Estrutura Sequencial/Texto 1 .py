import requests

url = "https://wiki.python.org.br/EstruturaSequencial"

# fazer uma solicitação HTTP ao URL do link e obter seu conteúdo
response = requests.get(url)
content = response.text

# escrever o conteúdo no arquivo README.md
with open("README.md", "w") as f:
    f.write(content)
