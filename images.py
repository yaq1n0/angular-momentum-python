# images (cheatsheet and documentation)

# imports
from Tkinter import Label
from PIL import Image, ImageTk
from myvars import cheatsheet_width, cheatsheet_height, documentation_width, documentation_height


def MyImage(frame, path, x_size, y_size):
    img_open = Image.open(path)
    img_resized = img_open.resize((x_size, y_size), Image.ANTIALIAS)
    img_Tk = ImageTk.PhotoImage(img_resized)
    img_label = Label(frame, image=img_Tk)
    img_label.image = img_Tk
    img_label.place(relx=0, rely=0, relwidth=1, relheight=1)


def run_cheatsheet(frame):
    MyImage(frame, 'images/cheatsheet.jpg', cheatsheet_width, cheatsheet_height)


def run_documentation(frame):
    MyImage(frame, 'images/documentation.jpg', documentation_width, documentation_height)
