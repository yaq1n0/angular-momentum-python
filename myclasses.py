from Tkinter import *

import myvars
import myfunctions


# Defining Object ToolTip
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
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw,
                      bd=1,
                      relief=FLAT,
                      text=self.text,
                      justify=LEFT,
                      bg=myvars.colors[2],
                      fg=myvars.colors[0],
                      )
        label.pack(ipadx=1)

    # hidetip method for ToolTip class
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


# Creating General Objects

# Creating MyGenButton
class MyGenButton(object):
    def __init__(self, parent, text, command, bgcolor, fgcolor, abgcolor, afgcolor, relx, rely, relwidth, relheight):
        self.button = Button(parent)
        self.button.configure(text=text, command=command)
        self.button.configure(bg=bgcolor, fg=fgcolor)
        self.button.configure(activebackground=abgcolor, activeforeground=afgcolor)
        self.button.configure(relief=RIDGE, highlightthickness=0, bd=0)
        self.button.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)


# Creating MyGenCanvas
class MyGenCanvas(object):
    def __init__(self, parent, bgcolor, relx, rely, abswidth, absheight):
        self.canvas = Canvas(parent)
        self.canvas.configure(bg=bgcolor)
        self.canvas.configure(width=abswidth, height=absheight)
        self.canvas.configure(relief=RIDGE, highlightthickness=0, bd=0)
        self.canvas.place(relx=relx, rely=rely)


# Creating MyGenEntry
class MyGenEntry(object):
    def __init__(self, parent, bgcolor, fgcolor, relx, rely, charwidth):
        self.entry = Entry(parent)
        self.entry.configure(width=charwidth)
        self.entry.configure(bg=bgcolor, fg=fgcolor)
        self.entry.configure(relief=RIDGE, highlightthickness=0, bd=0)
        self.entry.place(relx=relx, rely=rely)


# Creating MyGenFrame
class MyGenFrame(object):
    def __init__(self, parent, bgcolor, relx, rely, relwidth, relheight):
        self.frame = Frame(parent)
        self.frame.configure(bg=bgcolor)
        self.frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)


# Creating MyGenLabel
class MyGenLabel(object):
    def __init__(self, parent, text, bgcolor, fgcolor, relx, rely, relwidth, relheight):
        self.label = Label(parent)
        self.label.configure(text=text)
        self.label.configure(bg=bgcolor, fg=fgcolor)
        self.label.configure(relief=FLAT)
        self.label.configure(padx=2, pady=2)
        self.label.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)


# Creating MyGenScale
class MyGenScale(object):
    def __init__(self, parent, lowrange, highrange, resolution, bgcolor, fgcolor, relx, rely, relwidth, relheight):
        self.scale = Scale(parent)
        self.scale.configure(from_=lowrange, to=highrange)
        self.scale.configure(orient=HORIZONTAL, showvalue=1, resolution=resolution)
        self.scale.configure(bg=bgcolor, fg=fgcolor)
        self.scale.configure(relief=RIDGE, highlightthickness=0, bd=0)
        self.scale.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)


# Creating MyObjects

# Creating MyButton
class MyButton(object):
    def __init__(self, parent, text, command, relx, rely):
        bgcolor = myvars.colors[2]
        fgcolor = myvars.colors[0]

        abgcolor = myvars.colors[1]
        afgcolor = myvars.colors[4]

        relwidth = 0.10
        relheight = 0.05

        self.button = Button(parent)
        self.button.configure(text=text, command=command)
        self.button.configure(bg=bgcolor, fg=fgcolor)
        self.button.configure(activebackground=abgcolor, activeforeground=afgcolor)
        self.button.configure(relief=RIDGE, highlightthickness=0, bd=0)
        self.button.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)


# Creating MyCanvas
class MyCanvas(object):
    def __init__(self, parent):
        bgcolor = myvars.fbg

        abswidth = myvars.canvas_width
        absheight = myvars.canvas_height

        relx = myvars.canvas_relx
        rely = myvars.canvas_rely

        self.canvas = Canvas(parent)
        self.canvas.configure(bg=bgcolor)
        self.canvas.configure(width=abswidth, height=absheight)
        self.canvas.configure(relief=RIDGE, highlightthickness=0, bd=0)
        self.canvas.place(relx=relx, rely=rely)


# Creating MyEntry
class MyEntry(object):
    def __init__(self, parent, text, relx, rely):
        charwidth = 20

        bgcolor = myvars.fbg
        fgcolor = myvars.ffg

        self.entry = Entry(parent)
        self.entry.configure(width=charwidth)
        self.entry.configure(bg=bgcolor, fg=fgcolor)
        self.entry.configure(relief=RIDGE, highlightthickness=2, bd=0)
        self.entry.place(relx=relx, rely=rely)

        label_rely = rely - 0.045

        self.label = Label(parent)
        self.label.configure(text=text)
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
        bgcolor = myvars.fbg
        fgcolor = myvars.ffg

        self.label = Label(parent)
        self.label.configure(text=text)
        self.label.configure(bg=bgcolor, fg=fgcolor)
        self.label.configure(relief=FLAT)
        self.label.configure(padx=2, pady=2)
        self.label.place(relx=relx, rely=rely)


# Creating MyScale
class MyScale(object):
    def __init__(self, parent, text, relx, rely):
        bgcolor = myvars.fbg
        fgcolor = myvars.ffg

        lowrange = 1.0
        highrange = 100.0
        resolution = 0.1

        scale_relwidth = myvars.scale_relwidth
        scale_relheight = myvars.scale_relheight

        self.scale = Scale(parent)
        self.scale.configure(from_=lowrange, to=highrange)
        self.scale.configure(orient=HORIZONTAL, showvalue=1, resolution=resolution)
        self.scale.configure(bg=bgcolor, fg=fgcolor)
        self.scale.configure(relief=RIDGE, highlightthickness=0, bd=0)
        self.scale.place(relx=relx, rely=rely, relwidth=scale_relwidth, relheight=scale_relheight)

        label_rely = rely - 0.045

        self.label = Label(parent)
        self.label.configure(text=text)
        self.label.configure(bg=bgcolor, fg=fgcolor)
        self.label.configure(relief=FLAT)
        self.label.configure(padx=2, pady=2)
        self.label.place(relx=relx, rely=label_rely)
