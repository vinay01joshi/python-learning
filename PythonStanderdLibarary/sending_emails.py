from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

message = MIMEMultipart()
message["from"] = "Vinay Joshi"
message["to"] = "info@vinjo.ml"
message["subject"] = "This is the test Email"
message.attach(MIMEText("Body"))
message.attach(Path("Vinay Joshi.jpg").read_bytes())

with smtplib.SMTP(host="smtp.gmail.com", port=465) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("user_name", "password")
    smtp.send_message(message)
    print("Email Sent")
