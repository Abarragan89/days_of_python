import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")


weather_params = {
    "appid": WEATHER_API_KEY,
    "lat": 14.41,
    "lon": 39.6,
    "units": "imperial"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
data = response.json()

for num in range(0, 40):
    if data["list"][num]["weather"][0]["id"] < 700:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages \
            .create(
            body="It's going to rain, bring an umbrella!",
            from_="+16506634889",
            to="+16617145258"
        )
        print(message.status)
        break
