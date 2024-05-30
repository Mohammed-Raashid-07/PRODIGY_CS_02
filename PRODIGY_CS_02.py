import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Global path and key
path = r'python.jpg'   # here enter the path of the image which you want to encrypt/decrypt .
key = 0


# Function to update the image display
def update_image():
    try:
        img = Image.open(path)
        img = img.resize((600, 400), Image.LANCZOS)  # Using LANCZOS for high-quality downsampling
        img = ImageTk.PhotoImage(img)
        canvas.itemconfig(image_container, image=img)
        canvas.image = img
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Function for encryption
def encrypt_image():
    global key
    try:
        key = int(key_entry.get())
        with open(path, 'rb') as fin:
            image = fin.read()

        image = bytearray(image)
        for index, values in enumerate(image):
            image[index] = values ^ key

        with open(path, 'wb') as fout:
            fout.write(image)

        update_image()
        status_label.config(text="Encryption Done...")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Function for decryption
def decrypt_image():
    global key
    try:
        key = int(key_entry.get())
        with open(path, 'rb') as fin:
            image = fin.read()

        image = bytearray(image)
        for index, values in enumerate(image):
            image[index] = values ^ key

        with open(path, 'wb') as fout:
            fout.write(image)

        update_image()
        status_label.config(text="Decryption Done...")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create main window
root = tk.Tk()
root.title("Image Encryptor/Decryptor")
root.geometry("800x600")

# Create a canvas to display the image
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

# Load and display the image
img = Image.open(path)
img = img.resize((600, 400), Image.LANCZOS)  # Using LANCZOS for high-quality downsampling
img = ImageTk.PhotoImage(img)
image_container = canvas.create_image(300, 200, image=img)

# Entry for the key
key_label = tk.Label(root, text="This is the Image we are encrypting/decrypting. \n \nEnter Key:")
key_label.pack(pady=5)
key_entry = tk.Entry(root)
key_entry.pack(pady=5)

# Buttons for encryption and decryption
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_image)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_image)
decrypt_button.pack(pady=5)

# Status label
status_label = tk.Label(root, text="")
status_label.pack(pady=20)

# Run the application
root.mainloop()

# end of the code