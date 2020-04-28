# image components class

# imports
from Tkinter import Label
from data.myvariables import dev
from data.myfunctions import CreateTkImage, GrayScale
from data.myclasses import MyFrame


# Creating MyImageFrame
class MyImageFrame(object):
    def __init__(self, parent, path, x_size, y_size):
        if dev:
            print '[image] image created from ' + path
        self.img_frame = MyFrame(parent, GrayScale(20))

        img_object = CreateTkImage(path, x_size, y_size)

        self.img_label = Label(self.img_frame.frame, image=img_object)
        self.img_label.image = img_object
        self.img_label.place(relx=0, rely=0, relwidth=1, relheight=1)
