import requests
from bs4 import BeautifulSoup

url = "https://wiki.python.org.br/ExerciciosArquivos"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

with open("README.md", "w", encoding="utf-8") as file:
    file.write(soup.prettify())
