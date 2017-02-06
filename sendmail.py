import smtplib
from_addr = 'topaz.grant@gmail.com'
to_addr = 'katzlina.kl@gmail.com'
message = """From: {} <{}>
To: {} <{}>
Subject: {}

{}
"""
to_name = 'Kat'
subject = 'Hi'
from_name = 'Topaz'
msg = "where have you been all this time?"
message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)
username = 'topaz.grant@gmail.com'
password = '**** **** **** ****'
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()