import smtplib
import os
from email.message import EmailMessage

SYST = os.environ.get('HOMEPATH')
EMAIL_ADRESS = ''
EMAIL_PASS = ''

msg = EmailMessage()
msg['Subject'] = 'USB log'
msg['From'] = EMAIL_ADRESS
msg['To'] = 'jeanbaptistevanparys@gmail.com'
msg.set_content(f'sytem info:{SYST}')

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADRESS, EMAIL_PASS)

    subject = 'usb laatst gelogd'
    
    smtp.send_message(msg)