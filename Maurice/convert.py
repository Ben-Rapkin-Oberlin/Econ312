import pandas as pd

with open('btcusd.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('btcusd.csv', encoding='utf-8', index=False)








