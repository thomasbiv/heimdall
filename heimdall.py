from cryptography.fernet import Fernet
import os

print("Would you like to:")
print("1. Encrypt a file?")
print("2. Import a key that was given to you?")
print("3. Decrypt a file?")
choice = input("Please enter 1, 2 or 3: ")

if int(choice) == 1:
    #GENERATE NEW KEY
    key = Fernet.generate_key()
    with open('mykey.key', 'wb') as mykey: #create a file mykey.key with variable name mykey
        mykey.write(key) #write the key we generated to the file

    f = Fernet(key)

    #ENCRYPT FILE
    file_path = input("Please paste the full file path: ")
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


elif int(choice) == 2:
    #LOAD A KEY SOMEONE HAS SHARED
    with open('givenkey.key', 'rb') as givenkey:
        key = givenkey.read()

    #DECRYPTION CODE WOULD GO HERE


elif int(choice) == 3:
    #READ EXISTING KEY
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()

    f = Fernet(key)

    #DECRYPT FILE
    file_path = input("Please paste the full file path: ")
    try:
        # Open and read the file
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