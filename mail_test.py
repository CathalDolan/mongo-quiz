import os
import smtplib
from flask import Flask
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["EMAIL_ADDRESS"] = os.environ.get("EMAIL_ADDRESS")
app.config["PASSWORD"] = os.environ.get("PASSWORD")
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
PASSWORD = os.environ.get("PASSWORD")

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, PASSWORD)

    subject = "Test Mail"
    body = "This is the test mail body"

    msg = f'subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'cathal@gizagig.com', msg)
