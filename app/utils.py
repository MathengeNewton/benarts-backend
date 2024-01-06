import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(recipient_email:str):
    try:
        subject = 'Your Subject'
        body = 'Your email body'
        SMTP_SERVER=os.getenv('SMTP_SERVER')
        SMTP_USERNAME=os.getenv('SMTP_USERNAME')
        SMTP_PASSWORD=os.getenv('SMTP_PASSWORD')
        SMTP_PORT=os.getenv('SMTP_PORT')
        SMTP_MAIL_FROM=os.getenv('SMTP_MAIL_FROM')

        # Create a MIME object to represent the email
        message = MIMEMultipart()
        message['From'] = SMTP_MAIL_FROM
        message['To'] = recipient_email
        message['Subject'] = subject

        # Attach the body of the email
        message.attach(MIMEText(body, 'plain'))

        # Connect to the Amazon SES SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable TLS encryption
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_MAIL_FROM, recipient_email, message.as_string())
        
        return True
    except Exception as e:
        print("error: ",e)
        return False

