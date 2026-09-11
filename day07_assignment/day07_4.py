'''
Relational SQLite User Management System
Scenario
An internal employee directory stores user contact details in a SQLite database. The application must search for users, 
display existing details, or register new users.

Problem Description
Create a class UserDatabaseManager that connects to a SQLite database file:

__init__(self, db_path): Connects to the database and creates a table users if it doesn't already exist:
Columns: id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, address TEXT, mobile TEXT, email TEXT.
find_user(self, username):
Queries the database for the given username using a parameterized SQL query.
If found, returns a dictionary: {"id": row[0], "username": row[1], "address": row[2], "mobile": row[3], "email": row[4]}.
If not found, returns None.
add_or_update_user(self, username, address, mobile, email):
Checks if username exists.
If user exists, updates their address, mobile, and email values and returns "UPDATED".
If user does not exist, inserts a new record and returns "INSERTED".
list_all_users(self): Returns a list of dictionaries for all registered users ordered alphabetically by username.
Example Walkthrough
db = UserDatabaseManager("company.db")

# Insert new user
status1 = db.add_or_update_user("arham_k", "Pune, MH", "9876543210", "arham@cdac.in")
print(status1)  # Output: INSERTED

# Search user
user_info = db.find_user("arham_k")
print(user_info["email"])  # Output: arham@cdac.in

# Update existing user
status2 = db.add_or_update_user("arham_k", "Bengaluru, KA", "9876543210", "arham@cdac.in")
print(status2)  # Output: UPDATED

'''
import sqlite3


class UserDatabaseManager:

    def __init__(self, db_path):

        # Connect to database
        self.connection = sqlite3.connect(db_path)

        # Create cursor
        self.cursor = self.connection.cursor()

        # Create users table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                address TEXT,
                mobile TEXT,
                email TEXT
            )
        """)

        # Save changes
        self.connection.commit()


    def find_user(self, username):

        self.cursor.execute(
            """
            SELECT id, username, address, mobile, email
            FROM users
            WHERE username = ?
            """,
            (username,)
        )

        row = self.cursor.fetchone()

        if row is None:
            return None

        return {
            "id": row[0],
            "username": row[1],
            "address": row[2],
            "mobile": row[3],
            "email": row[4]
        }


    def add_or_update_user(self, username, address, mobile, email):

        # Check whether user exists
        user = self.find_user(username)

        if user is not None:

            # User exists → update
            self.cursor.execute(
                """
                UPDATE users
                SET address = ?, mobile = ?, email = ?
                WHERE username = ?
                """,
                (address, mobile, email, username)
            )

            self.connection.commit()

            return "UPDATED"

        else:

            # User doesn't exist → insert
            self.cursor.execute(
                """
                INSERT INTO users
                (username, address, mobile, email)
                VALUES (?, ?, ?, ?)
                """,
                (username, address, mobile, email)
            )

            self.connection.commit()

            return "INSERTED"


    def list_all_users(self):

        self.cursor.execute(
            """
            SELECT id, username, address, mobile, email
            FROM users
            ORDER BY username
            """
        )

        rows = self.cursor.fetchall()

        users = []

        for row in rows:

            user = {
                "id": row[0],
                "username": row[1],
                "address": row[2],
                "mobile": row[3],
                "email": row[4]
            }

            users.append(user)

        return users


# --------------------------------
# Input / Using the Database
# --------------------------------

db = UserDatabaseManager("company.db")


# Insert new user
status1 = db.add_or_update_user(
    "arham_k",
    "Pune, MH",
    "9876543210",
    "arham@cdac.in"
)

print(status1)


# Search user
user_info = db.find_user("arham_k")

print(user_info["email"])


# Update existing user
status2 = db.add_or_update_user(
    "arham_k",
    "Bengaluru, KA",
    "9876543210",
    "arham@cdac.in"
)

print(status2)


# List all users
print(db.list_all_users())