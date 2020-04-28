# main file

# imports
from Tkinter import Tk
from os import execv
from sys import executable, argv
from data.myvariables import dev, MyFonts, \
    start_geometry, main_geometry, game_geometry, cheatsheet_geometry, documentation_geometry, \
    start_width, start_height, main_width, main_height, game_height, game_width, \
    cheatsheet_width, cheatsheet_height, documentation_width, documentation_height
from data.myfunctions import GrayScale
from data.myclasses import MyMainFrame, MyGameFrame, MyImageFrame, MyFrame, MyButton, MyLabel

# variables:
ft_main = True
ft_game = True
ft_cheatsheet = True
ft_documentation = True
at_start = True
Fresh = True

# creating root
root = Tk()
root.title('Rotational Motion')
root.iconbitmap('data/images/favicon.ico')
root.geometry(start_geometry + '+' + str(root.winfo_screenwidth() / 2 - start_width / 2)
              + '+' + str(root.winfo_screenheight() / 2 - start_height / 2))
root.resizable(False, False)
root.configure(bg=GrayScale(20))

# creating start frame
start_bf = MyFrame(root, GrayScale(20))


# goto functions
def goto_start():
    global start_bf, at_start
    if dev:
        print '[nav] goto_start'

    root.geometry(start_geometry + '+' + str(root.winfo_screenwidth() / 2 - start_width / 2)
                  + '+' + str(root.winfo_screenheight() / 2 - start_height / 2))
    root.title('Rotational Motion')

    start_bf.frame.tkraise()

    at_start = True


def goto_main():
    global ft_main, main_bf, at_start, Fresh
    if dev:
        print '[nav] goto_main'

    root.title('Rotational Motion')

    if ft_main:
        main_bf = MyMainFrame(root)
        ft_main = False
    else:
        if main_bf.in_animation_settings:
            root.geometry(start_geometry + '+' + str(root.winfo_screenwidth() / 2 - start_width / 2)
                          + '+' + str(root.winfo_screenheight() / 2 - start_height / 2))
            main_bf.main_bf.frame.tkraise()
        if not main_bf.in_animation_settings:
            root.geometry(main_geometry + '+' + str(root.winfo_screenwidth() / 2 - main_width / 2)
                          + '+' + str(root.winfo_screenheight() / 2 - main_height / 2))
            main_bf.main_bf.frame.tkraise()

    at_start = False
    Fresh = False


def goto_game():
    global ft_game, game_bf, at_start, Fresh
    if dev:
        print '[nav] goto_game'

    root.geometry(game_geometry + '+' + str(root.winfo_screenwidth() / 2 - game_width / 2)
                  + '+' + str(root.winfo_screenheight() / 2 - game_height / 2))
    root.title('Quiz Game')

    if ft_game:
        game_bf = MyGameFrame(root)
        ft_game = False
        game_bf.create_questions()
        game_bf.shuffle_questions()
        game_bf.game_bf.frame.tkraise()

    else:
        game_bf.destroy_questions()
        game_bf.create_questions()
        game_bf.shuffle_questions()
        game_bf.game_bf.frame.tkraise()

    at_start = False
    Fresh = False


def goto_cheatsheet():
    global ft_cheatsheet, cheatsheet_bf, at_start, Fresh
    if dev:
        print '[nav] goto_cheatsheet'

    root.geometry(cheatsheet_geometry + '+' + str(root.winfo_screenwidth() / 2 - cheatsheet_width / 2)
                  + '+' + str(root.winfo_screenheight() / 2 - cheatsheet_height / 2))
    root.title('CheatSheet')

    if ft_cheatsheet:
        cheatsheet_bf = MyImageFrame(root, 'data/images/cheatsheet.jpg', cheatsheet_width, cheatsheet_height)
        ft_cheatsheet = False
    else:
        cheatsheet_bf.img_frame.frame.tkraise()

    at_start = False
    Fresh = False


def goto_documentation():
    global ft_documentation, documentation_bf, at_start, Fresh
    if dev:
        print '[nav] goto_documentation'
    root.geometry(
        documentation_geometry + '+' + str(root.winfo_screenwidth() / 2 - documentation_width / 2)
        + '+' + str(root.winfo_screenheight() / 2 - documentation_height / 2))
    root.title('Documentation')

    if ft_documentation:
        documentation_bf = MyImageFrame(root, 'data/images/documentation.jpg', documentation_width,
                                        documentation_height)
        ft_documentation = False
    else:
        documentation_bf.img_frame.frame.tkraise()

    at_start = False
    Fresh = False


# resart and quit functions
def program_restart():
    if dev:
        print '[program] restart'
    # code from 'https://blog.petrzemek.net/2014/03/23/restarting-a-python-script-within-itself/'
    execv(executable, ['python'] + argv)


def program_quit():
    if dev:
        print '[program] quit'
    exit()


# creating program-wide binds
def program_restart_bind(event):
    if not Fresh:
        program_restart()


def program_quit_bind(event):
    program_quit()


def goto_start_bind(event):
    if not at_start:
        goto_start()


# binding control + q to quit program
root.bind('<Control-q>', program_quit_bind)

# binding control + r to restart the program
root.bind('<Control-r>', program_restart_bind)

# binding escape to return to start
root.bind('<Escape>', goto_start_bind)

# start_bf objects
if dev:
    print '[start] creating objects'
title_label = MyLabel(start_bf.frame, 'Welcome!', 0.25, 0.05)
title_label.label.configure(bg=GrayScale(20), font=MyFonts['ExtraLargeBold'])
title_label.label.place(relwidth=0.5)

button1 = MyButton(start_bf.frame, 'Interactive Experiece', goto_main, 0.175, 0.15)
button1.button.place(relwidth=0.65)

button2 = MyButton(start_bf.frame, 'Test Your Understanding', goto_game, 0.175, 0.30)
button2.button.place(relwidth=0.65)

button3 = MyButton(start_bf.frame, 'Improve Your Understanding', goto_cheatsheet, 0.175, 0.45)
button3.button.place(relwidth=0.65)

button4 = MyButton(start_bf.frame, 'Program Documentation', goto_documentation, 0.175, 0.60)
button4.button.place(relwidth=0.65)

footnote_label = MyLabel(start_bf.frame,
                         'created by:\n Team 14\nYaqin Hasan\nLian Chao Hooi\nIbraheem El-Nahta\nJaden Pang',
                         0.25, 0.75
                         )
footnote_label.label.configure(bg=GrayScale(20), fg=GrayScale(60), font=MyFonts['Default'])
footnote_label.label.place(relwidth=0.5, relheight=0.25)

goto_start()

root.mainloop()
