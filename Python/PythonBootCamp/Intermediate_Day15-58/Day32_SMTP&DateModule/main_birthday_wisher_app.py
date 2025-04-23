##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict 
# like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the 
# person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), 
# Outlook(smtp-mail.outlook.com)

import pandas
import smtplib
import datetime as dt
import random

FILE_DIRECTORY = "./Python/PythonBootCampt/Day32_SMTP&DateModule"
WORK_FILE_DIRECTORY = "./Python/PythonBootCampt/Day32_SMTP&DateModule"
GMAIL_EMAIL = "Bugs.Bunny@acmemail.com" # Replace with the email you have setup to use.
PASSWD_G = "got-to-email-account-to-get-passwd"
HOTMAIL_EMAIL = "Bugs.Bunny@acmemail.com"
PLACEHOLDER = "[NAME]"

data = pandas.read_csv(f"{FILE_DIRECTORY}/birthdays.csv")
birthday_records = data.to_dict(orient="records")

# print(birthday_records)
# print(type(birthday_records))

current_date_time = dt.datetime.now()
current_day = current_date_time.day
current_month = current_date_time.month

random_letter_selection = random.randint(1, 3)
print(random_letter_selection)

# with open(f"{FILE_DIRECTORY}/letter_{random_letter_selection}.txt") as letter_file:
#     letter_contents = letter_file.read()
#     new_letter = letter_contents.replace(PLACEHOLDER, ) 

for item in birthday_records:
    if current_day == item['day'] and current_month == item['month']:
        print("Winner Winner Chicken Dinner!")
        print(f"{item['email']}")
        with open(f"{FILE_DIRECTORY}/letter_templates/letter_{random_letter_selection}.txt") as letter_file:
            letter_contents = letter_file.read()
            new_letter = letter_contents.replace(PLACEHOLDER, item['name'])
            print(new_letter)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(GMAIL_EMAIL, PASSWD_G)
            connection.sendmail(from_addr=GMAIL_EMAIL, to_addrs=str(item['email']),
                                msg=f"Subject:Happy Birthday {item['name']}\n\n{new_letter}")





