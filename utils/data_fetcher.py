import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
BASE_URL = 'https://www.alphavantage.co/query'

def get_stock_data(symbol, function='TIME_SERIES_DAILY', outputsize='compact'):
    params = {
        'function': function,
        'symbol': symbol,
        'apikey': API_KEY,
        'outputsize': outputsize,
        'datatype': 'json'
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        if 'Error Message' in data:
            raise ValueError(data['Error Message'])
        
        # Check for rate limiting
        if 'Note' in data and 'Thank you for using Alpha Vantage' in data['Note']:
            raise Exception('API rate limit exceeded. Please wait or upgrade your plan.')
        
        # Check for valid data
        if function == 'GLOBAL_QUOTE' and not data.get('Global Quote'):
            raise ValueError(f'No data available for symbol {symbol}')
            
        if function == 'TIME_SERIES_DAILY' and not data.get('Time Series (Daily)'):
            raise ValueError(f'No historical data available for symbol {symbol}')
            
        return data
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")