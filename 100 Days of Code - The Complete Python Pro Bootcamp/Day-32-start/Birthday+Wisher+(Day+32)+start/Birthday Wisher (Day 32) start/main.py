import smtplib
import datetime as dt
import random

my_email = "taekim1291@gmail.com"
password = "ogarinofnanoawwb"

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="taekim1291@gmail.com",
                        msg="Hello\n\n It's me, your 2nd brain"
    )


now = dt.datetime.now()
# year = now.year
# month = now.month
day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1990 , month=1 , day=2)
# print(date_of_birth)

with open("quotes.txt") as quotes:
    all_quotes = quotes.readlines()
    quote = random.choice(all_quotes)

    print(quote)

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="taekim1291@gmail.com",
                        msg=f"Subject:Tuesday Motivation \n\n {quote}"
                        )
