

def cypher(encrypted_message, secret_key, label_3):
    # encrypted_message = input('What is the encrypted message? ')
    # secret_key = input('What is the Secret Key? ')
    global message

    message = ''

    secret_key = int(secret_key, 16)
    secret_key = str(secret_key)

    if len(encrypted_message) > len(secret_key):
        n = round(len(encrypted_message) / len(secret_key))
        for j in range(0, n):
            secret_key = secret_key + secret_key

    for i in range(0, len(encrypted_message)):
        key_number = secret_key[i]
        key_number = int(key_number)

        character = encrypted_message[i]

        character = ord(character)
        character = character - key_number
        character = chr(character)
        message = message + character

    print("The message is: ", message)

    label_3.configure(state="disabled")
    label_3.config(text="The message is: " + message)

    label_3.configure(state='normal')
    return message









"""

    print("The message is: ", message)
    message = "The message is: " + message

    label_3.configure(state="disabled")
    label_3.config(text=message)
    #   label_3.configure(bg=root.cget('bg'), relief=FLAT)

    label_3.configure(state='normal')
    return message
"""








'''
if g == 1:
    label_3 = Label(root, text=message)
    label_3.grid(row=6, columnspan=4)
    g = g + 1
    Print("IF")
else:
    label_3.destroy()
    label_3 = Label(root, text=message)
    label_3.grid(row=6, columnspan=4)
    Print("else")
'''
'''
try:
    label_3.destroy()
    label_3 = Label(root, text=message)
    label_3.grid(row=6, columnspan=4)
    print("try")
except UnboundLocalError:
    label_3 = Label(root, text=message)
    label_3.grid(row=6, columnspan=4)
    print("except")
else:
    label_3.destroy()
    label_3 = Label(root, text=message)
    label_3.grid(row=6, columnspan=4)
    print("else")
'''