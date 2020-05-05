# preferences component class

# imports
from Tkinter import END
from tkMessageBox import showwarning, showinfo

from data.myclasses import MyFrame, MyLabel, MyEntry, MyToggleButton, MyImageButton
from data.myfunctions import program_restart, GrayScale, CreateTkImage, setAllTrue
from data.myvariables import MyFonts
from data.myvariables.userconfig import width as config_width
from data.myvariables.userconfig import height as config_height
from data.myvariables.userconfig import font as config_font
from data.myvariables.userconfig import font_size as config_font_size
from data.myvariables.userconfig import enable_tooltips as config_tooltips


def openConfig():
    # open userconfig.py for full overwrite
    myfile = open('data/myvariables/userconfig.py', 'w')
    return myfile


def writeConfig(myfile, width, height, font, font_size, tooltips_bool):
    # writing everything to config based on parameters, dev is set to false
    line1 = 'width = ' + str(width) + '\n'
    line2 = 'height = ' + str(height) + '\n'
    line3 = 'font = \'' + str(font) + '\'\n'
    line4 = 'font_size = ' + str(font_size) + '\n'
    line5 = 'enable_tooltips = ' + str(tooltips_bool) + '\n'
    # line6 = 'enable_developer = ' + str(dev) + '\n'
    line6 = 'enable_developer = False\n'

    myfile.writelines(
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
         line6,
         '\n',
         '# Oh Hello There\n'
         ]
    )

    myfile.close()


class MyPreferencesFrame(object):
    def __init__(self, root):
        self.parent = root

        self.main_bf = MyFrame(self.parent, GrayScale(20))
        self.create_objects()

        self.setAll()

    def create_objects(self):
        self.title_label = MyLabel(self.main_bf, 'Modify Program Settings', 0.05, 0.05)
        self.title_label.configure(font=MyFonts['ExtraLargeBold'])
        self.title_label.place(relwidth=0.9)

        self.width_entry = MyEntry(self.main_bf, 'Window Width (pixels)', 0.25, 0.20)
        self.width_entry.label.place(relwidth=0.90, relx=0.05)
        self.width_entry.place(relwidth=0.50)

        self.height_entry = MyEntry(self.main_bf, 'Window Height (pixels)', 0.25, 0.35)
        self.height_entry.label.place(relwidth=0.90, relx=0.05)
        self.height_entry.place(relwidth=0.50)

        self.font_entry = MyEntry(self.main_bf, 'Font Name', 0.25, 0.50)
        self.font_entry.label.place(relwidth=0.90, relx=0.05)
        self.font_entry.place(relwidth=0.50)

        self.font_size_entry = MyEntry(self.main_bf, 'Font Size (points)', 0.25, 0.65)
        self.font_size_entry.label.place(relwidth=0.90, relx=0.05)
        self.font_size_entry.place(relwidth=0.50)

        self.tooltips_button = MyToggleButton(self.main_bf, 'Tooltips', 0.15, 0.80)

        self.reset_button = MyImageButton(self.main_bf, GrayScale(20), CreateTkImage('data/images/reset.png', 48, 48),
                                          self.funcReset,
                                          0.45, 0.82)
        self.reset_button.place(relwidth=0.14, relheight=0.07)

        self.save_button = MyImageButton(self.main_bf, GrayScale(20), CreateTkImage('data/images/save.png', 48, 48),
                                         self.funcSave, 0.70,
                                         0.82)
        self.save_button.place(relwidth=0.14, relheight=0.07)

    def clearALL(self):
        # clear all entries in GUI
        self.width_entry.delete(0, END)
        self.height_entry.delete(0, END)
        self.font_entry.delete(0, END)
        self.font_size_entry.delete(0, END)

    def setAll(self):
        # set all entries in GUI from imported vars from userconfig.py
        self.clearALL()

        self.width_entry.insert(0, str(config_width))
        self.height_entry.insert(0, str(config_height))
        self.font_entry.insert(0, str(config_font))
        self.font_size_entry.insert(0, str(config_font_size))

        if config_tooltips:
            self.tooltips_button.func1()

        if not config_tooltips:
            self.tooltips_button.func2()

    def checkAll(self):
        # checking that values are reasonable
        # currently only checks that resolution is 16 by 9 and is a common resolution
        input_width = self.width_entry.get()
        input_height = self.height_entry.get()

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

    def funcReset(self):
        # reset to defaults
        self.clearALL()

        self.width_entry.insert(0, '1280')
        self.height_entry.insert(0, '720')
        self.font_entry.insert(0, 'Helvetica')
        self.font_size_entry.insert(0, '12')

        setattr(self.tooltips_button, 'enabled', True)
        self.tooltips_button.f2.tkraise()

        # reset all saved ask again boolean variables
        setAllTrue()

        showinfo('Settings Reset', 'All settings reset to default')

    def funcSave(self):
        # save and write to config
        if self.checkAll():
            writeConfig(openConfig(),
                        self.width_entry.get(),
                        self.height_entry.get(),
                        self.font_entry.get(),
                        self.font_size_entry.get(),
                        getattr(self.tooltips_button, 'enabled')
                        )

        showinfo('Settings Saved', 'Settings Saved, click OK to restart')

        program_restart()
