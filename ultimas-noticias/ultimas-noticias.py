import requests
from bs4 import BeautifulSoup
import deepl
import smtplib
from email.message import EmailMessage

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
enviar_email = print(titulo_traducido)
print(titulo_traducido)
#print(pregunta_descripcion)
print(enviar_email)

# envio de email con las noticias.

mensaje = EmailMessage()

email_subject = "Ultimas noticias abs-cnb" 
sender_email_address = "info@info.informaticaremota.es" 
receiver_email_address = "daniel@informaticaremota.es" 

mensaje['Subject'] = email_subject 
mensaje['From'] = sender_email_address 
mensaje['To'] = receiver_email_address

mensaje.set_content(f"Ultimas noticias de abs-cnb news: \{titulo_traducido}\", subtype="plain")

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