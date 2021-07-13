from flask import Flask, jsonify
from bs4 import BeautifulSoup as Soup
import urllib.request
import ssl
import re


app = Flask(__name__)

context = ssl._create_unverified_context()
page = urllib.request.urlopen('https://www.bnr.rw/currency/exchange-rate/?tx_bnrcurrencymanager_master%5Baction%5D=list&tx_bnrcurrencymanager_master%5Bcontroller%5D=Currency&tx_bnrcurrencymanager_master%5B%40widget_0%5D%5BcurrentPage%5D=5&cHash=f7e8d9b7ab989eeb3f22193779b76462',  context=context);

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

    data = jsonify(data)

    print(type(data))

    return data

@app.route('/')
def index():
    response = get_needed_currency()
    return response


