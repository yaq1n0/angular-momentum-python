# all functions

# imports
from tkMessageBox import showinfo
from PIL import Image
from PIL import ImageTk
from myclasses import ToolTip


# CreateToolTip function for ToolTip object
# code from 'https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python'
def CreateToolTip(widget, text):
    # instantizing toolTip instance of ToolTip class
    toolTip = ToolTip(widget)

    # binding enter event to showtip method
    def enter(event):
        toolTip.showtip(text)

    # binding leave event to hidetip method
    def leave(event):
        toolTip.hidetip()

    # binging enter and leave
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


# PlaceHolder function for whatever
def PlaceHolder():
    showinfo('placeholder', 'feature to be added or enabled in later version')


# creating MyImage
def CreateImage(path, x, y):
    img_open = Image.open(path)
    img_resized = img_open.resize((x, y), Image.ANTIALIAS)
    img_Tk = ImageTk.PhotoImage(img_resized)
    return img_Tk
