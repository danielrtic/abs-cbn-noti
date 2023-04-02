# La funcion de este script es el envio de lasnoticias de abs-cbn news traducidas al español.
import requests
from bs4 import BeautifulSoup
from  deep_translator import GoogleTranslator
import smtplib
from email.message import EmailMessage
import json
import pandas as pd
from tabulate import tabulate

# definir proxy 

apiproxy = requests.get("https://api.myprivateproxy.net/v1/fetchProxies/json/full/cu47s8oxdjivgf14to3ey2vywlk2o4u9")
todos = json.loads(apiproxy.text)


servidor = json.dumps(todos[0]['proxy_ip'])
puerto = json.dumps(todos[0]['proxy_port'])
usuario = json.dumps(todos[0]['username'])
contraseña = json.dumps(todos[0]['password'])

servidor = servidor.replace('"','')
puerto = puerto.replace('"','')
usuario = usuario.replace('"','')
contraseña = contraseña.replace('"','')

proxies = {"http": "http://"+usuario+":"+contraseña+"@"+servidor+":"+puerto,
           "https": "http://"+usuario+":"+contraseña+"@"+servidor+":"+puerto}


encabezados = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

url = "https://news.abs-cbn.com/news"
url2 = "https://news.abs-cbn.com/news?page=2"

respuesta = requests.get(url, headers = encabezados, proxies = proxies)
respuesta2 = requests.get(url2, headers = encabezados, proxies = proxies)

soup = BeautifulSoup(respuesta.text, 'html.parser')
soup2 = BeautifulSoup(respuesta2.text, 'html.parser')

#contenedor_de_noticias = soup.find(id="questions")

lista_de_noticias = soup.find_all("div", class_="col-9 content")
lista_de_noticias2 = soup2.find_all("section", class_="section-more-stories")

# crear lista de noticias

new_list = []
new2_list = []

for noticia in lista_de_noticias:
    new_list.append(noticia.text)
    print(new_list)


#    pregunta_descripcion = pregunta.find('div', class_="s-post-summary--content-excerpt")
#    pregunta_descripcion = pregunta_descripcion.text.replace("\n", "").replace("\r", "").strip()
"""
for noticia2 in lista_de_noticias2:
    noticias2 = noticia2.find('p').text
    noticias2 = noticia2.text.replace("Read more »", "FIN").replace("12345", "").replace(">","").replace("Last","").replace("ABS-CBN News","").rstrip()
#    pregunta_descripcion = pregunta.find('div', class_="s-post-summary--content-excerpt")
#    pregunta_descripcion = pregunta_descripcion.text.replace("\n", "").replace("\r", "").strip()

# Traducir con deep_translator
noticias_traducida = GoogleTranslator(source='tl', target='es').translate(noticias) 
noticias_traducida2 = GoogleTranslator(source='tl', target='es').translate(noticias2)
noticias_traducida = noticias_traducida.replace("ALETA", "FIN")
noticias_traducida2 = noticias_traducida2.replace("ALETA", "FIN")
print(noticias_traducida + noticias_traducida2)
# envio de email con las noticias.

mensaje = EmailMessage()

email_subject = "Ultimas noticias abs-cnb" 
sender_email_address = "info@info.informaticaremota.es" 
receiver_email_address = "daniel@informaticaremota.es" 

mensaje['Subject'] = email_subject 
mensaje['From'] = sender_email_address 
mensaje['To'] = receiver_email_address

mensaje.set_content(f"Ultimas noticias de abs-cnb news: \"{noticias_traducida}\" \"{noticias_traducida2}\"", subtype="plain")

email_smtp = "smtp.ionos.es"  
server = smtplib.SMTP(email_smtp, '587')

# Identify this client to the SMTP server 
server.ehlo() 

# Secure the SMTP connection 
server.starttls()

sender_email_address = "info@info.informaticaremota.es" 
email_password = "KJ46xb-LRQ45ca5" 

# Login to email account 
server.login(sender_email_address, email_password) 

# Send email 
server.send_message(mensaje) 

# Close connection to server 
server.quit()
"""