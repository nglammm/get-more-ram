import tkinter as tk
from pathlib import Path
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter.font as tkFont

def load_text_from_file(file_path, text_widget):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            text_widget.insert(tk.END, content)  # Insert the content into the text widget
    except Exception as e:
        text_widget.insert(tk.END, f"Error loading file: {e}")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets2\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("How this works?")
window.iconbitmap('RAM.ico')
window.geometry("500x300")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 300,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    249.0,
    32.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: quit(),
    relief="flat"
)
button_1.place(
    x=179.0,
    y=264.0,
    width=143.0,
    height=26.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: quit(),
    relief="flat"
)
button_2.place(
    x=452.04669189453125,
    y=12.0,
    width=33.0,
    height=33.0
)

text_widget = ScrolledText(canvas, wrap=tk.WORD, width=58, height=11)
text_widget.place(x=10, y=65)

custom_font = tkFont.Font(family="Helvetica", size=11)
text_widget.configure(font=custom_font)

file_path = "definition.txt"  # Replace with your actual file path
load_text_from_file(file_path, text_widget)
text_widget.config(state=tk.DISABLED)

window.resizable(False, False)
window.mainloop()
