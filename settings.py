

from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage



window = Tk()
window.title("Settings - Coming soon")
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
canvas.create_text(
    162.0,
    135.0,
    anchor="nw",
    text="Coming soon...",
    fill="#000000",
    font=("Inter", 25 * -1)
)
window.resizable(False, False)
window.mainloop()
