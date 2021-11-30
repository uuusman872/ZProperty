from django.core.mail import EmailMessage

def sendEmail(msg):
    email_Subject = "Please activate your account"
    message = str(msg)
    to_email = "uuusman872@gmail.com"
    send_email = EmailMessage(email_Subject, message, to=[to_email])
    send_email.send()
