# import smtplib
import datetime
import datetime as dt

#
# my_email = "testpython751@gmail.com"
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password="cbcqcthgldcwhiuw")
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="anthonybarragan87@yahoo.com",
#         msg="Subject:Hello World\n\nThis is the content of my email")


now = dt.datetime.now()
month = now.month
year = now.year
day = now.day
day_of_week = now.weekday()
print(month, day, year, day_of_week)

date_of_birth = datetime.datetime(year=1989, month=2, day=25)
print(date_of_birth)
