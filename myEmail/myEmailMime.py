import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config
import email.utils

fromaddr = config.fromaddr
toaddr = config.toaddr
msg = MIMEMultipart()
msg['Subject'] = "Hello from Mustapha am having a great time!!!!"
msg['To'] = email.utils.formataddr(('Recipient', toaddr))
msg['From'] = email.utils.formataddr(('Mustapha',fromaddr))
body = "What a wonderful world!"
msgBody = MIMEText(body, 'plain')
msg.attach(msgBody)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls() #encrypt the msg
server.login(fromaddr, config.password)
text = msg.as_string()
print("Text is:", text)
server.sendmail(fromaddr, toaddr, text)
server.quit()