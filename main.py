import json
import requests
import pandas as pd
from datetime import datetime

API_KEY = '2YnmvtDF40QUMHJIELjRVHgomI4'

start_date = datetime.strptime('2019-01-01', '%Y-%m-%d')
end_date = datetime.strptime('2023-11-28', '%Y-%m-%d')

start_timestamp = int(start_date.timestamp())
end_timestamp = int(end_date.timestamp())

res = requests.get('https://api.glassnode.com/v1/metrics/market/price_realized_usd',
    params={'a': 'BTC', 'i': '1h', 'f': 'CSV',
            's': start_timestamp,
            'u': end_timestamp,
#            'c': 'NATIVE',
            'timestamp_format': 'humanized', 'api_key': API_KEY})

csv_file_path = '/Users/jeffko/PycharmProjects/Glassnode_api/glassnode_data/realized-price-1h.csv'

with open(csv_file_path, 'w') as f:
    f.write(res.text)

print(f'DataFrame has been saved to {csv_file_path}')
