import sqlite3 as lite


def create_db():
    db = lite.connect('message.db')
    c = db.cursor()
    create = "CREATE TABLE IF NOT EXISTS {} {}".format('messages', COLUMNS)
    c.execute(create)
    db.commit()
    db.close()
