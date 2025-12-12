from cryptography.fernet import Fernet
import os
import csv

def keygen():
    #GENERATE NEW KEY
    key = Fernet.generate_key()
    with open('mykey.key', 'wb') as mykey: #create a file mykey.key with variable name mykey
        mykey.write(key) #write the key we generated to the file
    
    return mykey, key

def encrypt(mykey, key, file_path):
    result = 0
    f = Fernet(key)
    #ENCRYPT FILE
    try:
        # Open and read the file
        with open(file_path, 'rb') as original_file:
            original = original_file.read()
    except FileNotFoundError:
        print("The file was not found. Please check the path and try again.")
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return result

    encrypted = f.encrypt(original)

    full_path = os.path.join(os.path.dirname(file_path), "enc_passwords.csv")
    with open(full_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    #DELETE DECRYPTED FILE
    try:
        os.remove(file_path)
        print("File deleted successfully.")
        result = 1
        return result
    except FileNotFoundError:
        print("File not found.")
        return result
    except PermissionError:
        print("Permission denied. Cannot delete the file.")
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return result

def decrypt(file_path):
    result = 0
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
            return result
    except Exception as e:
            print(f"An error occurred: {e}")
            return result

    decrypted = f.decrypt(encrypted)


    full_path = os.path.join(os.path.dirname(file_path), "passwords.csv")
    with open(full_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    
    #DELETE ENCRYPTED FILE
    try:
        os.remove(file_path)
        print("File deleted successfully.")
        result = 1
        return result
    except FileNotFoundError:
        print("File not found.")
        return result
    except PermissionError:
        print("Permission denied. Cannot delete the file.")
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return result

def create_password_file(selected_folder):
    result = 0
    full_path = os.path.join(selected_folder, "passwords.csv")
    header = ['website', 'email','username','password']
    with open(full_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header) #write one row / header, writerows for multiple
    result = 1
    return result

def add_password_data(file_path, website, email, username, password):
    result = 0
    new_row = [website, email, username, password]

    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_row) #write one row / header, writerows for multiple

    result = 1
    return result

def view_file_contents(file_path):
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)

        if not rows:
            return
        else:
            return rows
        
def csv_delete(selected_values, file_path):
    # Reload CSV
    with open(file_path, newline='', encoding="utf-8") as f:
        reader = list(csv.reader(f))
        header = reader[0]
        data = reader[1:]

    # Remove matching row
    if selected_values in data:
        data.remove(selected_values)

    # Save back to file
        with open(file_path, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)

        return 1
    
def check_file_exists(selected_folder):
    dec_path = os.path.join(selected_folder, "dec_passwords.csv")
    new_path = os.path.join(selected_folder, "passwords.csv")
    enc_path = os.path.join(selected_folder, "enc_passwords.csv")
    if os.path.exists(dec_path):
        result = "dec"
    elif os.path.exists(new_path):
        result = "new"
    elif os.path.exists(enc_path):
        result = "enc"
    else:
        result = "NA" 
    return result

def get_photos():
    script_dir = os.path.dirname(__file__)  # Directory of the current script
    icon_path = os.path.join(script_dir, "images", "heimdall logo.png")
    words_path = os.path.join(script_dir, "images", "heimdalllogowithwords.png")
    return icon_path, words_path
        

