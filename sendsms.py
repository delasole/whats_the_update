from twilio.rest import Client
from crud import store_message
import os
import datetime


auth_key = os.environ['TWILIO_AUTH_TOKEN']
sending_number = '+12188750021'
acct_sid = os.environ['TWILIO_ACCOUNT_SID']

params = Client(acct_sid,auth_key)

def send_message(to,message):
        message = params.messages.create(to=to,from_=sending_number,body=message)



        

        

