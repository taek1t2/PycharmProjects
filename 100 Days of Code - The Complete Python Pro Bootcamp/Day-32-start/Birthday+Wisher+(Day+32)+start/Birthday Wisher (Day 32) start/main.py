import smtplib

my_email = "taekim1291@gmail.com"
password = "abcd1234()"

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="taekim1291@gmail.com", msg="Hello 2nd brain")
connection.close()