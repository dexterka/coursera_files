# Parse JSON data containing geo-location of branches and ATMs of CSOB SK

# Env setup
import urllib.request
import json
import sqlite3
import pandas as pd
from os import path
from pandas.io.json import json_normalize

pd.set_option('display.max_columns', 500)


# Functions
def process_oh(df, column_name):
    for key, value in enumerate(df[column_name]):
        if value is None or not value:
            df.at[key, column_name] = ''
            continue
        lst = list()
        for item in value:
            oh_from = item['from']
            oh_to = item['to']
            lst.append(oh_from + ' - ' + oh_to)
        df.at[key, column_name] = ' - '.join(lst)


def process_services(df, column_name):
    for key, value in enumerate(df[column_name]):
        if value is None or not value:
            df.at[key, column_name] = ''
            continue
        lst = list()
        for item in value:
            if item == 1:
                item = 'Open at weekends and during holidays'
            elif item == 2:
                item = 'Safe deposit box'
            elif item == 3:
                item = 'Private banking'
            elif item == 4:
                item = 'Wheelchair access'
            elif item == 5:
                item = 'Parking'
            elif item == 6:
                item = 'sixth'
            else:
                item = 'Corporate clients'
            lst.append(item)
        df.at[key, column_name] = ', '.join(lst)


def process_consultants(df, column_name):
    for key, value in enumerate(df[column_name]):
        if value is None or not value:
            df.at[key, column_name] = ''
            continue
        lst = list()
        for item in value:
            name = item['name']
            email = item['email']
            phone = item['phone']
            lst.append(name + ', ' + email + ', ' + phone)
        df.at[key, column_name] = ', '.join(lst)


# Connect to db
connect = sqlite3.connect(path.abspath(path.join('..', '..', 'sample_files', 'db', 'week5_assignment_branch_atm.sqlite')))
cursor = connect.cursor()

# Download JSON data
url_name = 'https://www.csob.sk/kontakty/pobocky-a-bankomaty?p_p_id=branchAndAtm_WAR_portalfoundation&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=branchesAndAtmsList.js'
html_request = urllib.request.Request(url_name, headers={'User-Agent': 'Mozilla/5.0'})
html_read = urllib.request.urlopen(html_request).read()

# Parse JSON data
parsed_json = json.loads(html_read)
json_data = json_normalize(parsed_json)  # flatten JSON data

# Save JSON data to pandas df
data_raw = pd.DataFrame(json_data)

# Cleanup the df
# Keep only certain columns
data_clean = data_raw[['id', 'branchTypeCode',
                       'address.street', 'address.city', 'address.postCode', 'address.locationDescr', 'address.email',
                       'address.phone', 'address.latitude', 'address.longitude',
                       'openingHours.calendarDays.MONDAY.sections',
                       'openingHours.calendarDays.TUESDAY.sections',
                       'openingHours.calendarDays.WEDNESDAY.sections',
                       'openingHours.calendarDays.THURSDAY.sections',
                       'openingHours.calendarDays.FRIDAY.sections',
                       'openingHours.calendarDays.SATURDAY.sections',
                       'openingHours.calendarDays.SUNDAY.sections',
                       'branchServiceCodes', 'consultants'
                       ]]
# Insert the new columns for bank code
data_clean.insert(1, 'bank_code', '7500')

# Rename the columns
data_clean.columns = ['id', 'bank_code', 'branch_type_id', 'street', 'town', 'zip_code', 'location', 'email', 'phone',
                      'latitude', 'longitude',
                      'oh_monday', 'oh_tuesday', 'oh_wednesday', 'oh_thursday', 'oh_friday', 'oh_saturday', 'oh_sunday',
                      'services', 'consultants']

# Process the opening hours
process_oh(data_clean, 'oh_monday')
process_oh(data_clean, 'oh_tuesday')
process_oh(data_clean, 'oh_wednesday')
process_oh(data_clean, 'oh_thursday')
process_oh(data_clean, 'oh_friday')
process_oh(data_clean, 'oh_saturday')
process_oh(data_clean, 'oh_sunday')

# Process services (labelling)
process_services(data_clean, 'services')
# counts_services = data_clean['services'].value_counts()
# print('Frequency table for provided services: ', counts_services)

# Process consultants
process_consultants(data_clean, 'consultants')

# Check the frequency table for branch_type_id
counts_branch_type = data_clean['branch_type_id'].value_counts()
# print('Frequency table for types of branches or ATM:', counts_branch_type)

# Create the codelist for the branch_type_id
codelist_raw = pd.read_csv(path.abspath(path.join('..', '..', 'sample_files', 'branch_types.csv')),
                           sep=';',
                           encoding='utf-8')
# print(codelist_raw.head())

# Load entries to db
data_load = data_clean.loc[:, 'id':'consultants']
data_load.to_sql('branch_atm', con=connect, index=False, if_exists='replace')
codelist_raw.to_sql('branch_type_cl', con=connect, index=False, if_exists='replace')

print('Loaded %d rows and %d columns to the database.' % (data_load.shape[0], data_load.shape[1]))
print('There are %d different branch or ATM types loaded to the database.' % codelist_raw.shape[0])
