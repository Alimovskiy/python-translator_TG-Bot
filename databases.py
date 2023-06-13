import sqlite3

database = sqlite3.connect('translator.db')
cursor = database.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER,
        from_lang TEXT,
        to_lang TEXT,
        org_text TEXT,
        trans_text TEXT
    )
''')

database.commit()
database.close()






