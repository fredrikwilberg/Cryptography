from tkinter import *
from Cypher_with_secret_key import cypher
import Cypher_with_secret_key as CWSK
import tkinter.messagebox


def secret_message(entry_1):
    encrypted_message = entry_1
    secret_key = entry_2.get()
    print("Hello", entry_1, entry_2.get())

    # label_3 = Label(root, text=entry_1)
    # label_3.grid(row=4)
    cypher(encrypted_message, secret_key, label_3)


def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"


def copy_text_to_clipboard(message):
    root.clipboard_clear()
    root.clipboard_append(message)


def _quit():
    root.quit()
    root.destroy()
    exit()


def _about():
    tkinter.messagebox.showinfo('About', 'Created by Fredrik Davanger Wilberg')


root = Tk()

# Title
root.title('Cypher')

# Icon

root.iconbitmap('C:\\Users\\fredrik.wilberg\\Python - MasterClass\\Cryptography\\secure_icon.ico')

# Menu bar
menu = Menu(root)
root.config(menu=menu)

# File
fileMenu = Menu(menu, tearoff=0)
fileMenu.add_command(label="Quit", command=_quit)
menu.add_cascade(label="File", menu=fileMenu)

# About
helpMenu = Menu(menu, tearoff=0)
helpMenu.add_command(label="About", command=_about)
menu.add_cascade(label="Help", menu=helpMenu)


# Header
header = Label(root, text='Encryption', bg='black', fg='white')
header.grid(row=0, column=1, sticky="ew")


# Message
label_1 = Label(root, text='Message')
label_1.grid(row=1)
entry_1 = Text(root, height=3, width=26, relief=RIDGE, borderwidth=2, highlightcolor='#82CAFF')
entry_1.grid(row=1, column=1)
entry_1.bind("<Tab>", focus_next_widget)


# KEY
label_2 = Label(root, text='Key (Hexadecimal)')
label_2.grid(row=3)
entry_2 = Entry(root, show='*')
entry_2.grid(row=3, column=1)

# Button
button_1 = Button(root, text='Encrypt Message', command=lambda: secret_message(entry_1.get("1.0",'end-1c')))
button_1.grid(row=4, column=1)

# Encrypted Message
label_3 = Label(root, text='')
label_3.grid(row=6, columnspan=4)

# Clipboard button
button_2 = Button(root, text='Copy Message', command=lambda:copy_text_to_clipboard(CWSK.message))
button_2.grid(row=5, column=1)


# Size of the screen
root.minsize(width=150, height=150)
root.geometry('400x225+800+400')


root.mainloop()
