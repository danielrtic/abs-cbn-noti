# The function of this script is to send the abs-cbn news translated into spanish.
# The script is still to be finished
import requests
from bs4 import BeautifulSoup
from  deep_translator import GoogleTranslator
import smtplib
from email.message import EmailMessage
import json
import os
from cfg import *
import random as rd

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

proxies_list = {"http": "http://"+usuario+":"+contraseña+"@"+servidor+":"+puerto,
           "https": "http://"+usuario+":"+contraseña+"@"+servidor+":"+puerto}




encabezados = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

url = "https://news.abs-cbn.com/news"
url2 = "https://news.abs-cbn.com/news?page=2"

response = requests.get(url, headers = encabezados, proxies = proxies_list)
response2 = requests.get(url2, headers = encabezados, proxies = proxies_list)

soup = BeautifulSoup(response.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')

lista_de_noticias = soup.find_all("section", class_="section-more-stories")
lista_de_noticias2 = soup2.find_all("section", class_="section-more-stories")



for noticia in lista_de_noticias:
    noticias = noticia.find_next('p').text
    #noticias = noticia.text.replace("Read more »", "FIN").replace("12345", "").replace(">","").replace("Last","").replace("ABS-CBN News","").rstrip()
    noticias = noticia.text.split('\n\n')



for noticia2 in lista_de_noticias2:
    noticias2 = noticia2.find_next('p').text
    #noticias2 = noticia2.text.replace("Read more »", "FIN").replace("12345", "").replace(">","").replace("Last","").replace("ABS-CBN News","").rstrip()
    noticias2 = noticia2.text.split('\n\n')

noticias_tradu = []
noticias_tradu2 = []

for prueba in noticias:
    #translate with google and add it to the translated in noticias_tradu
    noticias_traducida = GoogleTranslator(source='auto', target='es', proxies=proxies_list).translate(prueba)
    noticias_traducida = noticias_traducida.replace("Leer más ", "").replace("12345\n>\nÚltimo", "").replace("MÁS HISTORIAS", "").replace("ABS-CBN Noticias", "").replace("Noticias ABS-CBN", "")
    noticias_tradu.append(noticias_traducida)

for prueba2 in noticias2:
    #translate with google and add it to the translated in noticias_tradu2
    noticias_traducida2 = GoogleTranslator(source='auto', target='es').translate(prueba2)
    noticias_traducida2 = noticias_traducida2.replace("Leer más ", "").replace("12345\n>\nÚltimo", "").replace("Primero\n<\n", "").replace("MÁS HISTORIAS", "").replace("»", "").replace("ABS-CBN Noticias", "").replace("Noticias ABS-CBN", "")
    noticias_tradu2.append(noticias_traducida2)

# Convert the "noticias_tradu" list into something more pleasant to read.

open("temp.txt", "x")
with open('temp.txt', 'w') as archivo:
    for elemento in noticias_tradu:
        archivo.write(elemento + '\n')
f = open("temp.txt", "r")
news = f.read()
f.close()

# Convert the "noticias_tradu2" list into something more pleasant to read.

open("temp2.txt", "x")
with open('temp2.txt', 'w') as archivo2:
    for elemento2 in noticias_tradu2:
        archivo2.write(elemento2 + '\n')
f2 = open("temp2.txt", "r")
news2 = f2.read()
f.close()
# Send the email with the news


mensaje = EmailMessage()

email_subject = "Seccion de  noticias de abs-cnb" 
sender_email_address = origin
receiver_email_address = destination

mensaje['Subject'] = email_subject 
mensaje['From'] = sender_email_address 
mensaje['To'] = receiver_email_address

mensaje.set_content(f"Ultimas noticias de abs-cnb news: \"{news}\" \"{news2}\"", subtype="plain")

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

# remove the temp2 file
os.remove("temp2.txt")
