import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os

env = load_dotenv()

sheet_id = os.getenv('SPREADSHEET_ID')

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

template = client.open_by_key(sheet_id).worksheet('template')

categories = template.row_values(2)

# Create the CSV

categories_csv = open('categories.csv', 'w')

for i in range(len(categories)):
    if categories[i] != '':
        categories_csv.write(f'{categories[i]},{i}\n')


categories_csv.close()