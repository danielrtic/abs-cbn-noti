import requests
from bs4 import BeautifulSoup
import deepl

encabezados = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

url = "https://news.abs-cbn.com/entertainment"

respuesta = requests.get(url, headers = encabezados)

soup = BeautifulSoup(respuesta.text, 'html.parser')

#contenedor_de_noticias = soup.find(id="questions")

lista_de_noticias = soup.find_all("div", id="latest-news")

for noticia in lista_de_noticias:
    noticia_titulo = noticia.find('ul').text
#    pregunta_descripcion = pregunta.find('div', class_="s-post-summary--content-excerpt")
#    pregunta_descripcion = pregunta_descripcion.text.replace("\n", "").replace("\r", "").strip()

# Traducir con deepl
translator = deepl.Translator('1fed4bf3-24eb-d961-cb9a-09414bedeb3a:fx') 
titulo_traducido = translator.translate_text(noticia_titulo, target_lang='es') 
print(titulo_traducido)
#print(pregunta_descripcion)
print()