from cryptography.fernet import Fernet
import os


class SecretDiary:
    def __init__(self, filename='diary.txt'):
        """Initialize the Secret Diary with a key and a file for diary entries."""
        self.filename = filename
        self.key = self.load_or_create_key()  # Load or create a new encryption key
        self.cipher = Fernet(self.key)  # Create a Fernet cipher object


    def load_or_create_key(self):
        """Load an encryption key from a file or create a new one."""
        key_file = 'secret.key'
        if os.path.exists(key_file):
            with open(key_file, 'rb') as file:
                return file.read()  # Load existing key
        else:
            key = Fernet.generate_key()  # Generate a new key
            with open(key_file, 'wb') as file:
                file.write(key)  # Save the new key to a file
            return key


    def write_entry(self, entry):
        """
        Write an encrypted diary entry to the file.


        Args:
            entry (str): The diary entry to write.
        """
        encrypted_entry = self.cipher.encrypt(entry.encode())  # Encrypt the entry
        with open(self.filename, 'ab') as file:
            file.write(encrypted_entry + b'\n')  # Save the encrypted entry


    def read_entries(self):
        """Read and decrypt all diary entries from the file."""
        if not os.path.exists(self.filename):
            print("No diary entries found.")
            return []


        