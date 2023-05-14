import os

# Flask App Configuration
SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'

# MySQL Database Configuration
DB_HOST = 'localhost'
DB_USER = 'traffic_squad'
DB_PASSWORD = 'traffic_squad'
DB_NAME = 'traffic_squad'
