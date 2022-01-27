import smtplib
import ssl
import email.message

msg = email.message.Message()
msg['Subject'] = "My Subject"
body = """
Isto é uma mensagem feita por um script em Python. O intuito desse texto é mostrar como as acentuações estão corretas
com a inclusão do utf-8

- Pedro
"""
msg['From'] = '<from_email>'
msg['To'] = '<to_email>'
password = '<password>'
msg.add_header('Content Type', 'text/html')
msg.set_payload(body)
body = """
Subject: Assunto3

This is my message!

- Pedro
"""

ssl_context = ssl.create_default_context()
with smtplib.SMTP('smtp-mail.outlook.com', 587) as connection:
    connection.ehlo()
    connection.starttls(context = ssl_context)
    connection.login(msg['From'], password)
    connection.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
