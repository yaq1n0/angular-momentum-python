# main file

# imports
from Tkinter import Tk
from tkMessageBox import askquestion
from os import execv
from sys import executable, argv

from data.myclasses import MyMainFrame, MyGameFrame, MyImageFrame, MyPreferencesFrame, MyFrame, MyButton, MyImageButton, \
    MyLabel
from data.myfunctions import GrayScale, setGotoStartFalse, setGotoDocFalse, setExitPrefFalse, CreateTkImage
from data.myvariables import dev, MyFonts, ask_again_list, \
    start_geometry, main_geometry, game_geometry, cheatsheet_geometry, documentation_geometry, \
    start_width, start_height, main_width, main_height, game_height, game_width, \
    cheatsheet_width, cheatsheet_height, documentation_width, documentation_height
from data.myvariables import ask_goto_start_again_bool as agsab
from data.myvariables import ask_goto_documentation_again_bool as agdab
from data.myvariables import ask_exit_preferences_again_bool as aepab

# assigning imported variables to global variables
ask_goto_start_again_bool = agsab
ask_goto_documentation_again_bool = agdab
ask_exit_preferences_again_bool = aepab

# first time variables
ft_main = True
ft_game = True
ft_cheatsheet = True
ft_documentation = True
ft_preferences = True

# location identifier variables
at_start = True
Fresh = True
in_game = False
in_documentation = False
in_preferences = False

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


# restart and quit functions
def program_restart():
    if dev:
        print '[program] restart'
    # code from 'https://blog.petrzemek.net/2014/03/23/restarting-a-python-script-within-itself/'
    execv(executable, ['python'] + argv)


def program_quit():
    if dev:
        print '[program] quit'
    exit()


# goto functions
def goto_start():
    global start_bf, at_start, in_game, in_documentation, in_preferences
    if dev:
        print '[nav] goto_start'

    root.geometry(start_geometry + '+' + str(root.winfo_screenwidth() / 2 - start_width / 2)
                  + '+' + str(root.winfo_screenheight() / 2 - start_height / 2))
    root.title('Rotational Motion')

    start_bf.tkraise()

    at_start = True
    in_game = False
    in_documentation = False
    in_preferences = False


def goto_main():
    global ft_main, main_bf, at_start, Fresh
    if dev:
        print '[nav] goto_main'

    root.title('Interactive Experience')

    if ft_main:
        main_bf = MyMainFrame(root)
        ft_main = False
    else:
        if main_bf.in_animation_settings:
            root.geometry(start_geometry + '+' + str(root.winfo_screenwidth() / 2 - start_width / 2)
                          + '+' + str(root.winfo_screenheight() / 2 - start_height / 2))
            main_bf.main_bf.tkraise()
        if not main_bf.in_animation_settings:
            root.geometry(main_geometry + '+' + str(root.winfo_screenwidth() / 2 - main_width / 2)
                          + '+' + str(root.winfo_screenheight() / 2 - main_height / 2))
            main_bf.main_bf.tkraise()

    at_start = False
    Fresh = False


def goto_game():
    global ft_game, game_bf, at_start, Fresh, in_game
    if dev:
        print '[nav] goto_game'

    root.geometry(game_geometry + '+' + str(root.winfo_screenwidth() / 2 - game_width / 2)
                  + '+' + str(root.winfo_screenheight() / 2 - game_height / 2))
    root.title('Test Your Understanding')

    if ft_game:
        game_bf = MyGameFrame(root)
        ft_game = False
        game_bf.create_questions()
        game_bf.shuffle_questions()
        game_bf.game_bf.tkraise()

    else:
        game_bf.destroy_questions()
        game_bf.create_questions()
        game_bf.shuffle_questions()
        game_bf.game_bf.tkraise()

    at_start = False
    Fresh = False
    in_game = True


def goto_cheatsheet():
    global ft_cheatsheet, cheatsheet_bf, at_start, Fresh
    if dev:
        print '[nav] goto_cheatsheet'

    root.geometry(cheatsheet_geometry + '+' + str(root.winfo_screenwidth() / 2 - cheatsheet_width / 2)
                  + '+' + str(root.winfo_screenheight() / 2 - cheatsheet_height / 2))
    root.title('Improve Your Understanding')

    if ft_cheatsheet:
        cheatsheet_bf = MyImageFrame(root, 'data/images/cheatsheet.png', cheatsheet_width, cheatsheet_height)
        ft_cheatsheet = False
    else:
        cheatsheet_bf.img_frame.tkraise()

    at_start = False
    Fresh = False


def goto_documentation():
    global ft_documentation, documentation_bf, at_start, Fresh, in_documentation
    if dev:
        print '[nav] goto_documentation'
    root.geometry(
        documentation_geometry + '+' + str(root.winfo_screenwidth() / 2 - documentation_width / 2)
        + '+' + str(root.winfo_screenheight() / 2 - documentation_height / 2))
    root.title('Program Documentation')

    if ft_documentation:
        documentation_bf = MyImageFrame(root, 'data/images/documentation.png', documentation_width,
                                        documentation_height)
        ft_documentation = False
    else:
        documentation_bf.img_frame.tkraise()

    at_start = False
    Fresh = False
    in_documentation = True


def goto_preferences():
    global ft_preferences, preferences_bf, at_start, Fresh, in_preferences
    if dev:
        print '[nav] goto_preferences'
    root.geometry(start_geometry + '+' + str(root.winfo_screenwidth() / 2 - start_width / 2)
                  + '+' + str(root.winfo_screenheight() / 2 - start_height / 2))
    root.title('Modify Program settings')

    if ft_preferences:
        preferences_bf = MyPreferencesFrame(root)
        ft_preferences = False

    else:
        preferences_bf.main_bf.tkraise()

    at_start = False
    Fresh = False
    in_preferences = True


# creating program-wide binds
def program_restart_bind(event):
    if not Fresh:
        program_restart()


def program_quit_bind(event):
    program_quit()


def goto_start_bind(event):
    global ask_goto_start_again_bool, ask_exit_preferences_again_bool
    if in_game and ask_goto_start_again_bool:
        ask_goto_start = askquestion('Go Back?', 'You have pressed Escape to go to start.'
                                                 '\nYou will lose all progress in the quiz.'
                                                 '\nAre you sure you go to start?')
        if ask_goto_start == 'yes':
            ask_goto_start_again = askquestion(ask_again_list[0], ask_again_list[1])

            if ask_goto_start_again == 'yes':
                ask_goto_start_again_bool = False
                setGotoStartFalse()

            goto_start()

        if ask_goto_start == 'no':
            return

    if in_preferences and ask_exit_preferences_again_bool:
        ask_exit_preferences = askquestion('Exit Preferences', 'You may have unsaved changes.'
                                                               '\nIt is recommended to restart the program before exiting.'
                                                               '\nDo you want to restart?')
        if ask_exit_preferences == 'yes':
            program_restart()

        if ask_exit_preferences == 'no':
            ask_exit_preferences_again = askquestion(ask_again_list[0], ask_again_list[1])

            if ask_exit_preferences_again == 'yes':
                ask_exit_preferences_again_bool = False
                setExitPrefFalse()

            goto_start()

    if at_start:
        if dev:
            print '[start] already in start'
        return

    goto_start()


def goto_documentation_bind(event):
    global ask_goto_documentation_again_bool
    if in_game and ask_goto_documentation_again_bool:
        ask_goto_documentation = askquestion('Open Documentation?', 'You have pressed Control + H to open documentation.'
                                                                    '\nYou will lose all progress in the quiz.'
                                                                    '\nAre you sure you want to open documentation?')
        if ask_goto_documentation == 'yes':
            ask_goto_documentation_again = askquestion(ask_again_list[0], ask_again_list[1])

            if ask_goto_documentation_again == 'yes':
                ask_goto_documentation_again_bool = False
                setGotoDocFalse()

            goto_start()
            goto_documentation()

        if ask_goto_documentation == 'no':
            return

    if in_documentation:
        if dev:
            print '[documentation] already in documentation'
        return

    goto_start()
    goto_documentation()


# binding control + q to quit program
root.bind('<Control-q>', program_quit_bind)

# binding control + r to restart the program
root.bind('<Control-r>', program_restart_bind)

# binding escape to return to start
root.bind('<Escape>', goto_start_bind)

# binding control + h to show program documentation
root.bind('<Control-h>', goto_documentation_bind)

# start_bf objects
if dev:
    print '[start] creating objects'
title_label = MyLabel(start_bf, 'Welcome!', 0.25, 0.05)
title_label.configure(bg=GrayScale(20), font=MyFonts['ExtraLargeBold'])
title_label.place(relwidth=0.5)

button1 = MyButton(start_bf, 'Interactive Experience', goto_main, 0.175, 0.15)
button1.place(relwidth=0.65)

button2 = MyButton(start_bf, 'Test Your Understanding', goto_game, 0.175, 0.30)
button2.place(relwidth=0.65)

button3 = MyButton(start_bf, 'Improve Your Understanding', goto_cheatsheet, 0.175, 0.45)
button3.place(relwidth=0.65)

button4 = MyButton(start_bf, 'Program Documentation', goto_documentation, 0.175, 0.60)
button4.place(relwidth=0.65)

button5 = MyImageButton(start_bf, GrayScale(20), CreateTkImage('data/images/preferences.png', 32, 32), goto_preferences,
                        0.175, 0.75)
button5.place(relwidth=0.12, relheight=0.06)

footnote_label = MyLabel(start_bf,
                         'created by:\n Team 14\nYaqin Hasan\nLian Chao Hooi\nIbraheem El-Nahta\nJaden Pang',
                         0.25, 0.85
                         )
footnote_label.configure(bg=GrayScale(20), fg=GrayScale(60), font=MyFonts['Small'])
footnote_label.place(relwidth=0.5, relheight=0.15)

goto_start()

# mainloop
root.mainloop()
