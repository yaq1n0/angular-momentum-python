# main file

# imports
from Tkinter import Tk

from tkMessageBox import showerror

from os import execv

from sys import executable, argv

from data.myclasses import MyMainFrame, MyGameFrame, MyImageFrame, MyFrame, MyButton, MyLabel

from data.variables import dev, c_error, c_error_text, colors, start_geometry, main_geometry, game_geometry, \
    cheatsheet_geometry, \
    documentation_geometry, start_width, start_height, main_width, main_height, game_height, game_width, \
    cheatsheet_width, cheatsheet_height, documentation_width, documentation_height

# Program start debug
if c_error:
    root = Tk()
    root.withdraw()
    showerror('Config', c_error_text)
    exit()

if dev:
    print '[run] PROGRAM STARTED'

# creating root
root = Tk()
root.title('Rotational Motion')
root.geometry(start_geometry + '+' + str(root.winfo_screenwidth() / 2 - start_width / 2) + '+' + str(
    root.winfo_screenheight() / 2 - start_height / 2))
root.resizable(False, False)
root.configure(bg=colors[4])

# create start frame
start_bf = MyFrame(root, colors[4])
main_bf = MyMainFrame(root)
game_bf = MyGameFrame(root)


# goto functions
def goto_start():
    root.geometry(start_geometry + '+' + str(root.winfo_screenwidth() / 2 - start_width / 2) + '+' + str(
        root.winfo_screenheight() / 2 - start_height / 2))
    root.title('Rotational Motion')

    start_bf.frame.tkraise()


def goto_main():
    root.geometry(main_geometry + '+' + str(root.winfo_screenwidth() / 2 - main_width / 2) + '+' + str(
        root.winfo_screenheight() / 2 - main_height / 2))
    root.title('Rotational Motion')

    main_bf.main_bf.frame.tkraise()


def goto_game():
    root.geometry(game_geometry + '+' + str(root.winfo_screenwidth() / 2 - game_width / 2) + '+' + str(
        root.winfo_screenheight() / 2 - game_height / 2))
    root.title('Quiz Game')

    game_bf.create_questions()
    game_bf.shuffle_questions()
    game_bf.game_bf.frame.tkraise()


def goto_cheatsheet():
    root.geometry(cheatsheet_geometry + '+' + str(root.winfo_screenwidth() / 2 - cheatsheet_width / 2) + '+' + str(
        root.winfo_screenheight() / 2 - cheatsheet_height / 2))
    root.title('CheatSheet')

    cheatsheet_bf = MyImageFrame(root, 'data/images/cheatsheet.jpg', cheatsheet_width, cheatsheet_height)
    cheatsheet_bf.img_frame.tkraise()


def goto_documentation():
    root.geometry(
        documentation_geometry + '+' + str(root.winfo_screenwidth() / 2 - documentation_width / 2) + '+' + str(
            root.winfo_screenheight() / 2 - documentation_height / 2))
    root.title('Documentation')

    documentation_bf = MyImageFrame(root, 'data/images/documentation.jpg', documentation_width, documentation_height)
    documentation_bf.img_frame.tkraise()


# resart and quit functions
def program_restart():
    # code from 'https://blog.petrzemek.net/2014/03/23/restarting-a-python-script-within-itself/'
    execv(executable, ['python'] + argv)


def program_quit():
    exit()


# creating program-wide binds
def program_restart_bind(event):
    program_restart()


def program_quit_bind(event):
    program_quit()


def goto_start_bind(event):
    goto_start()


# binding control + q to quit program
root.bind('<Control-q>', program_quit_bind)

# binding control + r to restart the program
root.bind('<Control-r>', program_restart_bind)

# binding escape to return to start
root.bind('<Escape>', goto_start_bind)

# start_bf objects
title_label = MyLabel(start_bf.frame, 'Welcome!', 0.25, 0.05)
title_label.label.configure(bg=colors[4])
title_label.label.place(relwidth=0.5)

button1 = MyButton(start_bf.frame, 'Main', goto_main, 0.25, 0.15)
button1.button.place(relwidth=0.5)

button2 = MyButton(start_bf.frame, 'Quiz Game', goto_game, 0.25, 0.30)
button2.button.place(relwidth=0.5)

button3 = MyButton(start_bf.frame, 'CheatSheet', goto_cheatsheet, 0.25, 0.45)
button3.button.place(relwidth=0.5)

button4 = MyButton(start_bf.frame, 'Documentation', goto_documentation, 0.25, 0.60)
button4.button.place(relwidth=0.5)

footnote_label = MyLabel(start_bf.frame,
                         'created by: \n Yaqin Hasan \n Lian Chao Hooi \n Ibraheem El-Nahta \n Jaden Pang',
                         0.25, 0.70
                         )
footnote_label.label.configure(bg=colors[4], fg=colors[3])
footnote_label.label.place(relwidth=0.5, relheight=0.25)

goto_start()

root.mainloop()
