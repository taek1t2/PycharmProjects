import smtplib

my_email = "taekim1291@gmail.com"
password = "ogarinofnanoawwb"

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="taekim1291@gmail.com",
                        msg="Hello\n\n It's me, your 2nd brain"
    )


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1990 , month=1 , day=2)
print(date_of_birth)