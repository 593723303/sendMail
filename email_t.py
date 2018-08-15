#! C:\python27\
# coding: utf-8
from __future__ import print_function
import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.qq.com'
SMTP_PORT = '25'

def send_mail(user, pwd, to, subject, text):
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject

    try:
        smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        print('connect smtp server success')
        smtp_server.ehlo()
        print('say hello to smpt success')
        smtp_server.starttls()
        smtp_server.login(user, pwd)
        print('login to smtp success')
        smtp_server.sendmail(user, to, msg.as_string())
        print('send mail success')
    except Exception as err:
        print('send email failed:{0}',format(err))
    finally:
        smtp_server.quit()

def main():
    send_mail('xxxxx@qq.com', 'code', 'xxxxxx@qq.com', 'Important', 'text message')

if __name__ == '__main__':
    main()
