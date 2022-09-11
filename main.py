from email.mime import image
from fileinput import filename
import smtplib
from email import encoders, message
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server = smtplib.SMTP('smtp.gmail.com',25)

server.ehlo()

with open('password.txt' , 'r') as f:
    password = f.read()

server.login('itisfortestingonly@gmail.com',password)

msg = MIMEMultipart
msg['From']='yeskaydee-using-automation'
msg['To'] = 'email@gmail'
msg['Subject'] = 'Just a test'

with open('message.txt','r') as f:
    message = f.read()

msg.attach(MIMEText(message,'plain'))

filename = 'image.jpeg'
attachement = open(filename, 'rb')

p = MIMEBase('application','octet-stream')
p.set_payload(attachement.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment;filename = {filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('itisfortestingonly@gmail.com','email@gmail',text)
