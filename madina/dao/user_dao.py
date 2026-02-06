from dao.BaseDao import Dao
import sys

sys.path.append("/Users/argenkulzhanov/Desktop/Designer/baisal/classes")
from classes.user import User

class UserDAO(Dao):
    def __init__(self, db_path):
        super().__init__(db_path)

    def insert(self, user: User):
        query = "INSERT INTO users (username, password, email) VALUES (?, ?, ?)"
        self._cursor.execute(query, (user.get_username(), user.get_password(), user.get_email()))
        self._connection.commit()

    def find_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        if row:
            return User(row[1], row[2], row[3])  # Ensure row[3] corresponds to the email field
        return None

    def find_by_id(self, user_id):
        query = "SELECT * FROM Users WHERE id = ?"
        self._cursor.execute(query, (user_id,))
        row = self._cursor.fetchone()
        if row:
            return User(row[1], row[2])
        return None

    def find_by_email(self, email):
        query = "SELECT * FROM Users WHERE email = ?"
        self._cursor.execute(query, (email,))
        row = self._cursor.fetchone()
        if row:
            return User(row[1], row[2])
        return None