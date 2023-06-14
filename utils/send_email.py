import smtplib
import os


def send(body, subject):
    print(os.environ)
    sender_email = os.environ.get('PROD_SEND_EMAIL_ID')
    port = os.environ.get('PROD_SERVER_PORT')
    smtp_server = os.environ.get('PROD_SMTP_SERVER')
    receiver_emails = [os.environ.get('PROD_RECEIVER_EMAIL_1')]

    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sender_email, receiver_emails, subject, body)

    try:
        print(smtp_server, port, sender_email, receiver_emails, email_text)
        server = smtplib.SMTP(smtp_server, 25)
        server.connect(smtp_server, port)
        server.ehlo()
        server.sendmail(sender_email, receiver_emails, email_text)
        server.quit()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong while sending mail….", ex)

# send('test body', 'test subject for tushar')
