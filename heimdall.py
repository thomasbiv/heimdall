from cryptography.fernet import Fernet
import os

def keygen():
    #GENERATE NEW KEY
    key = Fernet.generate_key()
    with open('mykey.key', 'wb') as mykey: #create a file mykey.key with variable name mykey
        mykey.write(key) #write the key we generated to the file
    
    return mykey, key

def encrypt(mykey, key, file_path):
    f = Fernet(key)
    #ENCRYPT FILE
    try:
        # Open and read the file
        with open(file_path, 'rb') as original_file:
            original = original_file.read()
    except FileNotFoundError:
        print("The file was not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

    encrypted = f.encrypt(original)

    with open('enc_grades.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    #DELETE DECRYPTED FILE
    try:
        os.remove(file_path)
        print("File deleted successfully.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied. Cannot delete the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt(file_path):
    #READ EXISTING KEY
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()

    f = Fernet(key)
    #DECRYPT FILE
    try:
        #Open and read the file
        with open(file_path, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
    except FileNotFoundError:
            print("The file was not found. Please check the path and try again.")
    except Exception as e:
            print(f"An error occurred: {e}")

    decrypted = f.decrypt(encrypted)

    with open('dec_grades.csv', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    
    #DELETE ENCRYPTED FILE
    try:
        os.remove(file_path)
        print("File deleted successfully.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied. Cannot delete the file.")
    except Exception as e:
        print(f"An error occurred: {e}")