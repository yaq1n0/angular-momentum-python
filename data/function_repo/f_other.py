# other functions

# imports
from tkMessageBox import showinfo

from math import pi

from PIL import Image, ImageTk

from data.myvariables import spoke_width


# PlaceHolder function for whatever
def PlaceHolder():
    showinfo('placeholder', 'feature to be added or enabled in later version')


# create greyscale hex
def GrayScale(num):
    if 0 <= num <= 255 and type(num) == int:
        h_num = hex(num)
        h_num_str = str(h_num)

        if len(h_num_str) == 3:
            num3 = "0" + h_num_str[-1]

        elif len(h_num_str) == 4:
            num3 = h_num_str[-2] + h_num_str[-1]

        else:
            num3 = "fucky wucky"

        return '#' + str(num3) + str(num3) + str(num3)


# CreateToolTip function for ToolTip object
# code from 'https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python'
def CreateToolTip(widget, text):
    from data.myclasses import ToolTip
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


# create Tk-compatible image
def CreateTkImage(path, x_size, y_size):
    img_open = Image.open(path)
    img_resized = img_open.resize((x_size, y_size), Image.ANTIALIAS)
    img_Tk = ImageTk.PhotoImage(img_resized)
    return img_Tk


# convert degrees to radians
def dtr(theta):
    tmpvar = pi / 180.0
    return float(theta) * float(tmpvar)


# convert angular velocity to frequency
def rtf(rad):
    tmpvar = 2.0 * pi
    return float(rad) / float(tmpvar)


# convert frequency to angular_velocity
def ftr(freq):
    tmpvar = 2.0 * pi
    return float(tmpvar) * float(freq)


# convert angular velocity into linear velocity
def atl(ang_vel, radius):
    return float(ang_vel) * float(radius)
