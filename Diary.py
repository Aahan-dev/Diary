from cryptography.fernet import Fernet
import os


class SecretDiary:
    def __init__(self, filename='diary.txt'): # `__init__` function initializes the SecretDiary object.
        
        self.filename = filename
        self.key = self.load_or_create_key()  # Load or create a new encryption key
        self.cipher = Fernet(self.key)  # Create a Fernet cipher object


    def load_or_create_key(self): # `load_or_create_key` function loads an existing key or creates a new one if it doesn't exist.
        
        key_file = 'secret.key'
        if os.path.exists(key_file):
            with open(key_file, 'rb') as file:
                return file.read()  # Load existing key
        else:
            key = Fernet.generate_key()  # Generate a new key
            with open(key_file, 'wb') as file:
                file.write(key)  # Save the new key to a file
            return key


    def write_entry(self, entry): # `write_entry` function encrypts and saves a diary entry to the file.
        
        encrypted_entry = self.cipher.encrypt(entry.encode())  # Encrypt the entry
        with open(self.filename, 'ab') as file:
            file.write(encrypted_entry + b'\n')  # Save the encrypted entry


    def read_entries(self): # `read_entries` function decrypts and reads all diary entries from the file.
       
        if not os.path.exists(self.filename):
            print("No diary entries found.")
            return []


        with open(self.filename, 'rb') as file:
            entries = file.readlines()  # Read all lines from the file

        decrypted_entries = []
        for entry in entries:
            decrypted_entries.append(self.cipher.decrypt(entry).decode())  # Decrypt each entry

        return decrypted_entries  # Return the list of decrypted entries

def main(): # `main` function is the entry point of the SecretDiary application.
    
    diary = SecretDiary()  # Create an instance of SecretDiary

    while True:
        print("\nSecret Diary")
        print("1. Write Entry")
        print("2. Read Entries")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            diary_entry = input("Enter your diary entry: ")
            diary.write_entry(diary_entry)  # Write the entry
            print("Entry saved successfully.")

        elif choice == '2':
            entries = diary.read_entries()  # Read diary entries
            if entries:
                print("Your Diary Entries:")
                for idx, entry in enumerate(entries):
                    print(f"{idx + 1}: {entry}")
            else:
                print("No entries found.")

        elif choice == '3':
            print("Exiting Secret Diary. Goodbye!")
            break  # Exit the loop

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()  # Run the main function




