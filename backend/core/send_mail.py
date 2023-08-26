import smtplib
from email.mime.text import MIMEText


class SendMail:
    def __init__(
            self, host, port, email_address_from, email_password, email_address_to, message
    ):

        self.host = host
        self.port = port
        self.email_address_from = email_address_from
        self.email_password = email_password
        self.email_address_to = email_address_to
        self.message = message

    def send_email(self):
        try:
            message = MIMEText(self.message, 'plain', 'utf-8')

            server = smtplib.SMTP(f'{self.host}:{self.port}')
            server.starttls()
            server.login(self.email_address_from, self.email_password)
            server.sendmail(self.email_address_from, self.email_address_to, message.as_string())
            server.quit()
            return 'Message send successful'
        except:
            return 'An error occurred while sending the message'
