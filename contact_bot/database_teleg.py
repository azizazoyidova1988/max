import sqlite3


class Database:
    def __init__(self, database):
        self.conn = sqlite3.connect(database, check_same_thread=False)
        self.cur = self.conn.cursor()

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER NOT NULL,
            f_name text  NULL,
            l_name text  NULL,
            contact text NULL,
            created_at datetime
            )
        """)
        self.conn.commit()

    def create_user(self, chat_id,  created_at):
        self.cur.execute("""
            INSERT INTO users(chat_id,created_at) VALUES(?,?)
         """, (chat_id,  created_at))
        self.conn.commit()

    def get_chat_id(self, chat_id):
        self.cur.execute("""
        SELECT * FROM users
        WHERE chat_id=?
        """, (chat_id,))

        user = dict_fetchone(self.cur)
        return user

    def update_user(self, state, chat_id,data):
        if state == 1:
            self.conn.execute("""
            UPDATE users SET f_name=?
            WHERE chat_id=?
            """, ( chat_id,data))

        elif state == 2:
            self.conn.execute("""
            UPDATE users SET l_name=?
            WHERE chat_id=?
            """, (chat_id,data))

        elif state == 3:
            self.conn.execute("""
            UPDATE users SET contact=?
            WHERE chat_id=?
            """, ( chat_id,data))

        self.conn.commit()


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
