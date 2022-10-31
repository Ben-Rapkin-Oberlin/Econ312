# API Key - E9OSLRP3JVK5UC8M

import requests
import json

#API Request for daily BTC  prices
url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=CNY&apikey=E9OSLRP3JVK5UC8M'
r = requests.get(url)
data = r.json()
pretty_json = json.loads(r.text)


#writing json file
# a - append x - create r - read w - write
with open("btcusd.json", "x") as write_file:
    json.dump(data, write_file)

json_string = json.dumps(data)




'''
data = response.text
data_dict = json.loads(data)

df = pd.DataFrame(data_dict)
print(df)
'''
