import requests
from twilio.rest import Client
from newsapi import NewsApiClient

account_sid = ' '
auth_token = ' '

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API_KEY = ' '
NEWS_API_PARAMETER={
    "apiKey" : NEWS_API_KEY,
    "qInTitle" : COMPANY_NAME,
}

STOCK_API_KEY = ' '
STOCK_API_PARAMETER={
    "function" : 'TIME_SERIES_DAILY_ADJUSTED',
    "symbol" : STOCK,
    "apikey" : STOCK_API_KEY,
}
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK_API = requests.get(url="https://www.alphavantage.co/query",params=STOCK_API_PARAMETER)
stock_data = STOCK_API.json()
daily_stock=stock_data['Time Series (Daily)']
yesterday_closing_keyz = list(daily_stock.keys() )
yesterday_date = yesterday_closing_keyz[0]
before_yesterday_date = yesterday_closing_keyz[1]

yesterday_closing = daily_stock[yesterday_date]['4. close']
yesterday_closing_stock = float(yesterday_closing)

before_yesterday_closing = daily_stock[before_yesterday_date]['4. close']
before_yesterday_closing_stock = float(before_yesterday_closing)

positive_difference = abs(yesterday_closing_stock - before_yesterday_closing_stock)

denominator = (yesterday_closing_stock + before_yesterday_closing_stock)/2
stock_percentage_difference = positive_difference/denominator*100
if int(stock_percentage_difference)<5:
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    NEWS_API = requests.get(url="https://newsapi.org/v2/everything",params=NEWS_API_PARAMETER)
    all_articles = NEWS_API.json()
    article_keyz = list(all_articles['articles'][1].keys())
    message_text=f'\n\nTSLA: {int(stock_percentage_difference)}%🔺'
    for i in range(0,3):
        print(all_articles['articles'][i]['title'])
        print(all_articles['articles'][i]['description'])
        message_text+=f"\nHeadline: {all_articles['articles'][i]['title']}\n Brief: {all_articles['articles'][i]['description']} \n\n"
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=message_text,
        from_=TWILIO_NUMBER,
        to=R_M_N
    )
    print(message.status)

