import tkinter as tk
from tkinter import StringVar
import heimdall
from tkinter import filedialog
from tkinter import messagebox

def on_select(value):
    if value == "1. Encrypt a file":
        option_one(value)
    elif value == "2. Import a key that was given to you":
        option_two(value)
    elif value == "3. Decrypt a file":
        option_three(value)
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
    
    message = tk.Label(window, text="Nothing here yet...", font=("Arial", 14))
    message.pack(pady=(20, 10))

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


def reset_ui():
    for widget in window.winfo_children():
        widget.destroy()

    title_label = tk.Label(window, text="What would you like to do?", font=("Arial", 14))
    title_label.pack(pady=(20, 10))
    #Dropdown menu
    options = ["1. Encrypt a file", "2. Import a key that was given to you", "3. Decrypt a file"]
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
options = ["1. Encrypt a file", "2. Import a key that was given to you", "3. Decrypt a file"]
selected_option = StringVar()
selected_option.set(options[0])

dropdown = tk.OptionMenu(window, selected_option, *options, command=on_select)
dropdown.config(width=15) 
dropdown.pack(pady=20)


window.mainloop() #place window on screen and listen for events
