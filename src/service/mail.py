from src.static.message import ERROR_MESSAGE
from src.service.template import ViewTemplate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from email.mime.image import MIMEImage

import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_SERVER = os.getenv("EMAIL_SERVER")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))


view_template = ViewTemplate()


class Mail:
    def send_mail(self, login_user, name_user, email_to, template_path):
        body_template = view_template.message(login_user, name_user, template_path)
        message = MIMEMultipart()
        message["from"] = "Admin Backend"
        message["to"] = email_to
        message["subject"] = "Assunto Liga da Justiça"

        body = MIMEText(body_template, "html")
        message.attach(body)
        with smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT) as smtp:
            try:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(EMAIL_SERVER, PASSWORD)
                smtp.send_message(message)
            
            except Exception as error:
                print(ERROR_MESSAGE.format(error))
