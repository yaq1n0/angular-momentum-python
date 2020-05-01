# other classes

# imports
from Tkinter import \
    Toplevel, Frame, Canvas, Label, Button, Scale, Entry, \
    LEFT, HORIZONTAL, FLAT, RIDGE, SOLID, StringVar, N
from data.myfunctions import GrayScale
from data.myvariables import \
    MyFonts, canvas_relx, canvas_rely, canvas_width, canvas_height, \
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
        label.configure(bg=GrayScale(60), fg=GrayScale(220), font=MyFonts['Default'])
        label.pack(ipadx=1)

    # hidetip method for ToolTip class
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


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


# Creating MyInputFrame
class MyInputFrame(object):
    def __init__(self, parent, bgcolor):
        relx = 0
        rely = 0
        relwidth = 0.30
        relheight = 0.80

        self.frame = Frame(parent)
        self.frame.configure(bg=bgcolor)
        self.frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)


# Creating MyOutputFrame
class MyOutputFrame(object):
    def __init__(self, parent, bgcolor):
        relx = 0.70
        rely = 0
        relwidth = 0.30
        relheight = 0.80 / 0.90

        self.frame = Frame(parent)
        self.frame.configure(bg=bgcolor)
        self.frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)


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
        self.canvas.configure(relief=RIDGE, bd=2)
        self.canvas.place(relx=relx, rely=rely)


# Creating MyButton
class MyButton(object):
    def __init__(self, parent, text, command, relx, rely):
        bgcolor = GrayScale(40)
        fgcolor = GrayScale(220)

        relwidth = 0.10
        relheight = 0.05

        self.button = Button(parent)
        self.button.configure(text=text, command=command)
        self.button.configure(font=MyFonts['DefaultBold'])
        self.button.configure(bg=bgcolor, fg=fgcolor)
        self.button.configure(activebackground=bgcolor, activeforeground=fgcolor)
        self.button.configure(relief=RIDGE, highlightthickness=0, bd=0)
        self.button.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)


# Creating MyImageButton
class MyImageButton(object):
    def __init__(self, parent, bgcolor, img, command, relx, rely):
        relwidth = 0.05 / (16.0 / 9.0)
        relheight = 0.05

        self.button = Button(parent)
        self.button.configure(image=img)
        self.button.image = img
        self.button.configure(command=command)
        self.button.configure(bg=bgcolor, activebackground=bgcolor)
        self.button.configure(relief=RIDGE, highlightthickness=0, bd=0)
        self.button.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)


# Creating MyToggleButton
class MyToggleButton(object):
    def __init__(self, parent, text, relx, rely):
        # assigning parameters to attributes
        self.parent = parent
        self.text = text
        self.relx = relx
        self.rely = rely

        self.relwidth = 0.20
        self.relheight = 0.20 / 2

        self.enabled = False

        self.create_title_label()
        self.create_frames()

    def create_title_label(self):
        self.title_label = MyLabel(self.parent, self.text, self.relx, self.rely - 0.05)
        self.title_label.label.configure(font=MyFonts['LargeBold'])

    def create_frames(self):
        self.pf = Frame(self.parent)
        self.pf.configure(bg=GrayScale(0))
        self.pf.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)

        self.f1 = MyFrame(self.pf, GrayScale(80))
        self.f2 = MyFrame(self.pf, GrayScale(60))

        self.b1 = MyButton(self.f1.frame, 'Disabled', self.func1, 0, 0)
        self.b2 = MyButton(self.f2.frame, 'Enabled', self.func2, 0, 0)

        self.b1.button.configure(bg=GrayScale(40), activebackground=GrayScale(180))
        self.b2.button.configure(bg=GrayScale(180), activebackground=GrayScale(40), fg=GrayScale(20))

        self.b1.button.place(relwidth=1, relheight=1)
        self.b2.button.place(relwidth=1, relheight=1)

    def func1(self):
        self.f2.frame.tkraise()
        self.enabled = True

    def func2(self):
        self.f1.frame.tkraise()
        self.enabled = False


# Creating MyCycleButton3
class MyCycleButton3(object):
    def __init__(self, parent, options_list, frames_list, relx, rely):
        # assigning parameters to attributes
        self.parent = parent
        self.o_list = options_list
        self.f_list = frames_list
        self.relx = relx
        self.rely = rely

        self.relwidth = 0.10
        self.relheight = 0.05

        # creating frames
        self.create_frames()

    def create_frames(self):
        self.pf = Frame(self.parent)
        self.pf.configure(bg=GrayScale(0))
        self.pf.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)

        self.f1 = MyFrame(self.pf, GrayScale(80))
        self.f2 = MyFrame(self.pf, GrayScale(60))
        self.f3 = MyFrame(self.pf, GrayScale(40))

        self.b1 = MyButton(self.f1.frame, self.o_list[0], self.func1, 0, 0)
        self.b2 = MyButton(self.f2.frame, self.o_list[1], self.func2, 0, 0)
        self.b3 = MyButton(self.f3.frame, self.o_list[2], self.func3, 0, 0)

        self.b1.button.configure(bg=GrayScale(80), activebackground=GrayScale(80))
        self.b2.button.configure(bg=GrayScale(60), activebackground=GrayScale(60))
        self.b3.button.configure(bg=GrayScale(40), activebackground=GrayScale(40))

        self.b1.button.place(relwidth=1, relheight=1)
        self.b2.button.place(relwidth=1, relheight=1)
        self.b3.button.place(relwidth=1, relheight=1)

        self.f1.frame.tkraise()

    def func1(self):
        self.f2.frame.tkraise()
        self.f_list[2].tkraise()
        self.f_list[0].tkraise()

    def func2(self):
        self.f3.frame.tkraise()
        self.f_list[3].tkraise()
        self.f_list[0].tkraise()

    def func3(self):
        self.f1.frame.tkraise()
        self.f_list[1].tkraise()
        self.f_list[0].tkraise()


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
        self.label.configure(font=MyFonts['Default'])
        self.label.configure(bg=bgcolor, fg=fgcolor)
        self.label.configure(relief=FLAT)
        self.label.configure(padx=2, pady=2)
        self.label.place(relx=relx, rely=label_rely)


# Creating MyInputScale
class MyInputScale(object):
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
        self.scale.place(relx=relx, rely=rely, relwidth=scale_relwidth * 1.35 / 0.3,
                         relheight=scale_relheight * 1.35 / 0.8)

        label_rely = rely - 0.050

        self.label = Label(parent)
        self.label.configure(textvariable=self.l_val)
        self.label.configure(font=MyFonts['Default'])
        self.label.configure(bg=bgcolor, fg=fgcolor)
        self.label.configure(relief=FLAT)
        self.label.configure(padx=2, pady=2)
        self.label.place(relx=relx, rely=label_rely)


# Creating MyLabel
class MyLabel(object):
    def __init__(self, parent, text, relx, rely):
        bgcolor = GrayScale(20)
        fgcolor = GrayScale(220)

        self.label = Label(parent)
        self.label.configure(text=text)
        self.label.configure(font=MyFonts['Default'])
        self.label.configure(bg=bgcolor, fg=fgcolor)
        self.label.configure(relief=FLAT, anchor=N)
        self.label.configure(padx=2, pady=2)
        self.label.place(relx=relx, rely=rely)


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
        self.label.configure(font=MyFonts['Default'])
        self.label.configure(bg=bgcolor, fg=fgcolor)
        self.label.configure(relief=FLAT)
        self.label.configure(padx=2, pady=2)
        self.label.place(relx=relx, rely=label_rely)


# Creating MyOutputEntry
class MyOutputEntry(object):
    def __init__(self, parent, text, relx, rely):
        charwidth = 20

        bgcolor = GrayScale(20)
        fgcolor = GrayScale(220)

        self.entry = Entry(parent)
        self.entry.configure(width=charwidth)
        self.entry.configure(bg=bgcolor, fg=fgcolor)
        self.entry.configure(relief=RIDGE, highlightthickness=2, bd=0)
        self.entry.place(relx=relx, rely=rely)

        label_rely = rely - 0.050

        self.label = Label(parent)
        self.label.configure(text=text)
        self.label.configure(font=MyFonts['Default'])
        self.label.configure(bg=bgcolor, fg=fgcolor)
        self.label.configure(relief=FLAT)
        self.label.configure(padx=2, pady=2)
        self.label.place(relx=relx, rely=label_rely)
