import tkinter as tk
from Cypher_with_secret_key import cypher


def secret_message(entry_1):
    encrypted_message = entry_1
    secret_key = entry_2.get()
    print("Hello", entry_1, entry_2.get())

    # label_3 = Label(root, text=entry_1)
    # label_3.grid(row=4)
    cypher(encrypted_message, secret_key, label_3)


def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")


def copy_text_to_clipboard(message):
    root.clipboard_clear()
    root.clipboard_append(message)