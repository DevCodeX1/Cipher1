from tkinter import *
from tkinter import messagebox
import tkinter as tk
import base64

window = tk.Tk()
window.geometry("420x420")
window.resizable(False, False)
window.title("Cipher")
window.configure(bg="black")
photo = PhotoImage(file = "cipher2.png")
window.iconphoto(False, photo)
def encrypt():
    password = code.get()
    if password == "1234":
        screen1 = Toplevel(window)
        screen1.title("Encryption")
        screen1.geometry("400x250")
        screen1.configure(bg="green")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text="Text is Encrypted", font="Arial 10 bold").place(x=5, y=6)
        tex2 = Text(screen1, font="30", bd=4, wrap=WORD)
        tex2.place(x=2, y=30, width=390, height=180)
        tex2.insert(END, encrypt)

    elif password == "":
        messagebox.showerror("Error", "Pleas enter the secret key")
    elif password != "1234":
        messagebox.showerror("Sorry", "Invalid Key")


def decrypt():
    password = code.get()
    if password == "1234":
        screen2 = Toplevel(window)
        screen2.title("Encryption")
        screen2.geometry("400x250")
        screen2.configure(bg="blue")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen2, text="Text is Encrypted", font="Arial 10 bold").place(x=5, y=6)
        tex2 = Text(screen2, font="30", bd=4, wrap=WORD)
        tex2.place(x=2, y=30, width=390, height=180)
        tex2.insert(END, encrypt)

    elif password == "":
        messagebox.showerror("Error", "Pleas enter the secret key")
    elif password != "1234":
        messagebox.showerror("Sorry", "Invalid Key")

def reset():
    text1.delete(1.0, END)
    code.set("")


# Label
Label(window, text="Enter the text for Encryption and Decryption:", font="Arial 12 bold", bg="red").place(x=40, y=6)
Label(window, text="Enter Secret Key:", font="Arial 13 bold").place(x=132, y=185)
# Text
text1 = Text(window, font="20")
text1.place(x=5, y=45, width=410, height=120)

# Entry
code = StringVar()
Entry(textvariable=code, bd=4, font="Arial 10", show="#").place(x=130, y=220)

# Button
Button(window, text="Encryption", font="Arial 15", bg="green", fg="black", bd=3, command=encrypt).place(x=20, y=280,
                                                                                                        width=180)
Button(window, text="Decryption", font="Arial 15", bg="red", fg="black", bd=3, command=decrypt).place(x=220, y=280,
                                                                                                      width=180)
Button(window, text="Reset", font="Arial 15", bg="blue", fg="black", bd=3, command=reset).place(x=60, y=350, width=280)
window.mainloop()
