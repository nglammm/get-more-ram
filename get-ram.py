

import sys

batch_file = sys.argv[1]

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import threading
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets1\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


root = Tk()
root.title("Install RAM")
root.iconbitmap('RAM.ico')
root.geometry("300x200")
root.configure(bg = "#FFFFFF")

def show_text(text_widget):
    text_widget.place(x=10, y=140)
    content = text_widget.get("1.0", tk.END)  # Get all text from the widget
    
    
# Function to run the batch file and capture its output
def run_batch_file(batch_file, text_widget, progress_bar):
    process = subprocess.Popen(
        batch_file,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        universal_newlines=True,
        creationflags=subprocess.CREATE_NO_WINDOW
    )

    total_lines = 0

    # Function to read the output from stdout
    def read_output(stream, text_widget):
        nonlocal total_lines
        for line in iter(stream.readline, ''):
            if line.strip():
                text_widget.insert(tk.END, line)
                text_widget.see(tk.END)
                total_lines += 1
                progress_bar['value'] = (total_lines / expected_lines) * 100  # Update progress bar
                progress_bar.update()
        
        stream.close()

    # Count expected lines (you can adjust this based on your batch file)
    expected_lines = 8  # Set this to an estimated number of lines in the output

    # Start a thread to read stdout
    stdout_thread = threading.Thread(target=read_output, args=(process.stdout, text_widget))
    stdout_thread.start()

    # Wait for the process to complete
    process.wait()
    stdout_thread.join()

    # Wait for 2 seconds then close the root
    root.after(2000, root.destroy)


canvas = Canvas(
    root,
    bg = "#FFFFFF",
    height = 200,
    width = 300,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    152.0,
    37.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_text(text_widget),
    relief="flat"
)
button_1.place(
    x=88.0,
    y=110.0,
    width=123.0,
    height=19.0
)
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(pady=10)

progress_bar = ttk.Progressbar(canvas, length=250, mode='determinate', maximum=100)
progress_bar.place(
    x=25.0,
    y=70.0)

# Add a smaller ScrolledText widget to display the output


text_widget = ScrolledText(canvas, wrap=tk.WORD, width=33, height=3)

text_widget.pack_forget()

# Automatically run the batch file on startup
threading.Thread(target=run_batch_file, args=(batch_file, text_widget, progress_bar)).start()

root.mainloop()
