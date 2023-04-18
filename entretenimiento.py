# The function of this script is to send the latest entertainment news from abs-cbn news translated into spanish.
import requests
from bs4 import BeautifulSoup
import deepl
import smtplib
from email.message import EmailMessage
import json
import random as rd
# Define variables api configuration file .env in root project
from cfg import *

# define proxy 

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

url = "https://news.abs-cbn.com/entertainment"

respuesta = requests.get(url, headers = encabezados, proxies = proxies)

soup = BeautifulSoup(respuesta.text, 'html.parser')

lista_de_noticias = soup.find_all("section", class_="section-more-stories")

for noticia in lista_de_noticias:
    noticias = noticia.find('p').text
    noticias = noticia.text.replace("Read more »", "FIN").replace("12345", "").replace(">","").replace("Last","").replace("ABS-CBN News","").rstrip()

# Translate with deepl
translator = deepl.Translator(API_DEEPL) 
noticias_traducida = translator.translate_text(noticias, target_lang='es') 
enviar_email = print(noticias_traducida)

# sending of email with the news.

mensaje = EmailMessage()

email_subject = "Las noticias de entretenimiento de abs-news" 
sender_email_address = origin 
receiver_email_address = destination 

mensaje['Subject'] = email_subject 
mensaje['From'] = sender_email_address 
mensaje['To'] = receiver_email_address

mensaje.set_content(f"Ultimas noticias: \"{noticias_traducida}\"", subtype="plain")

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
