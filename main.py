#!/usr/bin/env python
import config as cfg
import json
import urllib.request
import datetime
import smtplib, ssl
from dateutil import relativedelta
from email.message import EmailMessage


today = datetime.datetime.today().strftime('%y%m%d')
plusOneMonth = datetime.date.today() + relativedelta.relativedelta(months=1)
nextMonth = plusOneMonth.strftime('%y%m%d')

# print(today)
# print(nextMonth)

# Create a secure SSL context
context = ssl.create_default_context()
emailMessage = EmailMessage()
emailMessage['To'] = cfg.to_email
emailMessage['From'] = cfg.from_email
emailMessage['Subject'] = "Vaccin"

with urllib.request.urlopen(f'https://booking-api.mittvaccin.se/clinique/{cfg.clinique_id}/appointments/{cfg.appointment_id}/slots/{today}-{nextMonth}') as url:
    jsonPlanning = json.loads(url.read().decode())
    for date in jsonPlanning:
        day = date['date']
        slots = date['slots']

        for slot in slots:
            time = slot['when']
            available = slot['available']
            if available:
                booking = f'Booking available on {day} at {time}: https://bokning.mittvaccin.se/klinik/{cfg.clinique_id}/bokning'
                # print(booking)
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(cfg.from_email, cfg.smtp_token)
                    emailMessage.set_content(booking)
                    server.send_message(emailMessage)
