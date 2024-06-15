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
json_keyfile_path = 'filepath'

# Set the URL of your Google Sheet
sheet_url = 'copy sheet url'

# Use credentials to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile_path, scope) #upload your json credential file in the folder

gc = gspread.authorize(credentials)

# Open the Google Sheet by URL
workbook = gc.open_by_url(sheet_url)

sheet = workbook.sheet1  

df = pd.DataFrame(sheet.get_all_records())

#print(df)

# Set the path to your seed CSV file
seed_csv_path = '/Users/coviddeaths.csv'

# Save the DataFrame to the seed CSV file
df.to_csv(seed_csv_path, index=False)