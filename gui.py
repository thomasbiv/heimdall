import tkinter as tk
from tkinter import StringVar
import heimdall
from tkinter import filedialog
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk

#import csv

def on_select(value):
    if value == "1. Encrypt a file":
        option_one(value)
    elif value == "2. Create a new password file":
        option_two(value)
    elif value == "3. Decrypt a file":
        option_three(value)
    elif value == "4. Add to a password file":
        option_four(value)
    elif value == "5. View password file contents":
        option_five(value)
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
        filetypes=[("CSV files", ".csv")]
    )
    if file_path:
        message = tk.Label(window, text=f"File Selected, you chose:\n{file_path}", font=("Arial", 12))
        message.pack(pady=(20, 10))
        print("Selected file:", file_path)

        #encrypt_button = tk.Button(window, text="Encrypt", command=lambda:heimdall.encrypt(mykey, key, file_path))
        encrypt_button = tk.Button(window, text="Encrypt", command=run_backend_encrypt(value, mykey, key, file_path))
        encrypt_button.pack(pady=10)

    back_button = tk.Button(window, text="Go Back", command=reset_ui)
    back_button.pack(pady=10)

def option_two(value):
    for widget in window.winfo_children():
        widget.destroy() 

    selected_folder = filedialog.askdirectory(title="Select the location for where your file will be created")
    if selected_folder:
        message = tk.Label(window, text=f"Folder Selected, you chose:\n{selected_folder}", font=("Arial", 12))
        message.pack(pady=(20, 10))

        message = tk.Label(window, text="Click here to create a new password file.", font=("Arial", 14))
        message.pack(pady=(20, 10))

        #check if file exists here
        result = heimdall.check_file_exists(selected_folder)
        if result == "dec":
            proceed = messagebox.askyesno("Warning!", "It looks like you already have an existing password file in this location. Creating a new password file will delete all contents from the current one saved on your computer. Would you still like to continue?")
            if not proceed:
                return reset_ui()
        elif result == "new":
            proceed = messagebox.askyesno("Warning!", "It looks like you already have an existing password file in this location. Creating a new password file will delete all contents from the current one saved on your computer. Would you still like to continue?")
            if not proceed:
                return reset_ui()
        elif result == "enc":
            proceed = messagebox.askyesno("Warning!", "It looks like you already have an existing password file in this location. Creating a new password file will delete all contents from the current one saved on your computer. Would you still like to continue?")
            if not proceed:
                return reset_ui()

        #create_button = tk.Button(window, text="Create", command=lambda:heimdall.create_password_file(selected_folder))
        create_button = tk.Button(window, text="Create", command=run_backend_create(value, selected_folder))
        create_button.pack(pady=10)   

        back_button = tk.Button(window, text="Go Back", command=reset_ui)
        back_button.pack(pady=10)
    else:
        message = tk.Label(window, text=f"No folder was selected", font=("Arial", 12))
        reset_ui()
    
def option_three(value):
    for widget in window.winfo_children():
        widget.destroy()

    message = tk.Label(window, text="Please navigate to file you wish to decrypt", font=("Arial", 14))
    message.pack(pady=(20, 10))
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("CSV files", ".csv")]
    )
    if file_path:
        message = tk.Label(window, text=f"File Selected, you chose:\n{file_path}", font=("Arial", 12))
        message.pack(pady=(20, 10))
        print("Selected file:", file_path)

        #decrypt_button = tk.Button(window, text="Decrypt", command=lambda:heimdall.decrypt(file_path))
        decrypt_button = tk.Button(window, text="Decrypt", command=run_backend_decrypt(value, file_path))
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
        filetypes=[("CSV files", ".csv")]
    )

    if file_path:
        for widget in window.winfo_children():
            widget.destroy()

        message = tk.Label(window, text=f"File Selected, you chose:\n{file_path}", font=("Arial", 12))
        message.pack(pady=(20, 10))
        print("Selected file:", file_path)

        if "enc" in file_path:
            cancel_message = tk.Label(window, text="Cannot edit this file. File encrypted.", font=("Arial", 12), fg="red")
            cancel_message.pack(pady=(10, 10))

            back_button = tk.Button(window, text="Go Back", command=reset_ui)
            back_button.pack(pady=10)
            return

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
            #heimdall.add_password_data(file_path, website, email, username, password)  # Assuming heimdall is defined
            run_backend_add(value, file_path, website, email, username, password)  # Assuming heimdall is defined

        submit_button = tk.Button(window, text="Done", command=on_done)
        submit_button.pack(pady=10)

    back_button = tk.Button(window, text="Go Back", command=reset_ui)
    back_button.pack(pady=10)

def option_five(value):
    for widget in window.winfo_children():
        widget.destroy()

    message = tk.Label(window, text="Please navigate to file you wish to edit", font=("Arial", 14))
    message.pack(pady=(20, 10))

    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("CSV files", ".csv")]
    )

    if not file_path:
        cancel_message = tk.Label(window, text="No file selected.", font=("Arial", 12), fg="red")
        cancel_message.pack(pady=(10, 10))

        back_button = tk.Button(window, text="Go Back", command=reset_ui)
        back_button.pack(pady=10)
        return
    
    filter_var = tk.StringVar()

    def load_data(website_filter=None):
        for widget in window.winfo_children():
            widget.destroy()

        message = tk.Label(window, text=f"File Selected, you chose:\n{file_path}", font=("Arial", 12))
        message.pack(pady=(10, 5))
        print("Selected file:", file_path)

        # Filter entry
        filter_frame = tk.Frame(window)
        filter_frame.pack(pady=5)

        tk.Label(filter_frame, text="Filter by website:").pack(side=tk.LEFT, padx=(0, 5))
        filter_entry = tk.Entry(filter_frame, textvariable=filter_var)
        filter_entry.pack(side=tk.LEFT)

        def apply_filter():
            load_data(website_filter=filter_var.get())

        #####

        tk.Button(filter_frame, text="Apply Filter", command=apply_filter).pack(side=tk.LEFT, padx=5)
        tk.Button(filter_frame, text="Clear Filter", command=lambda: load_data()).pack(side=tk.LEFT)

        rows = heimdall.view_file_contents(file_path)

        if not rows:
            tk.Label(window, text="No data found in the file.", fg="red").pack()
            return
        
        header = rows[0]
        data = rows[1:]

        if website_filter:
            data = [row for row in data if website_filter.lower() in str(row[0]).lower()]  # Assumes website is at index 0

        tree = ttk.Treeview(window)
        tree.pack(fill=tk.BOTH, expand=True)

        tree["columns"] = list(range(len(header)))
        tree["show"] = "headings"

        col_widths = [len(str(h)) for h in header]
        for row in data:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(cell)))

        for i, h in enumerate(header):
            est_pixel_width = max(100, col_widths[i] * 7)
            tree.heading(i, text=h)
            tree.column(i, width=est_pixel_width)

        for row in data:
            tree.insert("", "end", values=row)

        tree.config(height=min(len(data), 20))

        def delete_selected_row():
            selected = tree.selection()
            if not selected:
                return

            selected_values = tree.item(selected[0])["values"]
            
            result = heimdall.csv_delete(selected_values, file_path)

            if result == 1:
                load_data(website_filter=filter_var.get())  # Refresh Treeview
            display_backend_remove_result(result)

        delete_button = tk.Button(window, text="Delete Selected Row", command=delete_selected_row, fg="white", bg="red")
        delete_button.pack(pady=10)

        back_button = tk.Button(window, text="Go Back", command=reset_ui)
        back_button.pack(pady=10)

    load_data()

def run_backend_encrypt(value, mykey, key, file_path):
    result = 0
    if value == "1. Encrypt a file":
        result = heimdall.encrypt(mykey, key, file_path)

    # Now `result` is whatever the encrypt() function returned
    if result == 1:
        messagebox.showinfo("Success", "File encrypted successfully!")
    else:
        messagebox.showerror("Error", "Process failed.")

def run_backend_create(value, selected_folder):
    result = 0
    if value == "2. Create a new password file":
        result = heimdall.create_password_file(selected_folder)

    if result == 1:
        messagebox.showinfo("Success", "File created successfully!")
    else:
        messagebox.showerror("Error", "Process failed.")

def run_backend_decrypt(value, file_path):
    result = 0
    if value == "3. Decrypt a file":
        result = heimdall.decrypt(file_path)

    if result == 1:
        messagebox.showinfo("Success", "File decrypted successfully!")
    else:
        messagebox.showerror("Error", "Process failed.")

def run_backend_add(value, file_path, website, email, username, password):
    result = 0
    if value == "4. Add to a password file":
        result = heimdall.add_password_data(file_path, website, email, username, password) 

    if result == 1:
        messagebox.showinfo("Success", "Entry added successfully!")
    else:
        messagebox.showerror("Error", "Process failed.")

def display_backend_remove_result(result):
    if result == 1:
        messagebox.showinfo("Success", "Entry removed successfully!")
    else:
        messagebox.showerror("Error", "Process failed.")


def reset_ui():
    for widget in window.winfo_children():
        widget.destroy()

    image_lable = tk.Label(window, image=resized_image)
    image_lable.config()
    image_lable.pack(pady=20)

    title_label = tk.Label(window, text="What would you like to do?", font=("Arial", 14))
    title_label.pack(pady=(20, 10))
    #Dropdown menu
    options = ["1. Encrypt a file", "2. Create a new password file", "3. Decrypt a file", "4. Add to a password file", "5. View password file contents"]
    selected_option = StringVar()
    selected_option.set(options[0])

    dropdown = tk.OptionMenu(window, selected_option, *options, command=on_select)
    dropdown.config(width=15) 
    dropdown.pack(pady=20)



window = tk.Tk() #intantiate an instance of a window for us
window.geometry("500x500")
window.title("Heimdall Password Encryption Manager")

icon_path, words_path = heimdall.get_photos()
icon = tk.PhotoImage(file=icon_path) 
window.iconphoto(True, icon)
window.config(background="#001c2c")

logo = Image.open(words_path)
resized_image = logo.resize((400, 200))
resized_image = ImageTk.PhotoImage(resized_image) 

image_lable = tk.Label(window, image=resized_image)
image_lable.config()
image_lable.pack(pady=20)

#Title label
title_label = tk.Label(window, text="What would you like to do?", font=("Arial", 14))
title_label.pack(pady=(20, 10))
#Dropdown menu
options = ["1. Encrypt a file", "2. Create a new password file", "3. Decrypt a file", "4. Add to a password file", "5. View password file contents"]
selected_option = StringVar()
selected_option.set(options[0])

dropdown = tk.OptionMenu(window, selected_option, *options, command=on_select)
dropdown.config(width=15) 
dropdown.pack(pady=20)


window.mainloop() #place window on screen and listen for events
