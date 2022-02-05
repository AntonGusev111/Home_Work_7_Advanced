import email
import smtplib
import imaplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



class g_mail:

    def __init__(self):
        self.gmail_smtp = 'smtp.gmail.com'
        self.gmail_imap = 'imap.gmail.com'
        self.login = self.upload_vars('login')
        self.password = self.upload_vars('password')
        self.check_vars()

    def check_vars(self):
        if self.login == '':
            self.vars_writing('login')
            self.login = self.upload_vars('login')
        if self.password == '':
            self.vars_writing('password')
            self.password = self.upload_vars('password')

    def upload_vars(self,aut):
        f = open(f'{aut}.txt')
        return f.read()

    def vars_writing(self, aut):
        value = input(f'Введите ваш {aut}: ')
        with open(f'{aut}.txt', 'w') as file:
            file.write(value)
            file.close()


    def send(self, recipients, message, subject=None):
        self.message = message
        self.subject = subject
        self.recipients = recipients
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))
        msg = msg.as_string()
        ms = smtplib.SMTP(self.gmail_smtp, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, self.recipients, msg)
        ms.quit()


    def recieve(self, header=None):
        self.header = header
        mail = imaplib.IMAP4_SSL(self.gmail_imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = str(data[0][1])
        email_message = email.message_from_string(raw_email)
        return email_message
        mail.logout()


if __name__ == '__main__':
    gmail = g_mail()
    gmail.send([f'{input("input recipients: ")}'],f'{input("input message: ")}', f'{input("input subject: ")}')
    gmail.recieve()