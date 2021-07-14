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

sauce = Soup(page)
trs = sauce.body.findAll('tr')

result = []

for tr in trs:
    found = re.findall('USD', str(tr))
    if found:

        strings = [_string for _string in tr]

        for str_ in strings:
            if str_ != '\n':
                result.append(str_)

def get_needed_currency():
    buying_value_result = str(result[3])
    date_result = str(result[2])
    average_value_result = str(result[4])
    selling_value_result = str(result[5])

    buying_value = buying_value_result.replace('<td>', '').replace('</td>', '')
    current_date = date_result.replace('<td>', '').replace('</td>', '')
    average_value = average_value_result.replace('<td>', '').replace('</td>', '')
    selling_value = selling_value_result.replace('<td>', '').replace('</td>', '')

    data = {
        "buying_value": float(buying_value.strip()),
        "current_date": current_date,
        "average_value": float(average_value.strip()),
        "selling_value": float(selling_value.strip()),
        "from_currency": "RWF",
        "to_currency": "USD"
    }


    return data