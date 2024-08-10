from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import psutil
import ctypes
import sys
import threading
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
import webbrowser
import tkinter.font as tkFont
#Check for admin to work.


if ctypes.windll.shell32.IsUserAnAdmin() == 0:
    messagebox.showerror("Error","Run this app in administrator in order to work.")
    sys.exit(1)
    
ram = psutil.virtual_memory()

with open('data.txt','w') as f:
    f.write('0')
        
# Print RAM total, used, and available in GB
print(f"Total RAM: {ram.total / (1024.0 **3):.2f} GB")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

def open_lam():
    
    webbrowser.open('http://mrlam.us.to/thanks')

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def add_ram4gb(): #write data to file for others to read
    with open('data.txt','w') as f:
        f.write('4')
        
def add_ram8gb():
    with open('data.txt','w') as f:
        f.write('8')

def add_ram16gb():
    with open('data.txt','w') as f:
        f.write('16')

def confirm():
    
    with open('data.txt','r') as f:
        gb = str(f.read())
        
    if gb == "0":
        messagebox.showerror("Error","Choose the GB you want first before getting it.")
    else:
        
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        result = subprocess.run('python get-ram.py ' + gb+"gb", startupinfo=startupinfo, capture_output=True, text=True)

def how_work():
    
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    result = subprocess.run('python how-work.py', startupinfo=startupinfo, capture_output=True, text=True)

def open_settings():
    
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    result = subprocess.run('python settings.py', startupinfo=startupinfo, capture_output=True, text=True)
    
window = Tk()

window.title("Get More RAM")
window.iconbitmap('RAM.ico')
window.geometry("700x440")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 440,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    361.0,
    38.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    148.0,
    120.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    148.0,
    268.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    148.0,
    211.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    148.0,
    195.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    350.0,
    120.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    350.0,
    268.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    350.0,
    211.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    343.0,
    191.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    365.0,
    200.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    553.0,
    120.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    545.0,
    271.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    552.0,
    211.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    532.0,
    195.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    553.0,
    200.0,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    574.0,
    206.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    350.0,
    410.0,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    86.0,
    392.0,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    301.0,
    392.0,
    image=image_image_19
)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    485.0,
    392.0,
    image=image_image_20
)

image_image_21 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(
    117.0,
    416.0,
    image=image_image_21
)

image_image_22 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(
    325.0,
    416.0,
    image=image_image_22
)

image_image_23 = PhotoImage(
    file=relative_to_assets("image_23.png"))
image_23 = canvas.create_image(
    525.0,
    416.0,
    image=image_image_23
)

image_image_24 = PhotoImage(
    file=relative_to_assets("image_24.png"))
image_24 = canvas.create_image(
    192.0,
    416.0,
    image=image_image_24
)

image_image_25 = PhotoImage(
    file=relative_to_assets("image_25.png"))
image_25 = canvas.create_image(
    400.0,
    415.0,
    image=image_image_25
)
# Confirm button
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=confirm,
    relief="flat"
)
button_1.place(
    x=566.0,
    y=381.0,
    width=134.0,
    height=59.0
)

# 8gb button
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=add_ram8gb,
    relief="flat"
)
button_2.place(
    x=270.0,
    y=296.0,
    width=161.0,
    height=29.0
)
# 16gb button
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=add_ram16gb,
    relief="flat"
)
button_3.place(
    x=472.0,
    y=296.0,
    width=161.0,
    height=29.0
)

# 4gb button
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=add_ram4gb,
    relief="flat"
)
button_4.place(
    x=68.0,
    y=296.0,
    width=161.0,
    height=29.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=how_work,
    relief="flat"
)
button_5.place(
    x=581.0,
    y=15.0,
    width=41.0,
    height=41.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=open_settings,
    relief="flat"
)
button_6.place(
    x=638.0,
    y=15.0,
    width=41.0,
    height=41.0
)

image_image_26 = PhotoImage(
    file=relative_to_assets("image_26.png"))
image_26 = canvas.create_image(
    26.0,
    12.0,
    image=image_image_26
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=open_lam,
    relief="flat"
)
button_7.place(
    x=44.0,
    y=7.0,
    width=24.0,
    height=10.0
)

total_ram = round(ram.total / (1024.0 **3))# how much to add
 #added w/ options

canvas.create_text(
    63.0, # x
    401.0, # y
    anchor="nw",
    text=total_ram,
    fill="#FFFFFF",
    font=("Inter",19, "bold")
)

added_ramm = canvas.create_text(
        470.0,
        401.0,
        anchor="nw",
        text=total_ram,
        fill="#FFFFFF",
        font=("Inter",19, "bold")
    )

adde_ramm = canvas.create_text(
        270.0,
        401.0,
        anchor="nw",
        text=0,
        fill="#FFFFFF",
        font=("Inter",19, "bold")
    )

def updt():
    
    total_ram = round(ram.total / (1024.0 **3))
    with open('data.txt','r') as f:
        add_ram = int(f.read())
        added_ram = total_ram + add_ram
    if add_ram == 1:
        canvas.pack_forget()
        frame2.pack(fill="both", expand = True)
    canvas.itemconfig(added_ramm, text=added_ram)
    canvas.itemconfig(adde_ramm, text=add_ram)
    window.after(10,updt)


frame2 = tk.Frame(window, bg="white")

window.resizable(False, False)
updt()

window.mainloop()
