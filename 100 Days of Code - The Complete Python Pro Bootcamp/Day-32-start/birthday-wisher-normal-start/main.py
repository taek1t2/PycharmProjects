import smtplib
import datetime as dt
import pandas
import random

my_email = "taekim1291@gmail.com"
password = "ogarinofnanoawwb"


now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)

data = pandas.read_csv("birthdays.csv")


b_day_dict = {(data_row["month"], data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in b_day_dict:
    birthday_person = b_day_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Happy Birthday!!\n\n{content}"
                            )




