import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import random


def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Add the message to the body of the email
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Create a secure connection with the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Login to the sender's email account
        server.login(sender_email, sender_password)
        # Send the email
        server.send_message(msg)
        print("Email sent successfully")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))
    finally:
        # Close the connection to the SMTP server
        server.quit()


# Example usage
def sendMail(recipient_email):
    otp = str(random.randint(100000, 999999))
    sender_email = 'abzxy50312@gmail.com'
    sender_password = 'qtkydmevnsipgzoj'
    subject = 'OTP for ChatBot'
    message = 'Your OTP is '+otp
    print("Sending...")
    send_email(sender_email, sender_password, recipient_email, subject, message)
    return otp
# sendMail("dhruv20345@gmail.com")
