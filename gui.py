import tkinter as tk
from tkinter import StringVar
import heimdall
from tkinter import filedialog
from tkinter import messagebox
from tkinter import filedialog

def on_select(value):
    if value == "1. Encrypt a file":
        option_one(value)
    elif value == "2. Create a new password file":
        option_two(value)
    elif value == "3. Decrypt a file":
        option_three(value)
    elif value == "4. Edit a password file":
        option_four(value)
    else:
        print("you should never see this")

def option_one(value):
    for widget in window.winfo_children():
        widget.destroy()

    mykey, key = heimdall.keygen()
    message = tk.Label(window, text="Please navigate to file you wish to encrypt", font=("Arial", 14))
    message.pack(pady=(20, 10))
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("Text files", "*.txt"), ("CSV files", ".csv"), ("All files", "*.*"))
    )
    if file_path:
        message = tk.Label(window, text=f"File Selected, you chose:\n{file_path}", font=("Arial", 12))
        message.pack(pady=(20, 10))
        print("Selected file:", file_path)

        encrypt_button = tk.Button(window, text="Encrypt", command=lambda:heimdall.encrypt(mykey, key, file_path))
        encrypt_button.pack(pady=10)

    back_button = tk.Button(window, text="Go Back", command=reset_ui)
    back_button.pack(pady=10)

def option_two(value):
    for widget in window.winfo_children():
        widget.destroy() 
    
    message = tk.Label(window, text="Click here to create a new password file.", font=("Arial", 14))
    message.pack(pady=(20, 10))

    create_button = tk.Button(window, text="Create", command=lambda:heimdall.create_password_file())
    create_button.pack(pady=10)   

    back_button = tk.Button(window, text="Go Back", command=reset_ui)
    back_button.pack(pady=10)


def option_three(value):
    for widget in window.winfo_children():
        widget.destroy()

    message = tk.Label(window, text="Please navigate to file you wish to decrypt", font=("Arial", 14))
    message.pack(pady=(20, 10))
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("Text files", "*.txt"), ("CSV files", ".csv"), ("All files", "*.*"))
    )
    if file_path:
        message = tk.Label(window, text=f"File Selected, you chose:\n{file_path}", font=("Arial", 12))
        message.pack(pady=(20, 10))
        print("Selected file:", file_path)

        decrypt_button = tk.Button(window, text="Decrypt", command=lambda:heimdall.decrypt(file_path))
        decrypt_button.pack(pady=10)
    
    back_button = tk.Button(window, text="Go Back", command=reset_ui)
    back_button.pack(pady=10)

def option_four(value):
    for widget in window.winfo_children():
        widget.destroy()

    message = tk.Label(window, text="Please navigate to file you wish to edit", font=("Arial", 14))
    message.pack(pady=(20, 10))

    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("Text files", "*.txt"), ("CSV files", ".csv"), ("All files", "*.*"))
    )

    if file_path:
        for widget in window.winfo_children():
            widget.destroy()

        message = tk.Label(window, text=f"File Selected, you chose:\n{file_path}", font=("Arial", 12))
        message.pack(pady=(20, 10))
        print("Selected file:", file_path)

        tk.Label(window, text="Please enter the site's name (one word)", font=("Arial", 12)).pack(pady=(10, 5))
        website_entry = tk.Entry(window, width=30)
        website_entry.pack(pady=5)

        tk.Label(window, text="Enter the email associated with the account", font=("Arial", 12)).pack(pady=(10, 5))
        email_entry = tk.Entry(window, width=30)
        email_entry.pack(pady=5)

        tk.Label(window, text="Enter the username", font=("Arial", 12)).pack(pady=(10, 5))
        username_entry = tk.Entry(window, width=30)
        username_entry.pack(pady=5)

        tk.Label(window, text="Enter the password", font=("Arial", 12)).pack(pady=(10, 5))
        password_entry = tk.Entry(window, width=30)
        password_entry.pack(pady=5)

        def on_done():
            website = website_entry.get()
            email = email_entry.get()
            username = username_entry.get()
            password = password_entry.get()
            heimdall.add_password_data(website, email, username, password)  # Assuming heimdall is defined

        submit_button = tk.Button(window, text="Done", command=on_done)
        submit_button.pack(pady=10)

    back_button = tk.Button(window, text="Go Back", command=reset_ui)
    back_button.pack(pady=10)


def reset_ui():
    for widget in window.winfo_children():
        widget.destroy()

    title_label = tk.Label(window, text="What would you like to do?", font=("Arial", 14))
    title_label.pack(pady=(20, 10))
    #Dropdown menu
    options = ["1. Encrypt a file", "2. Create a new password file", "3. Decrypt a file", "4. Edit a password file"]
    selected_option = StringVar()
    selected_option.set(options[0])

    dropdown = tk.OptionMenu(window, selected_option, *options, command=on_select)
    dropdown.config(width=15) 
    dropdown.pack(pady=20)



window = tk.Tk() #intantiate an instance of a window for us
window.geometry("500x500")
window.title("Heimdall Password Encryption Manager")

#icon = PhotoImage(file='path of image in proj folder.png') #come back to this once i want to set a logo
#window.iconphoto(True, icon)
window.config(background="#237ACB")

#Title label
title_label = tk.Label(window, text="What would you like to do?", font=("Arial", 14))
title_label.pack(pady=(20, 10))
#Dropdown menu
options = ["1. Encrypt a file", "2. Create a new password file", "3. Decrypt a file", "4. Edit a password file"]
selected_option = StringVar()
selected_option.set(options[0])

dropdown = tk.OptionMenu(window, selected_option, *options, command=on_select)
dropdown.config(width=15) 
dropdown.pack(pady=20)


window.mainloop() #place window on screen and listen for events
