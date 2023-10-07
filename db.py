import sqlite3 as sq

db = sq.connect("deeplbot.db")
cur = db.cursor()


async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS history(user_id TEXT PRIMARY KEY, message TEXT, translate_message TEXT)")
    db.commit()


async def create_history(user_id):
    user = cur.execute("SELECT 1 FROM history WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO history VALUES(?,?,?)", (user_id, '', ''))
        db.commit()


async def edit_history(user_id, message, translate_message):
    cur.execute("UPDATE history WHERE user_id == '{}' SET message == '{}', translate_message == '{}'".format(user_id, message, translate_message))
    db.commit()
