#Info/Push notifications, when your medicine reaches the expiry date.
import smtplib 
from email.message import EmailMessage

import pandas as pd

#Creating the email generator. Email recipient is "jasminramonabuerkler@gmail.com"
def email_push(subject, body, to):
     msg = EmailMessage()
     msg.set_content(body)
     msg['subject'] = subject
     msg['to'] = to
     

     user = "jasminramonabuerkler@gmail.com"
     msg['from'] = user
     password = "mabh mcxw sljp deng"

     server = smtplib.SMTP("smtp.gmail.com", 587)
     server.starttls()
     server.login(user, password)
     server.send_message(msg)

     server.quit()

#Creating the content of the email.
if __name__ == '__main__':
    email_push("Expired Medication", "Hi George, your medication expired! Please dispose of it safely and purchase a new one if needed.", "jasminramonabuerkler@gmail.com")