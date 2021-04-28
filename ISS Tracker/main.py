import requests
import datetime as dt
from smtplib import SMTP
import time

MY_MAIL=' '
MY_PASSWORD=' '

LAT = 22.572645
LONG = 88.363892
parameters={
    'lat': LAT,
    'lng' : LONG,
    'formatted':0,
}

def is_night():
    response=requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data=response.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    #print(f'sunrise: {sunrise}   || sunset:  {sunset}')


    sunrise_time = sunrise.split('T')[1]
    sunrise_time_hour = int(sunrise_time.split(':')[0])+6
    if sunrise_time_hour>=24:
        #if utc of previous day
        sunrise_time_hour-=24
    print(sunrise_time_hour)

    sunset_time_hour = int(sunset.split('T')[1].split(':')[0])+6
    print(sunset_time_hour)

    now=dt.datetime.now()
    now_hour=now.hour
    print(now_hour)
    #print(f'now:  {now}')

    if now_hour>=sunset_time_hour or now_hour<=sunrise_time_hour:
        print('Night')
        return True
    else:
        print('Daytime')
        return False


#location of iss


def is_iss_here():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    iss_data = response_iss.json()

    iss_longitude = iss_data['iss_position']['longitude']
    iss_latitude = iss_data['iss_position']['latitude']
    latitude = float(iss_latitude)
    longitude = float(iss_longitude)
    print(latitude)
    print(longitude)
    if LAT-5<= latitude <=LAT+5 and LONG-5<= longitude <=LONG+5:
        return True



while True:
    time.sleep(120)
    if is_night() and is_iss_here():
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_MAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_MAIL, to_addrs='shubhrijana@gmail.com',
                                msg=f"Subject:Take a Look at the Sky\n\nISS is overhead!!!1")
            print('Mail Sent')
