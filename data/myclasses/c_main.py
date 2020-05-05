# main component class
# -*- encoding: utf-8 -*-

# imports
from Tkinter import END

from c_other import MyFrame, MyFrameWBP1, MyInputFrame, MyOutputFrame, \
    MyCanvas, MyLabel, MyScale, MyInputScale, MyOutputEntry, MyButton, MyImageButton, MyCycleButton3

from data.myfunctions import CreateToolTip, CreateTkImage, GrayScale, atl, \
    Moment_Inertia, Angular_Momentum, Linear_Momentum, \
    Rotational_Kinetic_Energy, Linear_Kinetic_Energy, TKE, \
    orbiting_particle_animation, rotating_circle_animation, rolling_circle_animation
from data.myvariables import dev, tooltips, MyFonts, \
    fb_rely_primary, fb_rely_secondary, \
    canvas_width, canvas_height, particle_constant, circle_constant, \
    start_geometry, start_width, start_height, main_geometry, main_width, main_height


class MyMainFrame(object):
    def __init__(self, root):
        # assigning parameters to attributes
        self.parent = root

        # creating first fun variables
        self.fr0 = True
        self.fr1 = True
        self.fr2 = True
        self.fr3 = True
        self.fr4 = True
        self.fr5 = True
        self.fr6 = True
        self.fr7 = True
        self.fr8 = True
        self.fr9 = True

        # creating defaults
        self.defaults()

    def defaults(self):
        # creating frames, navigation buttons and animation frame
        self.create_frames()
        self.create_nav()

        self.create_animation_frame()
        self.create_scales()

        # creating frame1, frame2, frame3 objects
        self.create_frame1()
        self.create_frame2()
        self.create_frame3()

        # select frames (main_pf1, frame1, frame1a)
        self.flip_main_pf1()
        self.flip_frame1()

    # noinspection DuplicatedCode,DuplicatedCode
    def create_frames(self):
        if dev:
            print '[main] frames created'

        self.main_bf = MyFrame(self.parent, GrayScale(20))
        self.main_pf1 = MyFrame(self.main_bf, GrayScale(20))
        self.main_pf2 = MyFrame(self.main_bf, GrayScale(20))
        self.scales = MyInputFrame(self.main_pf1, GrayScale(20))
        self.frame1 = MyFrameWBP1(self.main_pf1, GrayScale(20))
        self.frame2 = MyFrameWBP1(self.main_pf1, GrayScale(20))
        self.frame3 = MyFrameWBP1(self.main_pf1, GrayScale(20))
        self.frame1a = MyOutputFrame(self.frame1, GrayScale(20))
        self.frame1b = MyOutputFrame(self.frame1, GrayScale(20))
        self.frame1c = MyOutputFrame(self.frame1, GrayScale(20))
        self.frame2a = MyOutputFrame(self.frame2, GrayScale(20))
        self.frame2b = MyOutputFrame(self.frame2, GrayScale(20))
        self.frame2c = MyOutputFrame(self.frame2, GrayScale(20))
        self.frame3a = MyOutputFrame(self.frame3, GrayScale(20))
        self.frame3b = MyOutputFrame(self.frame3, GrayScale(20))
        self.frame3c = MyOutputFrame(self.frame3, GrayScale(20))

    def create_nav(self):
        if dev:
            print '[main] navigation buttons created'

        self.enter_as = MyImageButton(self.main_pf1, GrayScale(20),
                                      CreateTkImage('data/images/settings.png', 32, 32),
                                      self.flip_main_pf2, 0.05, fb_rely_primary
                                      )

        self.exit_as = MyImageButton(self.main_pf2, GrayScale(20),
                                     CreateTkImage('data/images/back.png', 32, 32),
                                     self.flip_main_pf1, 0.175, 0.85
                                     )

        self.exit_as.place(relwidth=0.125, relheight=0.0625)

        self.frame_cycle = MyCycleButton3(self.main_pf1,
                                          ['Orbiting Particle', 'Rotating Circle', 'Rolling Circle'],
                                          [self.scales, self.frame1, self.frame2, self.frame3],
                                          0.85, fb_rely_primary
                                          )

    def create_animation_frame(self):
        if dev:
            print '[main] animation frame objects created'

        self.main_pf2_title = MyLabel(self.main_pf2, 'Animation Settings', 0.175, 0.125)
        self.main_pf2_title.configure(bg=GrayScale(20), font=MyFonts['LargeBold'])
        self.main_pf2_title.place(relwidth=0.65)

        self.time_factor_scale = MyScale(self.main_pf2, 'Time Factor', 0.175, 0.25)
        self.len_mult_scale = MyScale(self.main_pf2, 'Length Multiplier', 0.175, 0.40)
        self.granularity_scale = MyScale(self.main_pf2, 'Granularity', 0.175, 0.55)

        self.time_factor_scale.configure(from_=1, to=100, resolution=1, bg=GrayScale(20))
        self.len_mult_scale.configure(from_=1, to=100, resolution=1, bg=GrayScale(20))
        self.granularity_scale.configure(from_=5, to=90, resolution=5, bg=GrayScale(20))

        self.time_factor_scale.label.configure(bg=GrayScale(20), font=MyFonts['Large'])
        self.len_mult_scale.label.configure(bg=GrayScale(20), font=MyFonts['Large'])
        self.granularity_scale.label.configure(bg=GrayScale(20), font=MyFonts['Large'])

        self.time_factor_scale.place(relwidth=0.65)
        self.len_mult_scale.place(relwidth=0.65)
        self.granularity_scale.place(relwidth=0.65)

        self.time_factor_scale.label.place(relwidth=0.65)
        self.len_mult_scale.label.place(relwidth=0.65)
        self.granularity_scale.label.place(relwidth=0.65)

        if dev:
            self.time_factor_scale.set(1)
            self.len_mult_scale.set(100)
            self.granularity_scale.set(5)

        if not dev:
            self.time_factor_scale.set(5)
            self.len_mult_scale.set(5)
            self.granularity_scale.set(5)

        if tooltips:
            CreateToolTip(self.time_factor_scale.label, 'Drag slider to adjust animation speed.'
                                                        '\nHigher value is faster.'
                          )

            CreateToolTip(self.len_mult_scale.label, 'Drag slider to adjust animation scale.'
                                                     '\nHigher value is bigger.'
                          )

            CreateToolTip(self.granularity_scale.label, 'Drag slider to adjust animation smoothness'
                                                        '\nHigher value is smoother'
                          )

    def create_scales(self):
        self.radius_scale = MyInputScale(self.scales, 'Radius (m)', 0.20, 0.25)
        self.mass_scale = MyInputScale(self.scales, 'Mass (kg)', 0.20, 0.40)
        self.ang_vel_scale = MyInputScale(self.scales, 'Angular Velocity (rad/s)', 0.20, 0.55)

        if tooltips:
            CreateToolTip(self.radius_scale.label, 'Drag slider to adjust radius')
            CreateToolTip(self.mass_scale.label, 'Drag slider to adjust mass')
            CreateToolTip(self.ang_vel_scale.label, 'Drag slider to adjust angular velocity')

        self.radius_scale.set(20.0)
        self.mass_scale.set(20.0)
        self.ang_vel_scale.set(20.0)

    # noinspection DuplicatedCode
    def create_frame1(self):
        if dev:
            print '[main] frame1 objects created'

        self.main_label_1 = MyLabel(self.frame1, 'Orbiting Particle', 0.40, 0.05)
        self.main_label_1.configure(font=MyFonts['ExtraLargeBold'])
        self.main_label_1.place(relwidth=0.20)

        self.animate_button_1 = MyButton(self.frame1, 'Animate', self.animate1, 0.05, fb_rely_secondary)
        self.frame1_canvas = MyCanvas(self.frame1)
        self.frame1_cycle = MyCycleButton3(self.frame1,
                                           ['Basic', 'Momentum', 'Energy'],
                                           [self.scales, self.frame1a, self.frame1b,
                                            self.frame1c],
                                           0.85, fb_rely_secondary
                                           )

        self.create_frame1a()
        self.create_frame1b()
        self.create_frame1c()

        self.frame1a.tkraise()

    # noinspection DuplicatedCode
    def create_frame2(self):
        if dev:
            print '[main] frame2 objects created'

        self.main_label_2 = MyLabel(self.frame2, 'Rotating Circle', 0.40, 0.05)
        self.main_label_2.configure(font=MyFonts['ExtraLargeBold'])
        self.main_label_2.place(relwidth=0.20)

        self.animate_button_2 = MyButton(self.frame2, 'Animate', self.animate2, 0.05, fb_rely_secondary)
        self.frame2_canvas = MyCanvas(self.frame2)
        self.frame2_cycle = MyCycleButton3(self.frame2,
                                           ['Basic', 'Momentum', 'Energy'],
                                           [self.scales, self.frame2a, self.frame2b, self.frame2c],
                                           0.85, fb_rely_secondary
                                           )

        self.create_frame2a()
        self.create_frame2b()
        self.create_frame2c()

        self.frame2a.tkraise()

    # noinspection DuplicatedCode
    def create_frame3(self):
        if dev:
            print '[main] frame3 objects created'

        self.main_label_3 = MyLabel(self.frame3, 'Rolling Circle', 0.40, 0.05)
        self.main_label_3.configure(font=MyFonts['ExtraLargeBold'])
        self.main_label_3.place(relwidth=0.20)

        self.animate_button_3 = MyButton(self.frame3, 'Animate', self.animate3, 0.05, fb_rely_secondary)
        self.frame3_canvas = MyCanvas(self.frame3)
        self.frame3_cycle = MyCycleButton3(self.frame3,
                                           ['Basic', 'Momentum', 'Energy'],
                                           [self.scales, self.frame3a, self.frame3b,
                                            self.frame3c],
                                           0.85, fb_rely_secondary
                                           )

        self.create_frame3a()
        self.create_frame3b()
        self.create_frame3c()

        self.frame3a.tkraise()

    # noinspection DuplicatedCode
    def create_frame1a(self):
        self.frame1a_entry1 = MyOutputEntry(self.frame1a, 'Moment of Inertia (kgm²)', 0.20, 0.25)

        self.calculate_button_1a = MyImageButton(self.frame1a, GrayScale(20),
                                                 CreateTkImage('data/images/calculator.png', 48, 48),
                                                 self.calculate_1a, 0.75, 0.25)
        self.calculate_button_1a.configure(bg=GrayScale(20), activebackground=GrayScale(20))
        self.calculate_button_1a.place(relwidth=0.10, relheight=0.10)

        if tooltips:
            CreateToolTip(self.frame1a_entry1.label, 'I = MR²')

    # noinspection DuplicatedCode
    def create_frame1b(self):
        self.frame1b_entry1 = MyOutputEntry(self.frame1b, 'Moment of Inertia (kgm²)', 0.20, 0.25)
        self.frame1b_entry2 = MyOutputEntry(self.frame1b, 'Angular Momentum (kgm²/s)', 0.20, 0.40)

        self.calculate_button_1b = MyImageButton(self.frame1b, GrayScale(20),
                                                 CreateTkImage('data/images/calculator.png', 48, 48),
                                                 self.calculate_1b, 0.75, 0.25)
        self.calculate_button_1b.configure(bg=GrayScale(20), activebackground=GrayScale(20))
        self.calculate_button_1b.place(relwidth=0.10, relheight=0.10)

        if tooltips:
            CreateToolTip(self.frame1b_entry1.label, 'I = MR²')
            CreateToolTip(self.frame1b_entry2.label, 'L = Iw')

    # noinspection DuplicatedCode
    def create_frame1c(self):
        self.frame1c_entry1 = MyOutputEntry(self.frame1c, 'Moment of Inertia (kgm²)', 0.20, 0.25)
        self.frame1c_entry2 = MyOutputEntry(self.frame1c, 'Rotational Kinetic Energy (J)', 0.20, 0.40)

        self.calculate_button_1c = MyImageButton(self.frame1c, GrayScale(20),
                                                 CreateTkImage('data/images/calculator.png', 48, 48),
                                                 self.calculate_1c, 0.75, 0.25)
        self.calculate_button_1c.configure(bg=GrayScale(20), activebackground=GrayScale(20))
        self.calculate_button_1c.place(relwidth=0.10, relheight=0.10)

        if tooltips:
            CreateToolTip(self.frame1c_entry1.label, 'I = MR²')
            CreateToolTip(self.frame1c_entry2.label, 'RKE = ½ Iw²')

    # noinspection DuplicatedCode
    def create_frame2a(self):
        self.frame2a_entry1 = MyOutputEntry(self.frame2a, 'Moment of Inertia (kgm²)', 0.20, 0.25)

        self.calculate_button_2a = MyImageButton(self.frame2a, GrayScale(20),
                                                 CreateTkImage('data/images/calculator.png', 48, 48),
                                                 self.calculate_2a, 0.75, 0.25)
        self.calculate_button_2a.configure(bg=GrayScale(20), activebackground=GrayScale(20))
        self.calculate_button_2a.place(relwidth=0.10, relheight=0.10)

        if tooltips:
            CreateToolTip(self.frame2a_entry1.label, 'I = ½ MR²')

    # noinspection DuplicatedCode
    def create_frame2b(self):
        self.frame2b_entry1 = MyOutputEntry(self.frame2b, 'Moment of Inertia (kgm²)', 0.20, 0.25)
        self.frame2b_entry2 = MyOutputEntry(self.frame2b, 'Angular Momentum (kgm²/s)', 0.20, 0.40)

        self.calculate_button_2b = MyImageButton(self.frame2b, GrayScale(20),
                                                 CreateTkImage('data/images/calculator.png', 48, 48),
                                                 self.calculate_2b, 0.75, 0.25)
        self.calculate_button_2b.configure(bg=GrayScale(20), activebackground=GrayScale(20))
        self.calculate_button_2b.place(relwidth=0.10, relheight=0.10)

        if tooltips:
            CreateToolTip(self.frame2b_entry1.label, 'I = ½ MR²')
            CreateToolTip(self.frame2b_entry2.label, 'L = Iw')

    # noinspection DuplicatedCode
    def create_frame2c(self):
        self.frame2c_entry1 = MyOutputEntry(self.frame2c, 'Moment of Inertia (kgm²)', 0.20, 0.25)
        self.frame2c_entry2 = MyOutputEntry(self.frame2c, 'Rotational Kinetic Energy (J)', 0.20, 0.40)

        self.calculate_button_2c = MyImageButton(self.frame2c, GrayScale(20),
                                                 CreateTkImage('data/images/calculator.png', 48, 48),
                                                 self.calculate_2c, 0.75, 0.25)
        self.calculate_button_2c.configure(bg=GrayScale(20), activebackground=GrayScale(20))
        self.calculate_button_2c.place(relwidth=0.10, relheight=0.10)

        if tooltips:
            CreateToolTip(self.frame2c_entry1.label, 'I = ½ MR²')
            CreateToolTip(self.frame2c_entry2.label, 'RKE = ½ Iw²')

    # noinspection DuplicatedCode
    def create_frame3a(self):
        self.frame3a_entry1 = MyOutputEntry(self.frame3a, 'Moment of Inertia (kgm²)', 0.20, 0.25)

        self.calculate_button_3a = MyImageButton(self.frame3a, GrayScale(20),
                                                 CreateTkImage('data/images/calculator.png', 48, 48),
                                                 self.calculate_3a, 0.75, 0.25)
        self.calculate_button_3a.configure(bg=GrayScale(20), activebackground=GrayScale(20))
        self.calculate_button_3a.place(relwidth=0.10, relheight=0.10)

        if tooltips:
            CreateToolTip(self.frame3a_entry1.label, 'I = ½ MR²')

    # noinspection DuplicatedCode
    def create_frame3b(self):
        self.frame3b_entry1 = MyOutputEntry(self.frame3b, 'Moment of Inertia (kgm²)', 0.20, 0.25)
        self.frame3b_entry2 = MyOutputEntry(self.frame3b, 'Angular Momentum (kgm²/s)', 0.20, 0.40)
        self.frame3b_entry3 = MyOutputEntry(self.frame3b, 'Linear Momentum (kgm/s)', 0.20, 0.55)

        self.calculate_button_3b = MyImageButton(self.frame3b, GrayScale(20),
                                                 CreateTkImage('data/images/calculator.png', 48, 48),
                                                 self.calculate_3b, 0.75, 0.25)
        self.calculate_button_3b.configure(bg=GrayScale(20), activebackground=GrayScale(20))
        self.calculate_button_3b.place(relwidth=0.10, relheight=0.10)

        if tooltips:
            CreateToolTip(self.frame3b_entry1.label, 'I = ½ MR²')
            CreateToolTip(self.frame3b_entry2.label, 'L = Iw')
            CreateToolTip(self.frame3b_entry3.label, 'p = MV')

    # noinspection DuplicatedCode
    def create_frame3c(self):
        self.frame3c_entry1 = MyOutputEntry(self.frame3c, 'Moment of Inertia (kgm²)', 0.20, 0.25)
        self.frame3c_entry2 = MyOutputEntry(self.frame3c, 'Rotational Kinetic Energy (J)', 0.20, 0.40)
        self.frame3c_entry3 = MyOutputEntry(self.frame3c, 'Linear Kinetic Energy (J)', 0.20, 0.55)
        self.frame3c_entry4 = MyOutputEntry(self.frame3c, 'Total Kinetic Energy (J)', 0.20, 0.70)

        self.calculate_button_3c = MyImageButton(self.frame3c, GrayScale(20),
                                                 CreateTkImage('data/images/calculator.png', 48, 48),
                                                 self.calculate_3c, 0.75, 0.25)
        self.calculate_button_3c.configure(bg=GrayScale(20), activebackground=GrayScale(20))
        self.calculate_button_3c.place(relwidth=0.10, relheight=0.10)

        if tooltips:
            CreateToolTip(self.frame3c_entry1.label, 'I = ½ MR²')
            CreateToolTip(self.frame3c_entry2.label, 'RKE = ½ Iw²')
            CreateToolTip(self.frame3c_entry3.label, 'LKE = ½ MV²')
            CreateToolTip(self.frame3c_entry4.label, 'TKE = RKE + LKE')

    def flip_main_pf1(self):
        self.main_pf1.tkraise()
        self.parent.geometry(
            main_geometry + '+' + str(self.parent.winfo_screenwidth() / 2 - main_width / 2) + '+' + str(
                self.parent.winfo_screenheight() / 2 - main_height / 2))

        self.in_animation_settings = False

    def flip_main_pf2(self):
        if self.fr0:
            self.create_animation_frame()
            self.fr0 = False

        self.main_pf2.tkraise()
        self.parent.geometry(
            start_geometry + '+' + str(self.parent.winfo_screenwidth() / 2 - start_width / 2) + '+' + str(
                self.parent.winfo_screenheight() / 2 - start_height / 2))

        self.in_animation_settings = True

    def flip_frame1(self):
        self.frame1.tkraise()
        self.frame1a.tkraise()
        self.scales.tkraise()

    def flip_frame2(self):
        self.frame2.tkraise()
        self.frame2a.tkraise()
        self.scales.tkraise()

    def flip_frame3(self):
        self.frame3.tkraise()
        self.frame3a.tkraise()
        self.scales.tkraise()

    # noinspection DuplicatedCode
    def calculate_1a(self):
        var1 = self.radius_scale.get()
        var2 = self.mass_scale.get()
        ans1 = Moment_Inertia(particle_constant, var1, var2)
        self.frame1a_entry1.delete(0, END)
        self.frame1a_entry1.insert(0, round(ans1, 2))

    # calculate 1b
    # noinspection DuplicatedCode
    def calculate_1b(self):
        var1 = self.radius_scale.get()
        var2 = self.mass_scale.get()
        var3 = self.ang_vel_scale.get()
        ans1 = Moment_Inertia(particle_constant, var1, var2)
        ans2 = Angular_Momentum(ans1, var3)
        self.frame1b_entry1.delete(0, END)
        self.frame1b_entry1.insert(0, round(ans1, 2))
        self.frame1b_entry2.delete(0, END)
        self.frame1b_entry2.insert(0, round(ans2, 2))

    # calculate 1c
    # noinspection DuplicatedCode
    def calculate_1c(self):
        var1 = self.radius_scale.get()
        var2 = self.mass_scale.get()
        var3 = self.ang_vel_scale.get()
        ans1 = Moment_Inertia(particle_constant, var1, var2)
        ans2 = Rotational_Kinetic_Energy(ans1, var3)
        self.frame1c_entry1.delete(0, END)
        self.frame1c_entry1.insert(0, round(ans1, 2))
        self.frame1c_entry2.delete(0, END)
        self.frame1c_entry2.insert(0, round(ans2, 2))

    # calculate 2a
    # noinspection DuplicatedCode
    def calculate_2a(self):
        var1 = self.radius_scale.get()
        var2 = self.mass_scale.get()
        ans1 = Moment_Inertia(circle_constant, var1, var2)
        self.frame2a_entry1.delete(0, END)
        self.frame2a_entry1.insert(0, round(ans1, 2))

    # calculate 2b
    # noinspection DuplicatedCode
    def calculate_2b(self):
        var1 = self.radius_scale.get()
        var2 = self.mass_scale.get()
        var3 = self.ang_vel_scale.get()
        ans1 = Moment_Inertia(circle_constant, var1, var2)
        ans2 = Angular_Momentum(ans1, var3)
        self.frame2b_entry1.delete(0, END)
        self.frame2b_entry1.insert(0, round(ans1, 2))
        self.frame2b_entry2.delete(0, END)
        self.frame2b_entry2.insert(0, round(ans2, 2))

    # calculate 2c
    # noinspection DuplicatedCode
    def calculate_2c(self):
        var1 = self.radius_scale.get()
        var2 = self.mass_scale.get()
        var3 = self.ang_vel_scale.get()
        ans1 = Moment_Inertia(circle_constant, var1, var2)
        ans2 = Rotational_Kinetic_Energy(ans1, var3)
        self.frame2c_entry1.delete(0, END)
        self.frame2c_entry1.insert(0, round(ans1, 2))
        self.frame2c_entry2.delete(0, END)
        self.frame2c_entry2.insert(0, round(ans2, 2))

    # calculate 3a
    # noinspection DuplicatedCode
    def calculate_3a(self):
        var1 = self.radius_scale.get()
        var2 = self.mass_scale.get()
        ans1 = Moment_Inertia(circle_constant, var1, var2)
        self.frame3a_entry1.delete(0, END)
        self.frame3a_entry1.insert(0, round(ans1, 2))

    # calculate 3b
    # noinspection DuplicatedCode
    def calculate_3b(self):
        var1 = self.radius_scale.get()
        var2 = self.mass_scale.get()
        var3 = self.ang_vel_scale.get()
        var4 = atl(var3, var1)
        ans1 = Moment_Inertia(circle_constant, var1, var2)
        ans2 = Angular_Momentum(ans1, var3)
        ans3 = Linear_Momentum(var2, var4)
        self.frame3b_entry1.delete(0, END)
        self.frame3b_entry1.insert(0, round(ans1, 2))
        self.frame3b_entry2.delete(0, END)
        self.frame3b_entry2.insert(0, round(ans2, 2))
        self.frame3b_entry3.delete(0, END)
        self.frame3b_entry3.insert(0, round(ans3, 2))

    # calculate 3c
    # noinspection DuplicatedCode
    def calculate_3c(self):
        var1 = self.radius_scale.get()
        var2 = self.mass_scale.get()
        var3 = self.ang_vel_scale.get()
        var4 = atl(var3, var1)
        ans1 = Moment_Inertia(circle_constant, var1, var2)
        ans2 = Rotational_Kinetic_Energy(ans1, var3)
        ans3 = Linear_Kinetic_Energy(var2, var4)
        ans4 = TKE(ans2, ans3)
        self.frame3c_entry1.delete(0, END)
        self.frame3c_entry1.insert(0, round(ans1, 2))
        self.frame3c_entry2.delete(0, END)
        self.frame3c_entry2.insert(0, round(ans2, 2))
        self.frame3c_entry3.delete(0, END)
        self.frame3c_entry3.insert(0, round(ans3, 2))
        self.frame3c_entry4.delete(0, END)
        self.frame3c_entry4.insert(0, round(ans4, 2))

    # animate orbiting particle
    def animate1(self):
        orbiting_particle_animation(self.parent,
                                    self.frame1_canvas,
                                    float(canvas_width) / 2.0,
                                    float(canvas_height) / 2.0,
                                    float(self.radius_scale.get()) * float(self.len_mult_scale.get()),
                                    float(self.ang_vel_scale.get()) / float(self.time_factor_scale.get()),
                                    self.granularity_scale.get()
                                    )

    # animate rotating circle
    def animate2(self):
        rotating_circle_animation(self.parent,
                                  self.frame2_canvas,
                                  float(canvas_width) / 2.0,
                                  float(canvas_height) / 2.0,
                                  float(self.radius_scale.get()) * float(self.len_mult_scale.get()),
                                  float(self.ang_vel_scale.get()) / float(
                                      self.time_factor_scale.get()),
                                  self.granularity_scale.get()
                                  )

    # animate rolling circle
    def animate3(self):
        rolling_circle_animation(self.parent,
                                 self.frame3_canvas,
                                 float(canvas_width) / 2.0,
                                 float(canvas_height) / 2.0,
                                 float(self.radius_scale.get()) * float(self.len_mult_scale.get()),
                                 float(self.ang_vel_scale.get()) / float(self.time_factor_scale.get()),
                                 self.granularity_scale.get()
                                 )
