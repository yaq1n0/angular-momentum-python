# GUI for modifying program settings

# imports
from Tkinter import Tk, END
from tkMessageBox import showwarning
from os import execv
from sys import executable, argv
from data.myclasses import MyLabel, MyEntry, MyToggleButton, MyImageButton
from data.myfunctions import GrayScale, CreateTkImage
from data.myvariables import start_geometry, start_width, start_height, MyFonts, dev
from data.userconfig import width as config_width
from data.userconfig import height as config_height
from data.userconfig import font as config_font
from data.userconfig import font_size as config_font_size
from data.userconfig import enable_tooltips as config_tooltips

# creating Tk window

root = Tk()
root.title('Modify Program settings')
root.iconbitmap('data/images/favicon.ico')
root.geometry(start_geometry + '+' + str(root.winfo_screenwidth() / 2 - start_width / 2)
              + '+' + str(root.winfo_screenheight() / 2 - start_height / 2))
root.resizable(False, False)
root.configure(bg=GrayScale(20))


# defining functions
def openConfig():
    # open userconfig.py for full overwrite
    myfile = open('data/userconfig.py', 'w')
    return myfile


def writeConfig(file, width, height, font, font_size, tooltips_bool):
    # writing everything to config based on parameters, dev is set to false
    line1 = 'width = ' + str(width) + '\n'
    line2 = 'height = ' + str(height) + '\n'
    line3 = 'font = \'' + str(font) + '\'\n'
    line4 = 'font_size = ' + str(font_size) + '\n'
    line5 = 'enable_tooltips = ' + str(tooltips_bool) + '\n'
    # line6 = 'enable_developer = ' + str(dev) + '\n'
    line6 = 'enable_developer = False\n'

    file.writelines(
        ['# program configuration\n',
         '\n',
         '# modify program resolution\n',
         line1,
         line2,
         '\n',
         '# modify program font\n',
         line3,
         line4,
         '\n',
         '# enable tooltips\n',
         line5,
         '\n',
         '# enable developer\n',
         line6
         ]
    )

    file.close()


def clearALL():
    # clear all entries in GUI
    width_entry.entry.delete(0, END)
    height_entry.entry.delete(0, END)
    font_entry.entry.delete(0, END)
    font_size_entry.entry.delete(0, END)


def setAll():
    # set all entries in GUI from imported vars from userconfig.py
    clearALL()

    width_entry.entry.insert(0, str(config_width))
    height_entry.entry.insert(0, str(config_height))
    font_entry.entry.insert(0, str(config_font))
    font_size_entry.entry.insert(0, str(config_font_size))

    if config_tooltips:
        tooltips_button.func1()

    if not config_tooltips:
        tooltips_button.func2()


def checkAll():
    # checking that values are reasonable
    # currently only checks that resolution is 16 by 9 and is a common resolution
    input_width = width_entry.entry.get()
    input_height = height_entry.entry.get()

    width_list = ['1280', '1920', '2560', '3840']
    height_list = ['720', '1080', '1440', '2160']

    if input_width not in width_list \
            or input_height not in height_list \
            or float(input_width) / float(input_height) != 16.0 / 9:
        showwarning('Resolution Warning!', 'You have selected a non standard resolution\n'
                                           'This may cause visual errors\n')
        return True

    else:
        return True


def funcReset():
    # reset to defaults
    clearALL()

    width_entry.entry.insert(0, '1280')
    height_entry.entry.insert(0, '720')
    font_entry.entry.insert(0, 'Helvetica')
    font_size_entry.entry.insert(0, '12')

    setattr(tooltips_button, 'enabled', True)
    tooltips_button.f2.frame.tkraise()


def funcSave():
    # save and write to config
    if checkAll():
        writeConfig(openConfig(),
                    width_entry.entry.get(),
                    height_entry.entry.get(),
                    font_entry.entry.get(),
                    font_size_entry.entry.get(),
                    getattr(tooltips_button, 'enabled')
                    )


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


# creating program-wide binds
def program_restart_bind(event):
    program_restart()


def program_quit_bind(event):
    program_quit()


# binds
# binding control + q to quit program
root.bind('<Control-q>', program_quit_bind)

# binding control + r to restart the program
root.bind('<Control-r>', program_restart_bind)

# creating objects
title_label = MyLabel(root, 'Modify Program Settings', 0.25, 0.10)
title_label.label.configure(font=MyFonts['LargeBold'])
title_label.label.place(relwidth=0.5)

width_entry = MyEntry(root, 'Window Width (pixels)', 0.25, 0.25)
width_entry.label.configure(font=MyFonts['LargeBold'])
width_entry.entry.place(relwidth=0.50)

height_entry = MyEntry(root, 'Window Height (pixels)', 0.25, 0.40)
height_entry.label.configure(font=MyFonts['LargeBold'])
height_entry.entry.place(relwidth=0.50)

font_entry = MyEntry(root, 'Font Name', 0.25, 0.55)
font_entry.label.configure(font=MyFonts['LargeBold'])
font_entry.entry.place(relwidth=0.50)

font_size_entry = MyEntry(root, 'Font Size (points)', 0.25, 0.70)
font_size_entry.label.configure(font=MyFonts['LargeBold'])
font_size_entry.entry.place(relwidth=0.50)

tooltips_button = MyToggleButton(root, 'Tooltips', 0.25, 0.85)

reset_button = MyImageButton(root, GrayScale(20), CreateTkImage('data/images/reset.png', 48, 48), funcReset, 0.50, 0.85)
reset_button.button.place(relwidth=0.14, relheight=0.07)

save_button = MyImageButton(root, GrayScale(20), CreateTkImage('data/images/save.png', 48, 48), funcSave, 0.70, 0.85)
save_button.button.place(relwidth=0.14, relheight=0.07)

setAll()

# mainloop
root.mainloop()
