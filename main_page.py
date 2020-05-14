import tkinter as tk
from first_page import *


from project_functions import *


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        header = tk.Label(self, text='Test', bg='black', fg='white')
        header.grid(row=0, column=1, sticky="ew")

        # label = tk.Label(self, text="Page 1")
        # label.grid(row = 2, column = 2)

        # Message
        label_1 = tk.Label(self, text='Message')
        label_1.grid(row=1)
        entry_1 = tk.Text(self, height=3, width=26, relief="ridge", borderwidth=2, highlightcolor='#82CAFF')
        entry_1.grid(row=1, column=1)
        entry_1.bind("<Tab>", focus_next_widget)

        # KEY
        label_2 = tk.Label(self, text='Key')
        label_2.grid(row=3)
        entry_2 = tk.Entry(self)
        entry_2.grid(row=3, column=1)

        # Button
        button_1 = tk.Button(self, text='Encrypt Message', command=lambda: secret_message(entry_1.get("1.0", 'end-1c')))
        button_1.grid(row=4, column=1)

        # Encrypted Message
        label_3 = tk.Label(self, text='')
        label_3.grid(row=6, columnspan=4)

        # Clipboard button
        button_2 = tk.Button(self, text='Copy Message', command=lambda: copy_text_to_clipboard(CWSK.message))
        button_2.grid(row=5, column=1)



