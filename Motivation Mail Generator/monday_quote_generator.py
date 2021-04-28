from smtplib import SMTP
import datetime as dt
import random

now=dt.datetime.now()
today=now.weekday()

MY_MAIL='         '
MY_PASSWORD='    '

if today==5:
    with open("quotes.txt", "r") as quote_text:
        lines = quote_text.readlines()
        line=random.choice(lines)
        print(line)

        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_MAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_MAIL, to_addrs='shubhrijana@gmail.com',
                                msg=line)
            print('Mail Sent')
