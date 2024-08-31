from datetime import datetime
import pandas as pd
import random
import smtplib
import os

MY_EMAIL = "vadisettydhanush.21bcs3950@gmail.com"  # Update with your email
MY_PASSWORD = "rmsg dffg idgn flbc"  # Update with your email password

# Ensure today's date is correctly retrieved
today = datetime.now()
today_tuple = (today.month, today.day)

# Load and process the CSV file
try:
    data = pd.read_csv("birthdays.csv")
except FileNotFoundError:
    print("Error: birthdays.csv file not found.")
    data = pd.DataFrame()

# Convert the data into a dictionary
birthdays_dict = {(row["month"], row["day"]): row for _, row in data.iterrows()}

# Check if today matches any birthday in the dictionary
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    # Select a random letter template
    try:
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name"])
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        contents = None

    # Send the email if contents were successfully read
    if contents:
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:  # Ensure port 587 for TLS
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=birthday_person["email"],
                    msg=f"Subject:Happy Birthday!\n\n{contents}"
                )
            print("Birthday email sent successfully!")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")
    else:
        print("Failed to prepare the email content.")
else:
    print("No birthdays today.")
