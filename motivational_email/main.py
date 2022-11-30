import datetime as dt
import smtplib
import random

my_email = "testpython751@gmail.com"

with open("quotes.txt", mode="r") as quote_file:
    motivation_list = quote_file.readlines()
    message = random.choice(motivation_list)
    print(type(message))


def send_email():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password="cbcqcthgldcwhiuw")
        connection.sendmail(
            from_addr=my_email,
            to_addrs="anthony.bar.89@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{message}"
        )


# check if it is Monday
now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    send_email()
