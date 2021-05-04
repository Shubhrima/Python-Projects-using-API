import lxml
from bs4 import BeautifulSoup
import requests
from unidecode import unidecode
from smtplib import SMTP

WEBSITE = "https://www.amazon.in/24x7-eMall-Comfortable-Blindfold-Eyes/dp/B07BK86MW3/ref=sr_1_8?crid=3T8NJV6KI32X7&dchild=1&keywords=eyepads+for+sleep&qid=1620086477&sprefix=eyep%2Caps%2C362&sr=8-8"
HEADER={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51",
    "Accept-Language" : "en-US,en;q=0.9",
}
response=requests.get(WEBSITE, headers=HEADER)
content=response.text

soup = BeautifulSoup(content, "html.parser")
PRICE = soup.select_one(selector="#priceblock_ourprice")
PRODUCT_PRICE = float(unidecode(PRICE.getText()).split("Rs ")[1])

PRODUCT = soup.select_one(selector ="#productTitle").getText()

my_mail=input("Sender Mail: ")
my_password=input("Password: ")
Reciever =input("Reciever Mail: ")
MESSAGE = f'Subject: Fall in Price\n\n There is a fall in the price of your favorite item - {PRODUCT}. Head over To {WEBSITE} to buy your product at {PRODUCT_PRICE}.'
if PRODUCT_PRICE<=150.00:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=my_password)
        connection.sendmail(from_addr=my_mail, to_addrs=Reciever , msg=MESSAGE)
        print("Mail Sent")
else:
    print('Price not within your Budget')
