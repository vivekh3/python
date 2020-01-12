import smtplib

#import config


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login("vivekscratch@gmail.com","Vishnu303!" )
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail("vivekscratch@gmail.com", "vivek.hari79@gmail.com", message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "Test subject"
msg = "Hello there, how are you today?"

send_email(subject, msg)
