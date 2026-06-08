import os
import json

# Heroku vs Local
IS_HEROKU = os.environ.get('DYNO') is not None

if IS_HEROKU:
    # Heroku config
    BOT_TOKEN = os.environ.get('8679142754:AAGOJnzPBw-bWBR0iWzkfre7V5TdNLe76yE', '')
    ADMIN_CHAT_ID = os.environ.get('7562559526', '')
    GROUP_CHAT_ID = os.environ.get('-1004059178902', '')
    
    # Orange Carrier Login Credentials (fallback)
    ORANGE_EMAIL = os.environ.get('wibowoutara@gmail.com', '')
    ORANGE_PASSWORD = os.environ.get('Anjas122@', '')
    
    # URLs
    LOGIN_URL = os.environ.get('LOGIN_URL', 'https://www.orangecarrier.com/login')
    CALL_URL = os.environ.get('CALL_URL', 'https://www.orangecarrier.com/live/calls')
    BASE_URL = os.environ.get('BASE_URL', 'https://www.orangecarrier.com')
    
    # Cookies from environment variable (JSON string)
    cookies_env = os.environ.get('ORANGE_COOKIES', '')
    ORANGE_COOKIES = json.loads(cookies_env) if cookies_env else []
    
    # Settings
    MAX_ERRORS = int(os.environ.get('MAX_ERRORS', '10'))
    CHECK_INTERVAL = int(os.environ.get('CHECK_INTERVAL', '5'))
    
else:
    # Local development Configuration
    BOT_TOKEN = '8679142754:AAGOJnzPBw-bWBR0iWzkfre7V5TdNLe76yE'
    ADMIN_CHAT_ID = '7562559526'
    GROUP_CHAT_ID = '-1004059178902'
    
    # Orange Carrier Login Credentials
    ORANGE_EMAIL = 'wibowoutara@gmail.com'
    ORANGE_PASSWORD = 'Anjas122@'
    
    # URLs
    LOGIN_URL = 'https://www.orangecarrier.com/login'
    CALL_URL = 'https://www.orangecarrier.com/live/calls'
    BASE_URL = 'https://www.orangecarrier.com'
    
    # Cookies (paste your cookies here as Python list)
    ORANGE_COOKIES = [
        # Paste your cookies here in the same format
        {
            "domain": ".orangecarrier.com",
            "expirationDate": 1803729122.883909,
            "hostOnly": False,
            "httpOnly": False,
            "name": "_ga",
            "path": "/",
            "sameSite": "unspecified",
            "secure": False,
            "session": False,
            "storeId": "0",
            "value": "GA1.2.1935366298.1768217292"
        },
        # ... add all other cookies
    ]
    
    # Settings
    MAX_ERRORS = 10
    CHECK_INTERVAL = 5
