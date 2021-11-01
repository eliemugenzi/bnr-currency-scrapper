from bs4 import BeautifulSoup as Soup
import urllib.request
import ssl
import re
import os
from dotenv import load_dotenv


load_dotenv()

URL = os.environ.get('BNR_CURRENCY_URL')

context = ssl._create_unverified_context()
page = urllib.request.urlopen(URL,  context=context);

html_content = Soup(page, features='html.parser')
table_rows = html_content.body.findAll('tr')

result = []

for table_row in table_rows:
    found_row = re.findall('USD', str(table_row))
    if found_row:

        table_data_set = [table_row_item for table_row_item in table_row]

        for table_data in table_data_set:
            if table_data != '\n':
                result.append(table_data)

def get_needed_currency():
    buying_value_result = str(result[3])
    date_result = str(result[2])
    average_value_result = str(result[4])
    selling_value_result = str(result[5])

    buying_value = buying_value_result.replace('<td>', '').replace('</td>', '').replace(',', '')
    current_date = date_result.replace('<td>', '').replace('</td>', '').replace(',', '')
    average_value = average_value_result.replace('<td>', '').replace('</td>', '').replace(',', '')
    selling_value = selling_value_result.replace('<td>', '').replace('</td>', '').replace(',', '')

    print('WTF', average_value)

    data = {
        "buying_value": float(buying_value.strip()),
        "current_date": current_date,
        "average_value": float(average_value.strip()),
        "selling_value": float(selling_value.strip()),
        "from_currency": "RWF",
        "to_currency": "USD"
    }


    return data