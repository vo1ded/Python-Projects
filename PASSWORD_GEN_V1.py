import random
from tkinter import *

def create_input(label, row):
    label = Label(root, text = label)
    entry = Entry(root, width = 50)
    label.grid(row = row, column = 0, padx = 30, pady = 20 )
    entry.grid(row = row, column = 1, padx = 0, pady = 20 )
    return entry

def update_alphabet(new_alph):
    lower = [i for i in new_alph if i.islower()]
    upper = [i for i in new_alph if i.isupper()]
    special = [i for i in new_alph if not i.isalpha()]
    return new_alph, lower, upper, special

def is_int(label):
    return label.get().isdigit()

alphabet, lower, upper, special = update_alphabet("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+-./:;<=>?@[\]_{|}~")

root = Tk()
root.title("Password Generator")
root.geometry("500x500")

title = Label(root, text = "Password Generator", font=('Arial 15'))
title.grid(row = 0, column = 1, pady = 20)

length_input = create_input("Password Length",1)
lower_input = create_input("Min Lowercase",2)
upper_input = create_input("Min Uppercase",3)
special_input = create_input("Min Special/Num",4)
alphabet_input = create_input("Possible Letters",5)

alphabet_input.insert(END, "".join(alphabet))

password_val = StringVar()
password_val.set("")

password_label = Label(root, textvariable = password_val, font=('Arial 15'))
password_label.grid(row = 6, column = 0, pady = 20)

def generate_pass():
    # define inputs to be checked
    check_inputs = [length_input, lower_input, upper_input, special_input]
    check_labels = ["Length", "Minimum Lowercase", "Minimum Uppercase", "Minimum Special"]
    
    # check for invalid input
    for i, inpt in enumerate(check_inputs):
        if not is_int(inpt):
            password_val.set(f"Invalid {check_labels[i]} Input")
            return
    if not alphabet_input.get():
        password_val.set("Invalid Options Input")
        return

    # get the new inputted alphabet
    alphabet, lower_alph, upper_alph, special_alph = update_alphabet(alphabet_input.get())
    # convert input box input into integers
    length_int, lower_int, upper_int, special_int = map(int, (length_input.get(), lower_input.get(), upper_input.get(), special_input.get()))

    # create copy of original alphabet
    letters = alphabet[:]
    generated = ""
    
    while length_int:
        # set new letters to use depending on min of the types
        if length_int == max(0, lower_int) + max(0, upper_int) + max(0, special_int):
            letters = lower_alph if lower_int > 0 else [] \
                    + upper_alph if upper_int > 0 else [] \
                    + special_alph if special_int > 0 else []
        letter = random.choice(letters)
        generated += letter

        # decrease min of type added
        if letter.isupper():
            upper_int -= 1
        elif letter.islower():
            lower_int -= 1
        elif not letter.isalnum():
            special_int -= 1
         
        length_int -= 1
    
    password_val.set(generated)

generate = Button(root, text="Generate", command=generate_pass)
generate.grid(row = 6, column = 1, padx = 30, pady = 20)

root.mainloop()

    
