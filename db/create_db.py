import sqlite3 as sql


connection = sql.connect('./db/User_db.db')
cursor = connection.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        subscribed INTEGER NOT NULL,
        tokens INTEGER NOT NULL,
        referral_count INTEGER NOT NULL,
        referral_link TEXT,
        get_subscribed BOOLEAN
        )
        ''')

connection.commit()