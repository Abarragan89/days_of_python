import requests
from datetime import datetime
import smtplib

MY_LAT = 34.052235
MY_LONG = -118.243683
MY_EMAIL = "testpython751@gmail.com"
PASSWORD = "cbcqcthgldcwhiuw"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

response = response.json()

latitude = float(response['iss_position']['latitude'])
longitude = float(response['iss_position']['longitude'])

coordinates = (latitude, longitude)
print("iss positin", coordinates)

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}
response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print("sunrise", sunrise)
print("sunset", sunset)

time_now = datetime.now()
current_hour = int(str(time_now).split(" ")[1].split(":")[0])
print(current_hour)

def send_email():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="anthony.bar.89@gmail.com",
            msg=f"Subject:ISS OVERHEAD!\n\nThe ISS is overhead!"
        )


def is_iss_overhead():
    lat_diff = abs(MY_LAT - coordinates[0])
    long_diff = abs(MY_LONG - coordinates[1])
    print(long_diff)
    print(lat_diff)
    if lat_diff < 120 and long_diff < 120:
        send_email()


def is_night_time():
    if sunset < current_hour < sunrise:
        is_iss_overhead()


is_night_time()
