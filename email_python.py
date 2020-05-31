#!/usr/bin/env python3
from email.message import EmailMessage
import os.path
import mimetypes
import smtplib
import getpass


message = EmailMessage()
mail_server = smtplib.SMTP('localhost')

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
message['From'] = sender
message['To'] = recipient

message['Subject'] = " Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
message.set_content(body)

attachment_path = "processed.pdf"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)
with open(attachment_path, 'rb') as ap:
	message.add_attachment(ap.read(),maintype=mime_type,subtype=mime_subtype,filename=os.path.basename(attachment_path))


mail_server.send_message(message)

