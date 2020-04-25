# other classes

# imports
from Tkinter import \
    Toplevel, Frame, Canvas, Label, Button, Scale, Entry, \
    LEFT, HORIZONTAL, FLAT, RIDGE, SOLID, StringVar, N

from data.myfunctions import GrayScale

from data.myvariables import \
    MyFont, MyFontB, canvas_relx, canvas_rely, canvas_width, canvas_height, \
    scale_relwidth, scale_relheight


# Defining Object ToolTip
# code from 'https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python'
class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    # showtip method for ToolTip class
    def showtip(self, text):
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox('insert')
        x = x + self.widget.winfo_rootx() + 60
        y = y + cy + self.widget.winfo_rooty() + 30
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry('+%d+%d' % (x, y))
        label = Label(tw, text=self.text)
        label.configure(justify=LEFT)
        label.configure(relief=SOLID, bd=1)
        label.configure(bg=GrayScale(60), fg=GrayScale(220), font=MyFont)
        label.pack(ipadx=1)

    # hidetip method for ToolTip class
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


# Creating MyObjects

# Creating MyButton
class MyButton(object):
    def __init__(self, parent, text, command, relx, rely):
        bgcolor = GrayScale(40)
        fgcolor = GrayScale(220)

        relwidth = 0.10
        relheight = 0.05

        self.button = Button(parent)
        self.button.configure(text=text, command=command)
        self.button.configure(font=MyFontB)
        self.button.configure(bg=bgcolor, fg=fgcolor)
        self.button.configure(activebackground=bgcolor, activeforeground=fgcolor)
        self.button.configure(relief=RIDGE, highlightthickness=0, bd=0)
        self.button.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)


# Creating MyImageButton
class MyImageButton(object):
    def __init__(self, parent, img, command, relx, rely):
        relwidth = 0.05 / (16.0 / 9.0)
        relheight = 0.05

        self.button = Button(parent)
        self.button.configure(image=img)
        self.button.image = img
        self.button.configure(command=command)
        self.button.configure(relief=RIDGE, highlightthickness=0, bd=0)
        self.button.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)


# Creating MyCanvas
class MyCanvas(object):
    def __init__(self, parent):
        bgcolor = GrayScale(20)

        abswidth = canvas_width
        absheight = canvas_height

        relx = canvas_relx
        rely = canvas_rely

        self.canvas = Canvas(parent)
        self.canvas.configure(bg=bgcolor)
        self.canvas.configure(width=abswidth, height=absheight)
        self.canvas.configure(relief=RIDGE, highlightthickness=0, bd=0)
        self.canvas.place(relx=relx, rely=rely)


# Creating MyEntry
class MyEntry(object):
    def __init__(self, parent, text, relx, rely):
        charwidth = 20

        bgcolor = GrayScale(20)
        fgcolor = GrayScale(220)

        self.entry = Entry(parent)
        self.entry.configure(width=charwidth)
        self.entry.configure(bg=bgcolor, fg=fgcolor)
        self.entry.configure(relief=RIDGE, highlightthickness=2, bd=0)
        self.entry.place(relx=relx, rely=rely)

        label_rely = rely - 0.045

        self.label = Label(parent)
        self.label.configure(text=text)
        self.label.configure(font=MyFont)
        self.label.configure(bg=bgcolor, fg=fgcolor)
        self.label.configure(relief=FLAT)
        self.label.configure(padx=2, pady=2)
        self.label.place(relx=relx, rely=label_rely)


# Creating MyFrame
class MyFrame(object):
    def __init__(self, parent, bgcolor):
        relx = rely = 0
        relwidth = relheight = 1

        self.frame = Frame(parent)
        self.frame.configure(bg=bgcolor)
        self.frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)


# Creating MyFrameWBP
class MyFrameWBP(object):
    def __init__(self, parent, bgcolor, frame_bottom_pad):
        relx = rely = 0
        relwidth = 1
        relheight = 1 - frame_bottom_pad

        self.frame = Frame(parent)
        self.frame.configure(bg=bgcolor)
        self.frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)


# Creating MyLabel
class MyLabel(object):
    def __init__(self, parent, text, relx, rely):
        bgcolor = GrayScale(20)
        fgcolor = GrayScale(220)

        self.label = Label(parent)
        self.label.configure(text=text)
        self.label.configure(font=MyFont)
        self.label.configure(bg=bgcolor, fg=fgcolor)
        self.label.configure(relief=FLAT, anchor=N)
        self.label.configure(padx=2, pady=2)
        self.label.place(relx=relx, rely=rely)


# Creating MyScale
class MyScale(object):
    def __init__(self, parent, text, relx, rely):
        # making parameters into attributes
        self.parent = parent
        self.text = text
        self.relx = relx
        self.rely = rely

        # creating Tkinter variables
        self.l_val = StringVar()

        # setting variables
        bgcolor = GrayScale(20)
        fgcolor = GrayScale(220)

        lowrange = 1.0
        highrange = 100.0
        resolution = 0.1

        def update(scale_value):
            self.l_val.set(' ' + self.text + ' = ' + scale_value + ' ')

        # creating Scale
        self.scale = Scale(self.parent)
        self.scale.configure(command=update)
        self.scale.configure(from_=lowrange, to=highrange)
        self.scale.configure(orient=HORIZONTAL, showvalue=0, resolution=resolution)
        self.scale.configure(bg=bgcolor, fg=fgcolor)
        self.scale.configure(relief=RIDGE, highlightthickness=0, bd=0)
        self.scale.place(relx=relx, rely=rely, relwidth=scale_relwidth, relheight=scale_relheight)

        label_rely = rely - 0.050

        self.label = Label(parent)
        self.label.configure(textvariable=self.l_val)
        self.label.configure(font=MyFont)
        self.label.configure(bg=bgcolor, fg=fgcolor)
        self.label.configure(relief=FLAT)
        self.label.configure(padx=2, pady=2)
        self.label.place(relx=relx, rely=label_rely)
