import sqlite3 as sql


def add_new_user(user_id, username, referral_link):
    connection = sql.connect('./db/User_db.db')
    cursor = connection.cursor()
    cursor.execute('''
            INSERT INTO Users (username, user_id, subscribed, tokens, referral_count, referral_link, get_subscribed)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (username, user_id, 0, 0, 0, referral_link, False))
    connection.commit()
    

def add_tokens(user_id, tokens):
    connection = sql.connect('./db/User_db.db')
    cursor = connection.cursor()
    cursor.execute('''
                UPDATE Users
                SET tokens = tokens + ? 
                WHERE user_id = ?
                ''', (tokens, user_id))
    connection.commit()

    
def add_invitation(user_id):
    connection = sql.connect('./db/User_db.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE Users SET referral_count = referral_count + 1 WHERE user_id = ?', (user_id,))
    connection.commit()
    

def change_subscribed(user_id):
    connection = sql.connect('./db/User_db.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE Users SET subscribed = 1 WHERE user_id = ?', (user_id,))
    connection.commit()
    

def change_subscribed_bonus(user_id):
    connection = sql.connect('./db/User_db.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE Users SET get_subscribed = 1 WHERE user_id = ?', (user_id,))
    connection.commit()
    

def get_balance(user_id):
    connection = sql.connect('./db/User_db.db')
    cursor = connection.cursor()
    cursor.execute("SELECT tokens FROM Users WHERE user_id = ?", (user_id,))
    user_balance = cursor.fetchone()
    connection.commit()
    user_balance = str(user_balance).replace('(', '').replace(')', '').replace(',', '')
    return user_balance


def get_referral_count(user_id):
    connection = sql.connect('./db/User_db.db')
    cursor = connection.cursor()
    cursor.execute("SELECT referral_count FROM Users WHERE user_id = ?", (user_id,))
    referral_count = cursor.fetchone()
    connection.commit()
    referral_count = str(referral_count).replace('(', '').replace(')', '').replace(',', '')
    return referral_count


def get_username(user_id):
    connection = sql.connect('./db/User_db.db')
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM Users WHERE user_id =?", (user_id,))
    username = cursor.fetchone()
    connection.commit()
    username = str(username).replace('(', '').replace(')', '').replace(',', '')
    return username


def is_old(user_id):
    connection = sql.connect('./db/User_db.db')
    cursor = connection.cursor()
    cursor.execute("SELECT 1 FROM Users WHERE user_id = ?", (user_id,))
    result  = cursor.fetchone()
    connection.commit()
    return bool(result)

def if_subscribed(user_id):
    connection = sql.connect('./db/User_db.db')
    cursor = connection.cursor()
    cursor.execute('SELECT get_subscribed FROM Users WHERE user_id =?', (user_id,))
    result = cursor.fetchone()
    connection.commit()
    result = str(result).replace('(', '').replace(')', '').replace(',', '')
    return int(result)