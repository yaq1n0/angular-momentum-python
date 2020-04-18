# main file

# imports
from Tkinter import Tk
from os import execv
from sys import executable, argv
from main import run_main
from game import run_game
from images import run_cheatsheet, run_documentation
from myclasses import MyFrame, MyButton, MyLabel
from myvars import colors, first_run1, first_run2, first_run3, first_run4
from myvars import start_geometry, main_geometry, game_geometry, cheatsheet_geometry, documentation_geometry

# space to test code

print ''

# creating root
root = Tk()
root.title('Rotational Motion')
root.geometry(start_geometry)
root.resizable(False, False)
root.configure(bg=colors[4])

# creating base frames
start_bf = MyFrame(root, colors[4])
main_bf = MyFrame(root, colors[4])
game_bf = MyFrame(root, colors[4])
cheatsheet_bf = MyFrame(root, colors[4])
documentation_bf = MyFrame(root, colors[4])

# raising start_bf and setting window size
start_bf.frame.tkraise()


# restart and quit functions
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


# goto functions
def goto_start():
    root.geometry(start_geometry)
    root.title('Rotational Motion')
    start_bf.frame.tkraise()


def goto_main():
    global first_run1
    root.geometry(main_geometry)
    root.title('Rotational Motion')
    if first_run1:
        run_main(root, main_bf.frame)
        first_run1 = False
    main_bf.frame.tkraise()


def goto_game():
    global first_run2
    root.geometry(game_geometry)
    root.title('Quiz Game')
    run_game(game_bf.frame)
    game_bf.frame.tkraise()


def goto_cheatsheet():
    global first_run3
    root.geometry(cheatsheet_geometry)
    root.title('CheatSheet')
    if first_run3:
        run_cheatsheet(cheatsheet_bf.frame)
        first_run3 = False
    cheatsheet_bf.frame.tkraise()


def goto_documentation():
    global first_run4
    root.geometry(documentation_geometry)
    root.title('Documentation')
    if first_run4:
        run_documentation(documentation_bf.frame)
        first_run4 = False
    documentation_bf.frame.tkraise()


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

root.mainloop()
