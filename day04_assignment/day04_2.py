'''
Robust Phonebook Contact Registry
Scenario
You are writing a Command-Line Interface (CLI) contact registry that maps user names to their phone numbers. 
The program needs to validate user inputs robustly to prevent corrupted formatting or empty values from breaking 
the registry database.

Problem Description
Define a custom exception class named InvalidPhoneNumberError that inherits from Exception.
Write a function register_contact(phonebook, name, phone_input):
phonebook is a dictionary mapping contact names (strings) to their phone numbers (strings).
Validate the name parameter: it must be a non-empty string consisting only of alphabetic characters and spaces. If invalid, 
raise a standard ValueError with the message: "Contact name must be a non-empty alphabetic string."
Validate the phone_input parameter: it must consist only of digits. Check this by attempting to convert it to an integer 
using int().
If the conversion fails (raises a ValueError), catch that exception and raise your custom InvalidPhoneNumberError with the 
message: "Phone number must contain digits only."
If validations pass, store phone_input as a string in the phonebook under the key name (preserving any leading zeros).
Return the updated phonebook dictionary.
Example Walkthrough
contacts = {}

# 1. Valid Input
contacts = register_contact(contacts, "Alice", "0987654321")
# Result: {"Alice": "0987654321"}

# 2. Invalid Phone Number (Raises InvalidPhoneNumberError)
try:
    contacts = register_contact(contacts, "Bob", "123-456-789")
except InvalidPhoneNumberError as e:
    print(e)  # Output: Phone number must contain digits only.

# 3. Invalid Name (Raises ValueError)
try:
    contacts = register_contact(contacts, "Bob123", "9876543210")
except ValueError as e:
    print(e)  # Output: Contact name must be a non-empty alphabetic string.

'''
class InvalidPhoneNumberError(Exception):
    pass

def register_contact(contact, name, phone_input):
    if not name.strip().isalpha() or name == "":
        raise ValueError("Contact name must be a non-empty alphabetic string.")
    elif not int(phone_input):
        raise InvalidPhoneNumberError("Phone number must contain digits only.")
    else:
        contact[name] = phone_input
        return contact

  
def main():
    contact = {}
    try:
        name = input("Enter name: ")
        phone_input = input("Enter phone number: ")
        result = register_contact(contact, name, phone_input)
        print(f"Result: {result}")
        
    except ValueError as e:
        print(e)
    except InvalidPhoneNumberError as e:
        print(e) 

if __name__ == "__main__" :
    main()