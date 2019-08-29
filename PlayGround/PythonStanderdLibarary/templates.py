from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib


template = Template(Path("PythonStanderdLibarary/templates.html").read_text())


message = MIMEMultipart()
message["from"] = "Vinay Joshi"
message["to"] = "vinay.joshi.ngi@gmail.com"
message["subject"] = "This is the test Email"
body = template.substitute({"name": "Vinay Joshi"})
message.attach(MIMEText(body, "html"))
message.attach(Path("PythonStanderdLibarary/VinayJoshi.jpg").read_bytes())

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("vinay001joshi@gmail.com", "VINAY01JOSHI")
    smtp.send_message(message)
    print("Email Sent")
