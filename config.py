import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
    BASE_URL = 'https://www.alphavantage.co/query'
    
    REDIS_CONFIG = {
        'host': os.getenv('REDIS_HOST', 'localhost'),
        'port': int(os.getenv('REDIS_PORT', 6379)),
        'db': int(os.getenv('REDIS_DB', 0)),
        'decode_responses': False
    }


#Create an instance to import elsewhere
config = Config()