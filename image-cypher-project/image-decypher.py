from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, filedialog, messagebox, Label
import numpy as np
from PIL import Image, ImageTk
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/deathday/PycharmProjects/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def xor_decrypt(image_path, key, output_path):
    # Open file for reading purpose
    with open(image_path, 'rb') as fin:
        # Storing image data in variable "image"
        image = fin.read()
    
    # Converting image into byte array to perform decryption easily on numeric data
    image = bytearray(image)

    # Convert key to bytes and resize to match the image length
    key_bytes = np.frombuffer(key.encode(), dtype=np.uint8)
    key_repeated = np.resize(key_bytes, len(image))

    # Performing XOR operation on each value of bytearray
    decrypted_image = np.bitwise_xor(image, key_repeated)

    # Opening file for writing purpose
    with open(output_path, 'wb') as fout:
        # Writing decrypted data in image
        fout.write(decrypted_image)

    print('Decryption Done...')


def get_next_filename(directory, base_filename, extension):
    i = 1
    while True:
        filename = f"{base_filename}_{i}.{extension}"
        if not os.path.exists(os.path.join(directory, filename)):
            return filename
        i += 1


def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        global encrypted_image_path
        encrypted_image_path = file_path
        
        # Display GIF as placeholder
        gif_path = "image-cypher-project/images/encryption-gif.gif"
        gif_image = Image.open(gif_path)
        
        # Resize gif to fit within 400x400 while maintaining aspect ratio
        gif_image.thumbnail((400, 400), Image.LANCZOS)
        
        # Create a new image with white background
        background = Image.new('RGB', (400, 400), (255, 255, 255))
        background.paste(
            gif_image, (int((400 - gif_image.width) / 2), int((400 - gif_image.height) / 2))
        )
        
        gif_image_tk = ImageTk.PhotoImage(background)
        canvas.create_image(305, 368, image=gif_image_tk, anchor="center")
        canvas.image = gif_image_tk


def decrypt_image():
    if not encrypted_image_path:
        messagebox.showerror("Error", "No file uploaded!")
        return

    key = entry_1.get()
    if not key:
        messagebox.showerror("Error", "No key provided!")
        return

    # Define output path for decrypted image
    directory = '/Users/deathday/Desktop/intro_to_python/Python-projects/image-cypher-project/images'
    filename = get_next_filename(directory, 'decrypted_image', 'jpeg')
    output_path = os.path.join(directory, filename)

    xor_decrypt(encrypted_image_path, key, output_path)
    
    decrypted_image = Image.open(output_path)
    
    # Resize image to fit within 400x400 while maintaining aspect ratio
    decrypted_image.thumbnail((400, 400), Image.LANCZOS)
    
    # Create a new image with white background
    background = Image.new('RGB', (400, 400), (255, 255, 255))
    background.paste(
        decrypted_image, (int((400 - decrypted_image.width) / 2), int((400 - decrypted_image.height) / 2))
    )
    
    decrypted_image_tk = ImageTk.PhotoImage(background)
    canvas.create_image(1248, 368, image=decrypted_image_tk, anchor="center")
    canvas.image = decrypted_image_tk

    messagebox.showinfo("Success", f"Image decrypted and saved as {filename}")


window = Tk()

window.geometry("1553x757")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=757,
    width=1553,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    105.0,
    168.0,
    505.0,
    568.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    1048.0,
    168.0,
    1448.0,
    568.0,
    fill="#D9D9D9",
    outline="")

button_1 = Button(
    text="File Upload",
    borderwidth=0,
    highlightthickness=0,
    command=upload_file,
    relief="flat",
    bg="#D9D9D9",
    fg="#000000",
    font=("Inter SemiBold", 14)
)
button_1.place(
    x=105.0,
    y=624.0,
    width=400.0,
    height=46.0
)

button_2 = Button(
    text="Decrypt",
    borderwidth=0,
    highlightthickness=0,
    command=decrypt_image,
    relief="flat",
    bg="#FF4081",
    fg="#FFFFFF",
    font=("Inter SemiBold", 14)
)
button_2.place(
    x=1049.0,
    y=623.0,
    width=400.0,
    height=48.0
)

entry_1 = Entry(
    bd=0,
    bg="#F7F7F7",
    fg="#000716",
    highlightthickness=0,
    font=("Inter SemiBold", 14)
)
entry_1.place(
    x=586.0,
    y=516.0,
    width=380.0,
    height=46.0
)

canvas.create_text(
    698.0,
    350.0,
    anchor="nw",
    text="decryption",
    fill="#2C2C2C",
    font=("Inter SemiBold", 30 * -1)
)

canvas.create_rectangle(
    674.0,
    400.0,
    881.0,
    402.0,
    fill="#000000",
    outline="")

canvas.create_text(
    105.0,
    59.0,
    anchor="nw",
    text="XOR Image Decryption",
    fill="#161616",
    font=("Inter Bold", 40 * -1)
)

encrypted_image_path = ""

window.resizable(False, False)
window.mainloop()
