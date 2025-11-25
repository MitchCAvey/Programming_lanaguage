import smtplib
import datetime as dt
import random

FILE_DIRECTORY = "./PersonalSource/Python/PythonBootCampt/Day32_SMTP&DateModule"
WORK_FILE_DIRECTORY = "./Python/PythonBootCampt/Day32_SMTP&DateModule"
GMAIL_EMAIL = "PLACE-HOLDER"
PASSWD_G = "PLACE-HOLDER"
HOTMAIL_EMAIL = "PLACE-HOLDER"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    with open(f"{FILE_DIRECTORY}/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        todays_quote = random.choice(all_quotes)
    print(todays_quote)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(GMAIL_EMAIL, PASSWD_G)
        connection.sendmail(from_addr=GMAIL_EMAIL, to_addrs=HOTMAIL_EMAIL,
                            msg=f"Subject:Monday Motivational Quotes\n\n {todays_quote}")

# gmail_email = "galic.warrior@gmail.com"
# passwd_g = "vfrc rhpw kpaj taau"
# hotmail_email = "galic_warrior@hotmail.com"
# passwd_h = "BXEKH-FWXZF-PWL25-4G44G-KHP48"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=gmail_email, password=passwd_g)
#     connection.sendmail(from_addr=gmail_email, 
#                         to_addrs=hotmail_email, 
#                         msg="Subject:Python Script Sending Emails\n\nTest Message from Python script")
# connection.close()

# current_date_time = dt.datetime.now()
# year = current_date_time.year
# month = current_date_time.month
# day = current_date_time.day
# hour = current_date_time.hour
# minute = current_date_time.minute

# print(current_date_time)
# print(type(current_date_time))

# print(year)
# print(type(year))

# print(f"The current year is: {year}, current month is: {month}, current day is: {day}")
# print(f"current hour is: {hour}, current minute is: {minute}")

# date_of_birth = dt.datetime(year=1986, month=6, day=21)
# print(date_of_birth)



