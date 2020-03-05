import os
import getpass
import re
import sys
import smtplib

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def send_email(sender, recipient):
	msg = MIMEMultipart()
	msg['To'] = recipient
	msg['From'] = sender
	subject = input('Enter your email subject: ')
	msg['Subject'] = subject
	message = input('Enter your email message. Press Enter whe\
	finished. ')
	part = MIMEText('text', "plain")
	part.set_payload(message)
	msg.attach(part)
	filename = input('Enter the file name of a GIF image: ')
	path = os.path.join(os.getcwd(), filename)
	if os.path.exists(path):
		img = MIMEImage(open(path, 'rb').read(), _subtype = "gif")
		img.add_header('Content-Disposition', 'attachment',
		filename = filename)
		msg.attach(img)
	session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	session.ehlo()
	session.starttls()
	session.ehlo
	password = getpass.getpass(prompt="Enter your email password: ")
	session.login(sender, password)
	session.sendmail(sender, recipient, msg.as_string())
	print("You email is sent to {0}.".format(recipient))
	session.quit()

if __name__ == '__main__':
	sender = input("Enter sender email address: ")
	recipient = input("Enter recipient email address: ")
	send_email(sender, recipient)
	
