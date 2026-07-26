
import pandas as pd
from datetime import datetime

import smtplib
from email.mime.text import MIMEText

print("Load tenant data with Pandas...")
df = pd.read_csv("tenants.csv")
today = datetime.today().strftime("%Y-%m-%d")

# Filter tenants whose rent is due today
due_today = df[df["RentDueDate"] == today]



print("Send personalized emails...")
for _, row in due_today.iterrows():
    msg = MIMEText(f"Dear {row['Name']},\n\nThis is a reminder that your rent of Rs.{row['RentAmount']} is due today.\n\nRegards,\nRajesh")
    msg["Subject"] = "Rent Reminder"
    msg["From"] = "ecrajeshkumar@gmail.com"
    msg["To"] = row["Email"]

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("ecrajeshkumar@gmail.com", "Reya@2024$#@")
        server.send_message(msg)
