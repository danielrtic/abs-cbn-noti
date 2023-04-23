# The function of this script is to send the latest vice-ganda news from abs-cbn news translated into spanish.
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import smtplib
from email.message import EmailMessage
import json
import random as rd
# Define variables api configuration file .env in root project
from cfg import *
import os

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

url = "https://news.abs-cbn.com/list/tag/vice-ganda"

respuesta = requests.get(url, headers = encabezados, proxies = proxies)

soup = BeautifulSoup(respuesta.text, 'html.parser')

lista_de_vice = soup.find_all("section", class_="section-more-stories")

for vice in lista_de_vice:
    vice_ganda = vice.find('p').text
    vice_ganda = vice.text.replace("Read more »", "FIN").replace("Last","").replace("ABS-CBN News","").rstrip().replace("''", "").replace("\xa0", "").replace("\t", "").replace("\r", "").split('\n\n')
    
noticias_tradu = []

for prueba in vice_ganda:
    #translate with google and add it to the translated in noticias traducidas
    noticias_traducida = GoogleTranslator(source='auto', target='es').translate(prueba)
    noticias_traducida = noticias_traducida.replace("12345", "").replace(">","").replace("Último","").replace("ALETA","FIN")
    noticias_tradu.append(noticias_traducida)
# Convert the "noticias_tradu" list into something more pleasant to read.

open("temp.txt", "x")
with open('temp.txt', 'w') as archivo:
    for elemento in noticias_tradu:
        archivo.write(elemento + '\n')
f = open("temp.txt", "r")
news = f.read()
f.close()
print(news)

# sending of email with the news.

mensaje = EmailMessage()

email_subject = "Las noticias de Vice ganda de abs-news" 
sender_email_address = origin 
receiver_email_address = destination 

mensaje['Subject'] = email_subject 
mensaje['From'] = sender_email_address 
mensaje['To'] = receiver_email_address

mensaje.set_content(f"Ultimas noticias de vice ganda (traducido): \"{news}\"", subtype="plain")

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
# remove the temp file
os.remove("temp.txt")
