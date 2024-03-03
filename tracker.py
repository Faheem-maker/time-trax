from plyer import notification
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import tkinter as tk
from tkinter import ttk
from datetime import date, datetime, timedelta
from googleapiclient import discovery
from dotenv import load_dotenv
import os

env = load_dotenv()

sheet_id = os.getenv('SPREADSHEET_ID')

def send_notification():
    notification.notify(
        title='Track your time',
        message='What are you doing?',
        timeout=10,
    )


categories_csv = open('categories.csv')

categories = {}

for line in categories_csv.readlines():
    data = line.split(',')
    categories[data[0]] = data[1]

def job():
    send_notification()

def rename_worksheet(spreadsheet_id,
                        sheet_id,
                        new_title,
                        credentials):

    '''
    Renames a worksheet

    :param spreadsheet_id (str):  The ID of the spreadsheet
    :param sheet_id (int):  The worksheet ID found at the end of the html string 
    :param new_title (str): Desired title
    :param credentials (obj):  Users credentials as an object genrerated by:
        scope = ['https://www.googleapis.com/auth/spreadsheets']
        credentials = ServiceAccountCredentials.from_json_keyfile_name("filepath_to_client_secret", scope)
    
   '''
    print('inside rename spreadsheet')
    service = discovery.build('sheets', 'v4', credentials=credentials)

    requests = {
        "updateSheetProperties": {
            "properties": {
                "sheetId": sheet_id,
                "title": new_title,
            },
            "fields": "title",
        }
    }    

    body = {
        'requests': requests
    }

    print(requests)
    
    service.spreadsheets().batchUpdate( spreadsheetId=spreadsheet_id, body=body ).execute()

def duplicate_worksheet(from_spreadsheet_id,
                        sheet_id,
                        to_spreadsheet_id,
                        credentials,
                        title=None):

    '''
    Duplicates a worksheet from an existing spreadsheet, and will optionally rename the new worksheet

    :param from_spreadsheet_id(str):  The ID of the spreadsheet containing the sheet to copy from.
    :param sheet_id (int):  The worksheet ID found at the end of the html string 
    :param to_spreadsheet_id (str):  The ID of the spreadsheet to copy the sheet to - **Note this can be the same spreadsheet!
    :param credentials (obj):  Users credentials as an object genrerated by:
        scope = ['https://www.googleapis.com/auth/spreadsheets']
        credentials = ServiceAccountCredentials.from_json_keyfile_name("filepath_to_client_secret", scope)
    :param title (str):  Renames the newly created worksheet, if None, no new title will be set 

    '''
    service = discovery.build('sheets', 'v4', credentials=credentials)

    copy_sheet_to_another_spreadsheet_request_body = {
        
        # The ID of the spreadsheet to copy the sheet to.
        'destination_spreadsheet_id': to_spreadsheet_id 

    }

    request = service.spreadsheets().sheets().copyTo(spreadsheetId=from_spreadsheet_id,
                                                     sheetId=sheet_id, 
                                                     body=copy_sheet_to_another_spreadsheet_request_body)
    response = request.execute()

    if title:
        new_sheet_id = response['sheetId']
        print('Renaming duplicated sheet: ')
        print('test')
        rename_worksheet(to_spreadsheet_id, new_sheet_id, title, credentials)

def save_to_google_sheets():
    text = entry_text.get()
    category = dropdown_var.get()
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)

    current_date = date.today().strftime("%Y-%m-%d")

    spreadsheet = client.open_by_key(sheet_id)

    sheet = None

    try:
        sheet = spreadsheet.worksheet(current_date)
    except gspread.WorksheetNotFound:
        source_worksheet = spreadsheet.worksheet('template')
        current_date = date.today().strftime("%Y-%m-%d")

        duplicate_worksheet(spreadsheet.id, source_worksheet.id, spreadsheet.id, creds, current_date)

        print('creating new spreadsheet with name: ' + current_date)
    finally:
        # Get the current time and round it down to the previous half-hour
        sheet = spreadsheet.worksheet(current_date)
        current_time = datetime.now().replace(second=0, microsecond=0)
        rounded_time = current_time - timedelta(minutes=current_time.minute % 30)
        formatted_time = rounded_time.strftime('%I:%M: %p')

        time_column_values = sheet.col_values(2)
        print(time_column_values)
        row_index = time_column_values.index(formatted_time) + 1

        print(f"Current Time: {current_time.strftime('%I:%M %p')}")
        print(f"Rounded Time: {formatted_time}")
        print(f"Row Index with the rounded time: {row_index}")

        sheet.update_cell(row_index, int(categories[category]) + 1, text)

# Create the main window
root = tk.Tk()
root.title("Time Tracker")

def open_menu():
    menu_window = root

    ttk.Label(menu_window, text="What are you doing?").grid(row=0, column=0, padx=10, pady=10)
    global entry_text
    entry_text = ttk.Entry(menu_window)
    entry_text.grid(row=0, column=1, padx=10, pady=10)

    # Dropdown for category
    ttk.Label(menu_window, text="Select Category:").grid(row=1, column=0, padx=10, pady=10)
    global dropdown_var
    options = list(categories.keys())
    dropdown_var = tk.StringVar(menu_window)
    dropdown_var.set(options[0])
    dropdown = ttk.Combobox(menu_window, textvariable=dropdown_var, values=options)
    dropdown.grid(row=1, column=1, padx=10, pady=10)

    # Save button
    save_button = ttk.Button(menu_window, text="Save", command=save_to_google_sheets)
    save_button.grid(row=2, column=0, columnspan=2, pady=20)


send_notification()
open_menu()

root.mainloop()