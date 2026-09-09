'''
Atomic Transaction processing with Log Rollback
Scenario
A bank updates user balances in a database dictionary based on transaction files. To ensure accounting consistency, if any single transaction in a batch 
contains an error (such as a negative transfer amount, an unrecognized account number, or an overdraft), the entire batch must fail, all accounts must be 
restored to their initial states, and a rollback action must be logged to a text file.

Problem Description
Define three custom exception classes inheriting from Exception:
AccountNotFoundError (raised when an account ID is missing from the registry).
OverdraftError (raised when a withdrawal amount exceeds the account balance).
InvalidTransactionError (raised when the transaction type is unrecognized or if transaction amounts are non-positive).
Write a function process_transaction_batch(accounts, batch_list, log_path):
accounts is a dictionary where keys are account numbers (strings) and values are balances (floats), e.g., {"ACC01": 500.0, "ACC02": 200.0}.
batch_list is a list of dictionaries representing transactions, e.g.:
[
    {"acc": "ACC01", "type": "deposit", "amt": 150.0},
    {"acc": "ACC02", "type": "withdraw", "amt": 50.0}
]
log_path is a string referencing the path of the transaction log file.
Atomicity Requirements:
Create a deep copy of the accounts dictionary before starting any transaction modifications to act as a restore point (backup).
Iterate through batch_list and apply the changes to accounts:
If the transaction "acc" does not exist in accounts, raise AccountNotFoundError with message: "Account '<acc>' not found."
If transaction "type" is not "deposit" or "withdraw", raise InvalidTransactionError with message: "Invalid transaction type '<type>'."
If transaction "amt" is less than or equal to 0, raise InvalidTransactionError with message: "Transaction amount must be positive."
If transaction "type" is "withdraw" and the account balance is less than "amt", raise OverdraftError with message: "Insufficient funds. Account <acc> has balance <bal>, 
requested <amt>."

Exception Handling & Rollback:
If any exception is raised during the processing of the list, catch the exception:
Restore the accounts dictionary to the exact state saved in your backup.
Open the file at log_path (create it if it doesn't exist, append to it if it does) and write the following entry:[ROLLBACK] Batch aborted: 
<Exception Class Name> - <Exception Message>\n 
Re-raise the caught exception so that the calling program knows the transaction batch failed.
If all transactions in the batch are executed successfully:
Open the file at log_path and write: [SUCCESS] Batch completed. <number_of_transactions> transaction(s) processed.\n
Return the updated accounts dictionary.

Constraint: Ensure all file operations are safely cleaned up. Use context managers (with open(...)) or try...finally to write to the log file.

Example Walkthrough
accounts = {"ACC01": 100.0, "ACC02": 50.0}
log_file = "transactions.log"

# Batch 1: Valid transactions
batch_1 = [
    {"acc": "ACC01", "type": "withdraw", "amt": 30.0},
    {"acc": "ACC02", "type": "deposit", "amt": 20.0}
]
accounts = process_transaction_batch(accounts, batch_1, log_file)
# Result: accounts changes to {"ACC01": 70.0, "ACC02": 70.0}
# transactions.log writes: "[SUCCESS] Batch completed. 2 transaction(s) processed."

# Batch 2: Invalid transaction (triggers rollback)
batch_2 = [
    {"acc": "ACC01", "type": "deposit", "amt": 50.0},
    {"acc": "ACC02", "type": "withdraw", "amt": 200.0} # Overdraft!
]
try:
    accounts = process_transaction_batch(accounts, batch_2, log_file)
except OverdraftError as e:
    print(f"Caught: {e}")

# Verify Rollback: ACC01 must remain 70.0, NOT updated to 120.0.
print(accounts) # Output: {"ACC01": 70.0, "ACC02": 70.0}
# transactions.log writes: "[ROLLBACK] Batch aborted: OverdraftError - Insufficient funds. Account ACC02 has balance 70.0, requested 200.0."

'''
import copy

log_file = "transactions.log"
class AccountNotFoundError(Exception):
    pass

class InvalidTransactionError(Exception):
    pass

class OverdraftError(Exception):
    pass
def log(msg):
    global log_file
    with open(log_file, mode = "a") as file:
        file.writelines(msg)
    

def process_transaction_batch(accounts, batch_list, log_path):
    backup = copy.deepcopy(accounts)
    print(f'{accounts=}')
    print('-'*80)
    type = ["withdraw","deposit"]
    for d in batch_list:
        if d['acc'] not in accounts.keys():
            log(f"[ROLLBACK] Batch aborted: AccountNotFoundError - Account Not Found for {d['acc']} \n ")
            raise AccountNotFoundError(f"Account '{d['acc']}' not found.", None)
        
        if d["type"] not in type:
            log(f"[ROLLBACK] Batch aborted: InvalidTransactionError - Invalid Transaction Type {d["type"]} for Account {d["acc"]} \n ")
            raise InvalidTransactionError(f"Invalid transaction type '{d["type"]}'.", None)

        if d["amt"] <= 0:
            log(f"[ROLLBACK] Batch aborted: InvalidTransactionError - Transaction amount must be positive. \n ")
            raise InvalidTransactionError("Transaction amount must be positive.", None)

        if d['amt'] > accounts[d['acc']] and d['type'] == 'withdraw':
            log(f"[ROLLBACK] Batch aborted: OverdraftError - Insufficient funds. Account {d['acc']} has balance {accounts[d['acc']]}, requested {d['amt']}.\n")
            for originalKey, originalValue in accounts.items():
                for deepKey, deepValue in backup.items():
                    if deepValue != originalValue and deepKey == originalKey:
                        print(f"{originalKey} must remain {deepValue} not update {originalValue}")

            print(backup)
            raise OverdraftError(f"Insufficient funds. Account {d['acc']} has balance {accounts[d['acc']]}, requested {d['amt']}.")

        if d["type"] == "withdraw":
            accounts[d['acc']] -= d['amt']

        if d["type"] == "deposit":
            accounts[d['acc']] += d['amt']

    return accounts



def main():
    accounts = {"ACC01": 100.0, "ACC02": 70.0}    
    try:
        batch_list = [
            {"acc": "ACC01", "type": "withdraw", "amt": 30.0},
            {"acc": "ACC02", "type": "deposit", "amt": 20.0}
        ]
        print(f'Current Batch : {batch_list}')
        result = process_transaction_batch(accounts, batch_list, log_file)
        accounts = result
        print(f'Updated account: {result}')
        print(f'Batch completed Successfully. {len(result)} transaction(s) processed')
        log(f"[SUCCESS] Batch completed. {len(result)} transaction(s) processed.\n")
    except (OverdraftError, InvalidTransactionError, AccountNotFoundError) as e:
        print(f"Caught: {e}")
    print(":"*80)
    try:
        batch_list = [
            {"acc": "ACC01", "type": "deposit", "amt": 50.0},
            {"acc": "ACC02", "type": "withdraw", "amt": 200.0} # Overdraft!
        ]
        print(f'Current Batch : {batch_list}')
        result = process_transaction_batch(accounts, batch_list, log_file)
        accounts = result
        print(f'Updated account: {result}')
        print(f'Batch completed Successfully. {len(result)} transaction(s) processed')
        log(f"[SUCCESS] Batch completed. {len(result)} transaction(s) processed.\n")
    except (OverdraftError, InvalidTransactionError, AccountNotFoundError) as e:
        print(f"Caught: {e}")
    print(":"*80)
if __name__ == "__main__":
    main()
    