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
    cookies_env = os.environ.get('_ga=GA1.2.1427950583.1780857193; _gid=GA1.2.919069519.1780857193; _fbp=fb.1.1780857193005.973973463471232193; _gat_gtag_UA_191466370_1=1; XSRF-TOKEN=eyJpdiI6IkJnTmlcL3VsUkRoNXZBQ0tOb1g1c3JnPT0iLCJ2YWx1ZSI6InY3aTlPZldTMGthTzhwQWM0czZldXFMZ0kzbTFzZmI5NHhWRDV4aDRZSVhYY0NwbXVcLzBCXC9BSTREMEtwMUNxYjdrT3psdW9zVmxzbFNLcTdMb2V3RTM5amZJZVwvV3VcL1N4TXRVaFI5Z3NFb0JHZElaSFJDc1Fja0tPcTRBWXhTdCIsIm1hYyI6ImU0OTBiZTdjNzM4YmE3ZmQxZGMyMWY1NmQ1MzkxNmE4NTQ5MDhmMzEyMDQwODVkMWY3MjU0ZWEzZWNiYjY4OTEifQ%3D%3D; orange_carrier_session=eyJpdiI6IjlSSlFcL213V25RWGE1ZEhDSkR5RldnPT0iLCJ2YWx1ZSI6Ik01MjFGSGlLNmFLSVlyNTRHSW5iQTFRRG1tSEFcL3BsK29BY3JJYkFKVll3R2JzVDg5aDhBY25BOVFnM0ViQzBKMk05QkJFblg4Tkd6bnpBaUtYeUkwd0FDbWVFeGFQSUdNOXFEaHNFMG9ENzBSdSt2aVA3NWh4cE54ckJqemY4eSIsIm1hYyI6IjI1YWUxOGUxNjE3NGMwZDdlOWY5OWEyNzdmMDc3ZGNmNGUyODQzYTFjYTUyMTg4YzhkOTI4ZGMwNjQ4ZTMyMGEifQ%3D%3D', '')
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
            "value": "GA1.2.1427950583.1780857193"
        },
        # ... add all other cookies
    ]
    
    # Settings
    MAX_ERRORS = 10
    CHECK_INTERVAL = 5
    
