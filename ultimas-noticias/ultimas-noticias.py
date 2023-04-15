# The function of this script is to send the latest news from abs-cbn news translated into spanish.
import requests
from bs4 import BeautifulSoup
import deepl
import smtplib
from email.message import EmailMessage
import json
import random as rd
from dotenv import load_dotenv
import os

# Define variables api configuration file config.env

root_file = os.getcwd()
config_file = os.path.join(root_file, 'config.env')

load_dotenv(config_file)

proxy = os.getenv("proxy")

# email config variables

origin = os.getenv("origin")
destination = os.getenv("destination")
password = os.getenv("password")
smtp = os.getenv("smtp")

# api key deepl

API_DEEPL = os.getenv("API_DEEPL")

# define proxy

n = rd.randint(0, 1)

apiproxy = requests.get("https://api.myprivateproxy.net/v1/fetchProxies/json/full/cu47s8oxdjivgf14to3ey2vywlk2o4u9")
todos = json.loads(apiproxy.text)


servidor = json.dumps(todos[n]['proxy_ip'])
puerto = json.dumps(todos[n]['proxy_port'])
usuario = json.dumps(todos[n]['username'])
contraseña = json.dumps(todos[n]['password'])

servidor = servidor.replace('"','')
puerto = puerto.replace('"','')
usuario = usuario.replace('"','')
contraseña = contraseña.replace('"','')

proxies = {"http": "http://"+usuario+":"+contraseña+"@"+servidor+":"+puerto,
           "https": "http://"+usuario+":"+contraseña+"@"+servidor+":"+puerto}


encabezados = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

url = "https://news.abs-cbn.com/entertainment"

respuesta = requests.get(url, headers = encabezados, proxies = proxies)

soup = BeautifulSoup(respuesta.text, 'html.parser')

#contenedor_de_noticias = soup.find(id="questions")

lista_de_noticias = soup.find_all("div", id="latest-news")

for noticia in lista_de_noticias:
    noticia_titulo = noticia.find('ul').text
#    pregunta_descripcion = pregunta.find('div', class_="s-post-summary--content-excerpt")
#    pregunta_descripcion = pregunta_descripcion.text.replace("\n", "").replace("\r", "").strip()

# Traducir con deepl
translator = deepl.Translator(API_DEEPL) 
titulo_traducido = translator.translate_text(noticia_titulo, target_lang='es') 
enviar_email = print(titulo_traducido)
print(titulo_traducido)
#print(pregunta_descripcion)
print(enviar_email)

# sending of email with the news.

mensaje = EmailMessage()

email_subject = "Ultimas noticias abs-cnb" 
sender_email_address = origin 
receiver_email_address = destination 

mensaje['Subject'] = email_subject 
mensaje['From'] = sender_email_address 
mensaje['To'] = receiver_email_address

mensaje.set_content(f"Ultimas noticias de abs-cnb news: \"{titulo_traducido}\"", subtype="plain")

email_smtp = smtp  
server = smtplib.SMTP(email_smtp, '587')

# Identify this client to the SMTP server 
server.ehlo() 

# Secure the SMTP connection 
server.starttls()

sender_email_address = origin
email_password = password 

# Login to email account 
server.login(sender_email_address, email_password) 

# Send email 
server.send_message(mensaje) 

# Close connection to server 
server.quit()