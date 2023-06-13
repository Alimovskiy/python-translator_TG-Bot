TOKEN = "6196472914:AAGD7pTZPr-wHesqQsb1NzFrEQduWuNA_JE"
CHANNAL_ID = ""

import flag

LANGUAGES = {
    'en': 'English 🇬🇧',
    'ru': 'Russian 🇷🇺',
    'de': 'Genman 🇩🇪',
    'uz': 'Uzbek 🇺🇿',
    'fr': 'French 🇫🇷',
    'ko': 'Korean 🇰🇷'
}

def get_key(value):
    for k, v in LANGUAGES.items():
        if value == v:
            return k