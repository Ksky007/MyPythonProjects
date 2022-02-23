import requests
import smtplib
import os

PASSWORD = os.environ.get('PASS')


def send_alert():
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user='test0827111@gmail.com', password=PASSWORD)
        connection.sendmail(from_addr='test0827111@gmail.com',
                            to_addrs='q564756917@yahoo.com',
                            msg="Subject: Rain Alert\n\nBring an Umbrella~")


API_KEY = os.environ.get('APIKEY')

PARAMETERS = {
    "lon": -96.7836,
    'lat': 32.7668,
    'units': 'metric',
    'exclude': "current,minutely,daily",
    'appid': API_KEY
}
response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=PARAMETERS)
response.raise_for_status()
data = response.json()
print(data['hourly'][0]['weather'][0]['id'])

for i in range(12):
    id = data['hourly'][i]['weather'][0]['id']
    if id < 700:
        send_alert()
        print(f"{i} {id}, Bring an Umbrella")
        break



