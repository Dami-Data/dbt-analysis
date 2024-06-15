import re
import pandas as pd
import requests
import certifi
import os
import json
import google.auth
from datetime import datetime, tzinfo, timezone
from google.oauth2 import service_account
from datetime import datetime, timedelta, date
from google.cloud import bigquery
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# Set the path to your service account JSON file
json_keyfile_path = 'file path to credential'

# Set the URL of your Google Sheet
sheet_url = 'copy sheet url' 

# Use credentials to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile_path, scope)#upload your json credential file in the folder

gc = gspread.authorize(credentials)

# Open the Google Sheet by URL
workbook = gc.open_by_url(sheet_url)

sheet = workbook.sheet1  

df = pd.DataFrame(sheet.get_all_records())

df = df.rename(columns={'Customer Name': 'name', 'Company Email': 'email', 'Company Name': 'company_name', 'Customer Number': 'phone'})

def format_phone(phone):
    phone_str = str(phone)
    if phone_str.startswith('234'):
        return '+' + phone_str
    elif phone_str.startswith('0'):
        return '+234' + phone_str[1:]
    elif phone_str[0] in('8','9','7'):
        return '+234' + phone_str
    else:
        return phone_str

df['phone'] = df['phone'].apply(format_phone)

def format_name(name):
    name_str = str(name)
    if name_str.startswith('234'):
        return '+' + name_str
    elif name_str.startswith('0'):
        return '+234' + name_str[1:]
    elif name_str[0] in('8','9','7'):
        return '+234' + name_str
    else:
        return name_str
df['name'] = df['name'].apply(format_name)



#df['phone'] = df['phone'].apply(lambda x: '+' + str(x) if str(x).startswith('234') else str(x))
#df['phone'] = df['phone'].apply(lambda x: '+234' + x[1:] if x.startswith('0') else x)
#df['name'] = df['name'].apply(lambda x: '+' + str(x) if str(x).startswith('234') else str(x))
#print(df)

# Set the path to your seed CSV file
seed_csv_path = '/Users/dbt/seeds/user_details.csv'

# Save the DataFrame to the seed CSV file
df.to_csv(seed_csv_path, index=False)