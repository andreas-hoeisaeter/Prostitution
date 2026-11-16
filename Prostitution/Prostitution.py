import tkinter as tk
import random
from PIL import ImageTk, Image
import winsound

def append():

    global current_image_index, photo_references
    
    current_image_index = (current_image_index + 1) % len(photo_references)
    
    image_label.config(image=photo_references[current_image_index])

    text = "One nut"

    new_text = text + "\n"
    
    text_box.insert(tk.END, new_text)
    text_box.see(tk.END)

    sound = "Sound/Ba.wav"
    winsound.PlaySound(sound, winsound.SND_FILENAME)

root = tk.Tk()
root.geometry("600x600")
root.title("Prostitution 1000")
root.iconbitmap("Sex.ico")

image1 = Image.open("Pictures/Woman_model.jpg").resize((275, 400), Image.Resampling.LANCZOS)
image2 = Image.open("Pictures/Man_model.jpg").resize((275, 400), Image.Resampling.LANCZOS)

photo1 = ImageTk.PhotoImage(image1)
photo2 = ImageTk.PhotoImage(image2)

photo_references = [photo1, photo2]
current_image_index = 0

image_label = tk.Label(root, image=photo_references[current_image_index])
image_label.pack(pady=20)

text_box = tk.Text(root, height=5, width=10)
text_box.pack(pady=10)

update_button = tk.Button(root, text="Bang", command=append)
update_button.pack()

root.mainloop()
