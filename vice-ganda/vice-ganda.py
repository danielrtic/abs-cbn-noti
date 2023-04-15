# La funcion de este script es el envio de las ultimas noticias de vice-ganda de abs-cbn news traducidas al español.
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
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

# definir proxy 

n = rd.randint(0, 1)

apiproxy = requests.get(proxy)
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

url = "https://news.abs-cbn.com/list/tag/vice-ganda"

respuesta = requests.get(url, headers = encabezados, proxies = proxies)

soup = BeautifulSoup(respuesta.text, 'html.parser')

lista_de_vice = soup.find_all("section", class_="section-more-stories")

for vice in lista_de_vice:
    vice_ganda = vice.find('p').text
#    pregunta_descripcion = pregunta.find('div', class_="s-post-summary--content-excerpt")
    vice_ganda = vice.text.replace("Read more »", "FIN").replace("12345", "").replace(">","").replace("Last","").replace("ABS-CBN News","").rstrip()
    # .replace(" ", "").replace("\r", "")

# la cuota de deepl se va agotar, hay que buscar implementacion con googletrans o alguna alternativa


# traducir con deep_translator

noticias_traducida = GoogleTranslator(source='auto', target='es').translate(vice_ganda)
noticias_traducida = noticias_traducida.replace("ALETA", "FIN")

# envio de email con las noticias.

mensaje = EmailMessage()

email_subject = "Las noticias de Vice ganda de abs-news" 
sender_email_address = origin 
receiver_email_address = destination 

mensaje['Subject'] = email_subject 
mensaje['From'] = sender_email_address 
mensaje['To'] = receiver_email_address

mensaje.set_content(f"Ultimas noticias de vice ganda (sin traducir): \"{noticias_traducida}\"", subtype="plain")

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