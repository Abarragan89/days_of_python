import datetime as dt
import smtplib
import pandas
import csv

# Get current Date
now = dt.datetime.now()
current_month = now.month
current_day = now.day
my_email = "testpython751@gmail.com"


def send_wishes(user_info):
    with open("letter_2.txt", mode="r") as letter_file:
        letter = letter_file.readlines()
        print(letter[0])
        letter[0] = letter[0].replace("[NAME]", user_info['name'])
        custom_letter = "".join(letter)


    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password="cbcqcthgldcwhiuw")
        connection.sendmail(
            from_addr=my_email,
            to_addrs=user_info['email'],
            msg=f"Subject:Happy Birthday\n\n{custom_letter}"
        )


data = pandas.read_csv("birthday_data.txt")

birthdays_array = data.to_dict(orient="records")
for birthday_info in birthdays_array:
    birthday_month = birthday_info['month']
    birthday_day = birthday_info['day']
    if birthday_month == current_month and birthday_day == current_day:
        send_wishes(birthday_info)
