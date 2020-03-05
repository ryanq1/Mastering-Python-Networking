#!/usr/bin/env python3
# Listing 1 - First email client
import smtplib
import getpass

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
def send_email(sender, recipient):
	msg = MIMEMultipart()
	msg['To'] = recipient
	msg['From'] = sender
	msg['Subject'] = input('Enter your email subject: ')
	message = input('Enter your email message.Press Enter when finsihed. ')
	part = MIMEText('text', "plain")
	part.set_payload(message)
	msg.attach(part)
	session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	session.set_debuglevel(1)
	session.ehlo()
	session.starttls()
	session.ehlo()
	password = getpass.getpass(prompt="Enter your email password:")
	session.login(sender, password)
	for x in range(0,5):
		session.sendmail(sender, recipient, msg.as_string())
	print("You email is sent to {0}.".format(recipient))
	session.quit()

if __name__ == '__main__':
	sender = input("Enter sender email address: ")
	recipient = input("Enter recipient email address: ")
	send_email(sender, recipient)
