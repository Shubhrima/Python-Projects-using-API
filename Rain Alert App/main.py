import requests
from twilio.rest import Client

API_KEY = " "
account_sid = ' '
auth_token = ' '

PARAMETER= {
    "lat": 22.572645,
    "lon": 88.363892,
    "appid" : API_KEY,
    "exclude" : "current,minutely,daily",
}
api = requests.get(url="http://api.openweathermap.org/data/2.5/onecall",params=PARAMETER)

data =  api.json()
print(data)

bring_umbrella = False

for i in range(0,12):
    hourly_condition = data['hourly'][i]['weather'][0]['id']
    if(hourly_condition<700):
        bring_umbrella = True

if (bring_umbrella == True):
    print('Bring Umbrella')
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Bring Umbrella ☔☔",
        from_='+12052368131',
        to='+919674029417'
    )
    print(message.status)
else:
    print('May be a sunny day. Carry sunglasses. 👓')
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="May be a sunny 🌞 day. Carry sunglasses. 👓",
        from_='+12052368131',
        to='+919674029417'
    )
    print(message.status)



