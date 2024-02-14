import smtplib
from email.mime.text import MIMEText

smtp = smtplib.SMTP('smtp.live.com', 465)
smtp.ehlo()
smtp.starttls()
smtp.login('lee@live.com', 'password')

# SMTP Server

msg = MIMEText('test')
msg['Subject'] = 'Test'
msg['To'] = 'whjung@cubox.aero'
smtp.sendmail('lee@live.com', 'whjung@cubox.aero', msg.as_string())

smtp.quit()