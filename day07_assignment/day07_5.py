'''
Transactional Banking Ledger with SQLite & ACID Rollback Management
Scenario
A financial transaction engine executes fund transfers between accounts in a SQLite database. The engine must support 
ACID guarantees: if any part of a transfer fails (e.g. insufficient funds, invalid account), 
the entire transaction must roll back cleanly.

Problem Description
Create a custom exception TransactionError(Exception). Create a class BankingLedger that manages an accounts table 
(account_id TEXT PRIMARY KEY, holder_name TEXT, balance REAL) and an audit_log table 
(tx_id INTEGER PRIMARY KEY AUTOINCREMENT, from_acc TEXT, to_acc TEXT, amount REAL, timestamp TEXT):

create_account(account_id, holder_name, initial_deposit): Adds a new account. Raises ValueError if initial_deposit < 0.
transfer_funds(from_acc, to_acc, amount):
Executes an atomic transfer of amount from from_acc to to_acc.
Deducts amount from from_acc and adds amount to to_acc.
Records an entry in the audit_log table.
Validation & Rollback Rules:
amount must be strictly positive (> 0).
Both accounts must exist in the database.
from_acc must have a sufficient balance (>= amount).
If any condition fails, raise TransactionError and execute conn.rollback().
If all checks pass, execute conn.commit().
get_balance(account_id): Returns the current balance for the given account.
Example Walkthrough
bank = BankingLedger("bank.db")
bank.create_account("ACC101", "Arham", 5000.0)
bank.create_account("ACC102", "Lisa", 2000.0)

# Valid transfer
bank.transfer_funds("ACC101", "ACC102", 1500.0)
print(bank.get_balance("ACC101"))  # Output: 3500.0
print(bank.get_balance("ACC102"))  # Output: 3500.0

# Invalid transfer (insufficient funds) -> rolled back
try:
    bank.transfer_funds("ACC101", "ACC102", 10000.0)
except TransactionError as e:
    print(e)  # Output: Insufficient funds in account ACC101

# Balances remain untouched
print(bank.get_balance("ACC101"))  # Output: 3500.0
print(bank.get_balance("ACC102"))  # Output: 3500.0
'''
import sqlite3
from datetime import datetime


# --------------------------------
# Custom Exception
# --------------------------------

class TransactionError(Exception):
    pass


# --------------------------------
# Banking Ledger
# --------------------------------

class BankingLedger:

    def __init__(self, db_path):

        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        # Create accounts table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                account_id TEXT PRIMARY KEY,
                holder_name TEXT,
                balance REAL
            )
        """)

        # Create audit log table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS audit_log (
                tx_id INTEGER PRIMARY KEY AUTOINCREMENT,
                from_acc TEXT,
                to_acc TEXT,
                amount REAL,
                timestamp TEXT
            )
        """)

        self.conn.commit()


    # --------------------------------
    # Create Account
    # --------------------------------

    def create_account(self, account_id, holder_name, initial_deposit):

        try:

            if initial_deposit < 0:
                raise ValueError(
                    "Initial deposit cannot be negative."
                )

            self.cursor.execute(
                """
                INSERT INTO accounts
                (account_id, holder_name, balance)
                VALUES (?, ?, ?)
                """,
                (account_id, holder_name, initial_deposit)
            )

            self.conn.commit()

        except ValueError as e:
            print(e)

        except sqlite3.IntegrityError as e:
            print("Account already exists.")


    # --------------------------------
    # Transfer Funds
    # --------------------------------

    def transfer_funds(self, from_acc, to_acc, amount):

        try:

            # Check amount
            if amount <= 0:
                raise TransactionError(
                    "Transfer amount must be greater than zero."
                )

            # Check source account
            self.cursor.execute(
                """
                SELECT balance
                FROM accounts
                WHERE account_id = ?
                """,
                (from_acc,)
            )

            from_account = self.cursor.fetchone()

            if from_account is None:
                raise TransactionError(
                    f"Account {from_acc} does not exist."
                )

            # Check destination account
            self.cursor.execute(
                """
                SELECT balance
                FROM accounts
                WHERE account_id = ?
                """,
                (to_acc,)
            )

            to_account = self.cursor.fetchone()

            if to_account is None:
                raise TransactionError(
                    f"Account {to_acc} does not exist."
                )

            # Check sufficient balance
            if from_account[0] < amount:
                raise TransactionError(
                    f"Insufficient funds in account {from_acc}"
                )

            # Deduct money from sender
            self.cursor.execute(
                """
                UPDATE accounts
                SET balance = balance - ?
                WHERE account_id = ?
                """,
                (amount, from_acc)
            )

            # Add money to receiver
            self.cursor.execute(
                """
                UPDATE accounts
                SET balance = balance + ?
                WHERE account_id = ?
                """,
                (amount, to_acc)
            )

            # Add audit record
            timestamp = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            self.cursor.execute(
                """
                INSERT INTO audit_log
                (from_acc, to_acc, amount, timestamp)
                VALUES (?, ?, ?, ?)
                """,
                (from_acc, to_acc, amount, timestamp)
            )

            # Everything successful
            self.conn.commit()

            print("Transaction successful.")

        except TransactionError as e:

            # Undo everything done in this transaction
            self.conn.rollback()

            print(e)


    # --------------------------------
    # Get Balance
    # --------------------------------

    def get_balance(self, account_id):

        self.cursor.execute(
            """
            SELECT balance
            FROM accounts
            WHERE account_id = ?
            """,
            (account_id,)
        )

        row = self.cursor.fetchone()

        if row is None:
            return None

        return row[0]


# --------------------------------
# Objects
# --------------------------------

bank = BankingLedger("bank.db")


# Create accounts
bank.create_account(
    "ACC101",
    "Arham",
    5000.0
)

bank.create_account(
    "ACC102",
    "Lisa",
    2000.0
)


# Valid transfer
bank.transfer_funds(
    "ACC101",
    "ACC102",
    1500.0
)

print(bank.get_balance("ACC101"))
print(bank.get_balance("ACC102"))


# Invalid transfer
bank.transfer_funds(
    "ACC101",
    "ACC102",
    10000.0
)


# Balances remain unchanged
print(bank.get_balance("ACC101"))
print(bank.get_balance("ACC102"))