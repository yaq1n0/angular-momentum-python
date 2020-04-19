# other functions

# imports
from tkMessageBox import showinfo
from math import pi, sin, cos
from PIL import Image, ImageTk
from data.myclasses import ToolTip
from data.variables import spoke_width


# PlaceHolder function for whatever
def PlaceHolder():
    showinfo('placeholder', 'feature to be added or enabled in later version')


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


# line at theta degrees from x_pos, y_pos to x, y (for animate_rotating_circle)
def ttl(canvas, x_pos, y_pos, radius, theta):
    x = x_pos + (float(radius) * sin(dtr(theta)))
    y = y_pos + (float(-radius) * cos(dtr(theta)))
    return canvas.create_line(x_pos, y_pos, x, y, width=spoke_width)
