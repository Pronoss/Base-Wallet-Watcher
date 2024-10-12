import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
    BASE_RPC_URL = os.getenv('BASE_RPC_URL')  # RPC URL for Base Blockchain
