'''
Here are some practical examples you can script:

    File management: Rename, move, or organize files automatically.

    Data cleanup: Load CSVs with Pandas, clean missing values, and save results.

    Email notifications: Send automated emails (e.g., tenant reminders, reports).

    Web scraping: Collect data from websites for analysis.

    System tasks: Backup folders, monitor logs, or schedule jobs.

'''

print("1. File Organizer...")
import os
import shutil

source = "E:/Downloads"
dest_images = "E:/Sorted/Images"
dest_docs = "E:/Sorted/Documents"

for filename in os.listdir(source):
    if filename.endswith((".jpg", ".png")):
        shutil.move(os.path.join(source, filename), dest_images)
    elif filename.endswith((".pdf", ".docx")):
        shutil.move(os.path.join(source, filename), dest_docs)


print("2. Daily CSV Report Cleaner...")
import pandas as pd

df = pd.read_csv("daily_report.csv")
df = df.dropna()  # remove missing values
df.to_csv("clean_report.csv", index=False)

print("3. Automated Email (using smtplib)...")
import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Reminder: Rent due tomorrow.")
msg["Subject"] = "Tenant Reminder"
msg["From"] = "you@example.com"
msg["To"] = "tenant@example.com"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("you@example.com", "yourpassword")
    server.send_message(msg)
