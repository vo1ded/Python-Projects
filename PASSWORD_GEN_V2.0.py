import random
import string
import tkinter as tk

def get_int(button):
    return int(button.get()) if button.get().isdigit() else -1

def generate_password():
    characters = alphabet_input.get()
    length = get_int(length_input)
    
    # create lists of characters for each category from inputted characters
    categories = [
        [char for char in characters if char.islower()],
        [char for char in characters if char.isupper()],
        [char for char in characters if not char.isalnum()],
        [char for char in characters if char.isdigit()]
    ]

    inputs = [lowercase_input, uppercase_input, special_input, number_input]
    password = []

    counts = list(map(get_int, inputs))

    # check for invalid input
    if -1 in counts:
        label_text.set("Invalid Input")
        return
    
    # generate the minimum for each catagory
    for cat, count in zip(categories, counts):
        password.extend(random.choices(cat, k=count))
    
    # fill remaining characters with random characters from options
    remaining_length = length - len(password)
    if remaining_length > 0:
        password += random.choices(characters, k=remaining_length)
    
    # shuffle and join the password list into a string
    if len(password) > length:
        label_text.set("Minimum Values Exceed Length")
    else:
        random.shuffle(password)
        label_text.set("".join(password))

def copy_password():
    window.clipboard_clear()
    window.clipboard_append(label_text.get())
    window.update()

def create_input(parent, row, column, label_text):
    label = tk.Label(parent, text=label_text)
    entry = tk.Entry(parent)
    label.grid(row=row, column=column, padx=5, pady=5)
    entry.grid(row=row, column=column+1, padx=5, pady=5)
    return entry

def create_button(parent, row, column, text, command):
    button = tk.Button(parent, text=text, command=command)
    button.grid(row=row, column=column, columnspan=2, padx=5, pady=5)
    return button

def create_label(parent, row, column, textvariable):
    label = tk.Label(parent, textvariable=textvariable)
    label.grid(row=row, column=column, columnspan=2, padx=5, pady=5)
    return label

# create the Tkinter window
window = tk.Tk()
window.title("PASSWORD GENERATOR")

# add the input widgets
alphabet_input = create_input(window, 0, 0, "Characters:")
length_input = create_input(window, 1, 0, "Length:")
lowercase_input = create_input(window, 2, 0, "Min Lowercases:")
uppercase_input = create_input(window, 3, 0, "Min Uppercases:")
special_input = create_input(window, 4, 0, "Min Symbols:")
number_input = create_input(window, 5, 0, "Min Numbers:")

alphabet_input.insert(0, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+-./:;<=>?@[\]_{|}~")

button = create_button(window, 6, 0, "GENERATE", generate_password)

label_text = tk.StringVar()
label_text.set("")
label = create_label(window, 7, 0, label_text)

button = create_button(window, 8, 0, "COPY", copy_password)

window.mainloop()
