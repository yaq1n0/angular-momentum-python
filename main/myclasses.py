
# contains all custom classes

# importing python modules
from Tkinter import *
import tkMessageBox

# importing personal modules
import myvars


# Defining Object ToolTip
# code from "https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python"
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

        relwidth = 0.10
        relheight = 0.05

        self.button = Button(parent)
        self.button.configure(text=text, command=command)
        self.button.configure(bg=bgcolor, fg=fgcolor)
        self.button.configure(activebackground=bgcolor, activeforeground=fgcolor)
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
        # making parameters into attributes
        self.parent = parent
        self.text = text
        self.relx = relx
        self.rely = rely

        # creating Tkinter variables
        self.l_val = StringVar()

        # setting variables
        bgcolor = myvars.fbg
        fgcolor = myvars.ffg

        lowrange = 1.0
        highrange = 100.0
        resolution = 0.1

        scale_relwidth = myvars.scale_relwidth
        scale_relheight = myvars.scale_relheight

        def update(scale_value):
            self.l_val.set(self.text + " = " + scale_value)

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
        self.label.configure(bg=bgcolor, fg=fgcolor)
        self.label.configure(relief=FLAT)
        self.label.configure(padx=2, pady=2)
        self.label.place(relx=relx, rely=label_rely)


class MyQuestion(object):
    def __init__(self, parent, question_text, ans1_text, ans2_text, ans3_text, ans4_text, exp1_text, exp2_text,
                 exp3_text, exp4_text, correct_ans):

        # making parameters into attributes
        self.parent = parent

        self.qtext = str(question_text)

        self.text1 = str(ans1_text)
        self.text2 = str(ans2_text)
        self.text3 = str(ans3_text)
        self.text4 = str(ans4_text)

        self.exp1 = str(exp1_text)
        self.exp2 = str(exp2_text)
        self.exp3 = str(exp3_text)
        self.exp4 = str(exp4_text)

        self.ans = int(correct_ans)

        # correct answer explanation
        if self.ans == 1:
            self.ans_text = "A. " + self.text1
            self.ans_exp = self.exp1
        elif self.ans == 2:
            self.ans_text = "B. " + self.text2
            self.ans_exp = self.exp2
        elif self.ans == 3:
            self.ans_text = "C. " + self.text3
            self.ans_exp = self.exp3
        elif self.ans == 4:
            self.ans_text = "D. " + self.text4
            self.ans_exp = self.exp4
        else:
            self.ans_text = "invalid correct_ans parameter"
            self.ans_exp = "invalid correct_ans parameter"
            print "invalid correct_ans parameter, please input between 1 and 4"

        # creating Tkinter variables

        self.ans_input = IntVar()
        self.is_correct = BooleanVar()
        self.efbg = StringVar()
        self.is_correct_text = StringVar()

        # questionwide bgcolor, fgcolor
        self.bgcolor = myvars.colors[2]
        self.fgcolor = myvars.colors[4]

        self.parent_frame()
        self.question_frame()

    def parent_frame(self):
        self.pf = MyFrame(self.parent, self.bgcolor)

    def question_frame(self):
        # creating frame
        self.qf = MyFrame(self.pf.frame, self.bgcolor)

        # creating title label

        self.title_label = Label(self.qf.frame)
        self.title_label.configure(text=self.qtext)
        self.title_label.configure(bg=self.bgcolor, fg=self.fgcolor)
        self.title_label.configure(relief=FLAT)
        self.title_label.configure(padx=2, pady=2)
        self.title_label.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.10)

        # creating radio buttons 1-4
        self.q1 = Radiobutton(self.qf.frame)
        self.q1.configure(text="A. " + self.text1)
        self.q1.configure(bg=self.bgcolor, activebackground=self.bgcolor)
        self.q1.configure(variable=self.ans_input, value=1)
        self.q1.place(relx=0.10, rely=0.20)

        self.q2 = Radiobutton(self.qf.frame)
        self.q2.configure(text="B. " + self.text2)
        self.q2.configure(bg=self.bgcolor, activebackground=self.bgcolor)
        self.q2.configure(variable=self.ans_input, value=2)
        self.q2.place(relx=0.10, rely=0.35)

        self.q3 = Radiobutton(self.qf.frame)
        self.q3.configure(text="C. " + self.text3)
        self.q3.configure(bg=self.bgcolor, activebackground=self.bgcolor)
        self.q3.configure(variable=self.ans_input, value=3)
        self.q3.place(relx=0.10, rely=0.50)

        self.q4 = Radiobutton(self.qf.frame)
        self.q4.configure(text="D. " + self.text4)
        self.q4.configure(bg=self.bgcolor, activebackground=self.bgcolor)
        self.q4.configure(variable=self.ans_input, value=4)
        self.q4.place(relx=0.10, rely=0.65)

        # creating check button
        self.cb = MyButton(self.qf.frame, "Check Answer", self.check_ans, 0.85, 0.85)
        self.cb.button.configure(bg=myvars.colors[4], fg=myvars.colors[0])
        self.cb.button.configure(activebackground=myvars.colors[4], activeforeground=myvars.colors[0])

    def explanation_frame(self, exp_text):
        self.ef = MyFrame(self.pf.frame, self.efbg.get())
        self.ef.frame.tkraise()

        self.correct_label = Label(self.ef.frame)
        self.correct_label.configure(text=self.is_correct_text.get())
        self.correct_label.configure(bg=self.efbg.get(), fg=self.fgcolor)
        self.correct_label.configure(relief=FLAT)
        self.correct_label.configure(padx=2, pady=2, anchor=N)
        self.correct_label.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.05)

        self.exp_label = Label(self.ef.frame)
        self.exp_label.configure(text=exp_text)
        self.exp_label.configure(bg=self.efbg.get(), fg=self.fgcolor)
        self.exp_label.configure(relief=FLAT)
        self.exp_label.configure(padx=2, pady=2, anchor=N)
        self.exp_label.place(relx=0.05, rely=0.10, relwidth=0.90, relheight=0.85)

        # creating next question button
        self.nq = MyButton(self.ef.frame, "Next Question", self.next_ques, 0.85, 0.85)
        self.nq.button.configure(bg=myvars.colors[4], fg=myvars.colors[0])
        self.nq.button.configure(activebackground=myvars.colors[4], activeforeground=myvars.colors[0])

        if not self.is_correct.get():
            self.disp_ans_button()

    def disp_ans_button(self):
        self.eb = MyButton(self.ef.frame, "Show Answer", self.disp_ans, 0.70, 0.85)
        self.eb.button.configure(bg=myvars.colors[4], fg=myvars.colors[0])
        self.eb.button.configure(activebackground=myvars.colors[4], activeforeground=myvars.colors[0])

    def check_ans(self):

        if self.ans_input.get() == self.ans:
            self.efbg.set(myvars.color_green)
            self.is_correct.set(True)
            self.is_correct_text.set("Correct Answer! :)")

        else:
            self.efbg.set(myvars.color_red)
            self.is_correct.set(False)
            self.is_correct_text.set("Wrong Answer :(")

        if self.ans_input.get() == 1:
            self.explanation_frame(self.exp1)

        elif self.ans_input.get() == 2:
            self.explanation_frame(self.exp2)

        elif self.ans_input.get() == 3:
            self.explanation_frame(self.exp3)

        elif self.ans_input.get() == 4:
            self.explanation_frame(self.exp4)

        else:
            tkMessageBox.showerror("Error", "Please select an answer to continue")

    def next_ques(self):
        self.ef.frame.destroy()
        self.qf.frame.destroy()
        self.pf.frame.destroy()

    def disp_ans(self):
        disp_ans_text = 'The correct answer is "' + str(self.ans_text) + '" because ' + str(self.ans_exp)
        tkMessageBox.showinfo("Correct Answer", disp_ans_text)
