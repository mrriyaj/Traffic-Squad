import mysql.connector
from mysql.connector import pooling
from bcrypt import hashpw, gensalt

from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

# Create database connection pool
db_config = {
    'host': DB_HOST,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'database': DB_NAME
}

db_pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)

class User:
    """User model"""
    def __init__(self, id, name, email, password_hash):
        self.id = id
        self.name = name
        self.email = email
        self.password_hash = password_hash

    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)    

    def is_authenticated(self):
        return True
    
    @staticmethod
    def get_user(user_id):
        """Load user by user_id"""
        try:
            cnx = db_pool.get_connection()
            cursor = cnx.cursor()
            query = f"SELECT * FROM users WHERE id='{user_id}'"
            cursor.execute(query)
            result = cursor.fetchone()
            cursor.close()
            cnx.close()
            if result:
                user = User(result[0], result[1], result[2], result[3])
                return user
            else:
                return None
        except mysql.connector.Error as error:
            print("Error retrieving user from the database:", error)
            return None

    @staticmethod
    def find_user_by_email(email):
        """Find user by email"""
        try:
            cnx = db_pool.get_connection()
            cursor = cnx.cursor()
            query = f"SELECT * FROM users WHERE email='{email}'"
            cursor.execute(query)
            result = cursor.fetchone()
            cursor.close()
            cnx.close()
            if result:
                user = User(result[0], result[1], result[2], result[3])
                return user
            else:
                return None
        except mysql.connector.Error as error:
            print("Error retrieving user from the database:", error)
            return None

    @staticmethod
    def create_user(name, email, password):
        """Create a new user"""
        try:
            password_hash = User._hash_password(password)
            cnx = db_pool.get_connection()
            cursor = cnx.cursor()
            query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            values = (name, email, password_hash)
            cursor.execute(query, values)
            cnx.commit()
            user_id = cursor.lastrowid
            cursor.close()
            cnx.close()
            user = User(user_id, name, email, password_hash)
            return user
        except mysql.connector.Error as error:
            print("Error creating user in the database:", error)
            return None

    def verify_password(self, password):
        """Verify the user's password"""
        return hashpw(password.encode('utf-8'), self.password_hash.encode('utf-8')) == self.password_hash.encode('utf-8')

    @staticmethod
    def _hash_password(password):
        """Hash the password using bcrypt"""
        return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')
    
    @staticmethod
    def get_all_users():
        try:
            cnx = mysql.connector.connect(**db_config)
            cursor = cnx.cursor()
            query = "SELECT id, name, email FROM users"
            cursor.execute(query)
            users = cursor.fetchall()
            cursor.close()
            cnx.close()
            return users
        except mysql.connector.Error as error:
            print("Error retrieving users from the database:", error)
            return []

    @staticmethod
    def get_user_by_id(user_id):
        try:
            cnx = mysql.connector.connect(**db_config)
            cursor = cnx.cursor()
            query = f"SELECT * FROM users WHERE id = {user_id}"
            cursor.execute(query)
            result = cursor.fetchone()
            cursor.close()
            cnx.close()
            if result:
                user = User(result[0], result[1], result[2], result[3])
                return user
            else:
                return None
        except mysql.connector.Error as error:
            print("Error retrieving user from the database:", error)
            return None

    def save(self):
        try:
            cnx = mysql.connector.connect(**db_config)
            cursor = cnx.cursor()
            query = f"UPDATE users SET name = '{self.name}', email = '{self.email}' WHERE id = {self.id}"
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
        except mysql.connector.Error as error:
            print("Error updating user in the database:", error)

    def delete(self):
        try:
            cnx = mysql.connector.connect(**db_config)
            cursor = cnx.cursor()
            query = f"DELETE FROM users WHERE id = {self.id}"
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
        except mysql.connector.Error as error:
            print("Error deleting user from the database:", error)
