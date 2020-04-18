# MyQuestion class definition

# imports
from Tkinter import BooleanVar, IntVar, StringVar
from Tkinter import Frame, Label, Button, Radiobutton
from Tkinter import FLAT, RIDGE
from Tkinter import N
from tkMessageBox import showinfo, showerror
from myvars import MyFont, dev
from myvars import colors, color_green, color_red


class MyQuestion(object):
    def __init__(self, parent, question_text, ans1_text, ans2_text, ans3_text, ans4_text,
                 exp1_text, exp2_text, exp3_text, exp4_text, correct_ans):
        # assigning parameters to attributes
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

        # creating Tkinter variables
        self.ans_input = IntVar()
        self.is_correct = BooleanVar()
        self.efbg = StringVar()
        self.is_correct_text = StringVar()
        self.exp_text = StringVar()

        # developer mode
        if dev:
            self.ans_input.set(self.ans)

        # questionwide bgcolor, fgcolor
        self.bgcolor = colors[2]
        self.fgcolor = colors[4]

        # creating parent frame
        self.parent_frame()
        self.question_frame()

    def parent_frame(self):
        # creating parent frame
        self.pf = Frame(self.parent)
        self.pf.configure(bg=self.bgcolor)
        self.pf.place(relx=0, rely=0, relwidth=1, relheight=1)

    def question_frame(self):
        # creating question frame within parent frame
        self.qf = Frame(self.pf)
        self.qf.configure(bg=self.bgcolor)
        self.qf.place(relx=0, rely=0, relwidth=1, relheight=1)

        # creating objects within question frame
        self.title_label()
        self.radiobutton1()
        self.radiobutton2()
        self.radiobutton3()
        self.radiobutton4()
        self.check_ans_button()

    def explanation_frame(self):
        # creating explanation frame within parent frame
        self.ef = Frame(self.pf)
        self.ef.configure(bg=self.efbg.get())
        self.ef.place(relx=0, rely=0, relwidth=1, relheight=1)

        # creating objects within explanation frame
        self.is_correct_label()
        self.exp_label()
        self.next_ques_button()

        # creating display answer button if answer is wrong
        if not self.is_correct.get():
            self.disp_ans_button()

    def title_label(self):
        # creating title label for question frame
        self.tl = Label(self.qf)
        self.tl.configure(text=self.qtext)
        self.tl.configure(font=MyFont)
        self.tl.configure(bg=self.bgcolor, fg=self.fgcolor)
        self.tl.configure(relief=FLAT)
        self.tl.configure(padx=2, pady=2, anchor=N)
        self.tl.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.10)

    def radiobutton1(self):
        # creating radiobuttion1 for question frame
        self.q1 = Radiobutton(self.qf)
        self.q1.configure(text='A. ' + self.text1)
        self.q1.configure(font=MyFont)
        self.q1.configure(bg=self.bgcolor, activebackground=self.bgcolor)
        self.q1.configure(variable=self.ans_input, value=1)
        self.q1.place(relx=0.10, rely=0.20)

    def radiobutton2(self):
        # creating radiobutton2 for question frame
        self.q2 = Radiobutton(self.qf)
        self.q2.configure(text='B. ' + self.text2)
        self.q2.configure(font=MyFont)
        self.q2.configure(bg=self.bgcolor, activebackground=self.bgcolor)
        self.q2.configure(variable=self.ans_input, value=2)
        self.q2.place(relx=0.10, rely=0.35)

    def radiobutton3(self):
        # creating radiobutton3 for question frame
        self.q3 = Radiobutton(self.qf)
        self.q3.configure(text='C. ' + self.text3)
        self.q3.configure(font=MyFont)
        self.q3.configure(bg=self.bgcolor, activebackground=self.bgcolor)
        self.q3.configure(variable=self.ans_input, value=3)
        self.q3.place(relx=0.10, rely=0.50)

    def radiobutton4(self):
        # creating radiobutton4 for question frame
        self.q4 = Radiobutton(self.qf)
        self.q4.configure(text='D. ' + self.text4)
        self.q4.configure(font=MyFont)
        self.q4.configure(bg=self.bgcolor, activebackground=self.bgcolor)
        self.q4.configure(variable=self.ans_input, value=4)
        self.q4.place(relx=0.10, rely=0.65)

    def check_ans_button(self):
        # creating check answer button for question frame
        self.cb = Button(self.qf)
        self.cb.configure(text='Check Answer', command=self.check_ans)
        self.cb.configure(font=MyFont)
        self.cb.configure(bg=self.bgcolor, fg=self.fgcolor)
        self.cb.configure(activebackground=self.bgcolor, activeforeground=self.fgcolor)
        self.cb.configure(relief=RIDGE, highlightthickness=0, bd=0)
        self.cb.place(relx=0.80, rely=0.85, relwidth=0.10, relheight=0.05)

    def is_correct_label(self):
        # creating is_correct_label for explanation frame
        self.cl = Label(self.ef)
        self.cl.configure(text=self.is_correct_text.get())
        self.cl.configure(font=MyFont)
        self.cl.configure(bg=self.efbg.get(), fg=self.fgcolor)
        self.cl.configure(relief=FLAT)
        self.cl.configure(padx=2, pady=2, anchor=N)
        self.cl.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.05)

    def exp_label(self):
        # creating exp_label for explanation frame
        self.el = Label(self.ef)
        self.el.configure(text=self.exp_text.get())
        self.el.configure(font=MyFont)
        self.el.configure(bg=self.efbg.get(), fg=self.fgcolor)
        self.el.configure(relief=FLAT)
        self.el.configure(padx=2, pady=2, anchor=N)
        self.el.place(relx=0.05, rely=0.10, relwidth=0.90, relheight=0.85)

    def next_ques_button(self):
        # creating next question button for explanation frame
        self.nq = Button(self.ef)
        self.nq.configure(text='Next Question', command=self.next_ques)
        self.nq.configure(font=MyFont)
        self.nq.configure(bg=self.bgcolor, fg=self.fgcolor)
        self.nq.configure(activebackground=self.bgcolor, activeforeground=self.fgcolor)
        self.nq.configure(relief=RIDGE, highlightthickness=0, bd=0)
        self.nq.place(relx=0.80, rely=0.85, relwidth=0.10, relheight=0.05)

    def disp_ans_button(self):
        # creating display answer button for explanation frame
        self.da = Button(self.ef)
        self.da.configure(text='Show Answer', command=self.disp_ans)
        self.da.configure(font=MyFont)
        self.da.configure(bg=self.bgcolor, fg=self.fgcolor)
        self.da.configure(activebackground=self.bgcolor, activeforeground=self.fgcolor)
        self.da.configure(relief=RIDGE, highlightthickness=0, bd=0)
        self.da.place(relx=0.65, rely=0.85, relwidth=0.10, relheight=0.05)

    def assign_all(self):
        # assigning correct answer text (ans_text) and explanation attributes (ans_exp)
        if self.ans == 1:
            self.ans_text = 'A. ' + self.text1
            self.ans_exp = self.exp1
        elif self.ans == 2:
            self.ans_text = 'B. ' + self.text2
            self.ans_exp = self.exp2
        elif self.ans == 3:
            self.ans_text = 'C. ' + self.text3
            self.ans_exp = self.exp3
        elif self.ans == 4:
            self.ans_text = 'D. ' + self.text4
            self.ans_exp = self.exp4
        else:
            self.ans_text = 'invalid correct_ans parameter'
            self.ans_exp = 'invalid correct_ans parameter'
            print 'invalid correct_ans parameter, please input between 1 and 4'

    def check_ans(self):
        # defining check answer function

        # is_correct (Boolean conditional)
        if self.ans_input.get() == self.ans:
            self.efbg.set(color_green)
            self.is_correct.set(True)
            self.is_correct_text.set('Correct Answer! :)')

        else:
            self.efbg.set(color_red)
            self.is_correct.set(False)
            self.is_correct_text.set('Wrong Answer :(')

            # only assign values for show answer if user answer is wrong
            self.assign_all()

        # appropriate response to selected answer
        if self.ans_input.get() == 1:
            self.exp_text.set(self.exp1)
            self.explanation_frame()

        elif self.ans_input.get() == 2:
            self.exp_text.set(self.exp2)
            self.explanation_frame()

        elif self.ans_input.get() == 3:
            self.exp_text.set(self.exp3)
            self.explanation_frame()

        elif self.ans_input.get() == 4:
            self.exp_text.set(self.exp4)
            self.explanation_frame()

        else:
            # no selected answer condition
            showerror('Error', 'Please select an answer to continue')

        # create explanation frame
        self.explanation_frame()

        # destroy question frame
        self.qf.destroy()

    def disp_ans(self):
        # defining display answer function
        tmp_str = self.ans_exp[0].lower() + self.ans_exp[1:]
        disp_ans_text = 'The correct answer is "' + str(self.ans_text) + '" because ' + str(tmp_str)
        showinfo('Correct Answer', disp_ans_text)

    def next_ques(self):
        # defininf next_question function
        self.pf.destroy()
        self.ef.destroy()
