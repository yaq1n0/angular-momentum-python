# main component class
# -*- encoding: utf-8 -*-

# imports
from Tkinter import END
from data.myvariables import dev, tooltips, MyFonts, \
    frame_bottom_pad1, fb_rely_primary, fb_rely_secondary, \
    canvas_width, canvas_height, particle_constant, circle_constant, \
    start_geometry, start_width, start_height, main_geometry, main_width, main_height
from data.myfunctions import CreateToolTip, CreateTkImage, GrayScale, atl, \
    Moment_Inertia, Angular_Momentum, Linear_Momentum, \
    Rotational_Kinetic_Energy, Linear_Kinetic_Energy, TKE, \
    orbiting_particle_animation, rotating_circle_animation, rolling_circle_animation
from data.myclasses import MyFrame, MyFrameWBP, MyInputFrame, MyOutputFrame, MyCanvas, MyLabel, MyScale, MyInputScale, \
    MyOutputEntry, \
    MyButton, MyImageButton, MyCycleButton


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

    def create_frames(self):
        if dev:
            print '[main] frames created'

        self.main_bf = MyFrame(self.parent, GrayScale(20))
        self.main_pf1 = MyFrame(self.main_bf.frame, GrayScale(20))
        self.main_pf2 = MyFrame(self.main_bf.frame, GrayScale(20))
        self.scales = MyInputFrame(self.main_bf.frame, GrayScale(20))
        self.frame1 = MyFrameWBP(self.main_bf.frame, GrayScale(20), frame_bottom_pad1)
        self.frame2 = MyFrameWBP(self.main_bf.frame, GrayScale(20), frame_bottom_pad1)
        self.frame3 = MyFrameWBP(self.main_bf.frame, GrayScale(20), frame_bottom_pad1)
        self.frame1a = MyOutputFrame(self.frame1.frame, GrayScale(20))
        self.frame1b = MyOutputFrame(self.frame1.frame, GrayScale(20))
        self.frame1c = MyOutputFrame(self.frame1.frame, GrayScale(20))
        self.frame2a = MyOutputFrame(self.frame2.frame, GrayScale(20))
        self.frame2b = MyOutputFrame(self.frame2.frame, GrayScale(20))
        self.frame2c = MyOutputFrame(self.frame2.frame, GrayScale(20))
        self.frame3a = MyOutputFrame(self.frame3.frame, GrayScale(20))
        self.frame3b = MyOutputFrame(self.frame3.frame, GrayScale(20))
        self.frame3c = MyOutputFrame(self.frame3.frame, GrayScale(20))

    def create_nav(self):
        if dev:
            print '[main] navigation buttons created'

        self.enter_as = MyImageButton(self.main_pf1.frame, GrayScale(20),
                                      CreateTkImage('data/images/settings.png', 32, 32),
                                      self.flip_main_pf2, 0.05, fb_rely_primary
                                      )

        self.exit_as = MyImageButton(self.main_pf2.frame, GrayScale(20),
                                     CreateTkImage('data/images/back.png', 32, 32),
                                     self.flip_main_pf1, 0.175, 0.85
                                     )

        self.exit_as.button.place(relwidth=0.125, relheight=0.0625)

        self.frame_cycle = MyCycleButton(self.main_pf1.frame,
                                         ['Orbiting Particle', 'Rotating Circle', 'Rolling Circle'],
                                         [self.scales.frame, self.frame1.frame, self.frame2.frame, self.frame3.frame],
                                         0.85, fb_rely_primary
                                         )

    def create_animation_frame(self):
        if dev:
            print '[main] animation frame objects created'

        self.main_pf2_title = MyLabel(self.main_pf2.frame, 'Animation Settings', 0.175, 0.125)
        self.main_pf2_title.label.configure(bg=GrayScale(20), font=MyFonts['LargeBold'])
        self.main_pf2_title.label.place(relwidth=0.65)

        self.time_factor_scale = MyScale(self.main_pf2.frame, 'Time Factor', 0.175, 0.25)
        self.len_mult_scale = MyScale(self.main_pf2.frame, 'Length Multiplier', 0.175, 0.40)
        self.granularity_scale = MyScale(self.main_pf2.frame, 'Granularity', 0.175, 0.55)

        self.time_factor_scale.scale.configure(from_=1, to=100, resolution=1, bg=GrayScale(20))
        self.len_mult_scale.scale.configure(from_=1, to=100, resolution=1, bg=GrayScale(20))
        self.granularity_scale.scale.configure(from_=5, to=90, resolution=5, bg=GrayScale(20))

        self.time_factor_scale.label.configure(bg=GrayScale(20), font=MyFonts['Large'])
        self.len_mult_scale.label.configure(bg=GrayScale(20), font=MyFonts['Large'])
        self.granularity_scale.label.configure(bg=GrayScale(20), font=MyFonts['Large'])

        self.time_factor_scale.scale.place(relwidth=0.65)
        self.len_mult_scale.scale.place(relwidth=0.65)
        self.granularity_scale.scale.place(relwidth=0.65)

        self.time_factor_scale.label.place(relwidth=0.65)
        self.len_mult_scale.label.place(relwidth=0.65)
        self.granularity_scale.label.place(relwidth=0.65)

        if dev:
            self.time_factor_scale.scale.set(1)
            self.len_mult_scale.scale.set(100)
            self.granularity_scale.scale.set(5)

        if not dev:
            self.time_factor_scale.scale.set(5)
            self.len_mult_scale.scale.set(10)
            self.granularity_scale.scale.set(15)

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
        self.radius_scale = MyInputScale(self.scales.frame, 'Radius (m)', 0.20, 0.25)
        self.mass_scale = MyInputScale(self.scales.frame, 'Mass (kg)', 0.20, 0.40)
        self.ang_vel_scale = MyInputScale(self.scales.frame, 'Angular Velocity (rad/s)', 0.20, 0.55)

        if tooltips:
            CreateToolTip(self.radius_scale.label, 'Drag slider to adjust radius')
            CreateToolTip(self.mass_scale.label, 'Drag slider to adjust mass')
            CreateToolTip(self.ang_vel_scale.label, 'Drag slider to adjust angular velocity')

    def create_frame1(self):
        if dev:
            print '[main] frame1 objects created'

        self.main_label_1 = MyLabel(self.frame1.frame, 'Orbiting Particle', 0.40, 0.05)
        self.main_label_1.label.configure(font=MyFonts['ExtraLargeBold'])
        self.main_label_1.label.place(relwidth=0.20)

        self.animate_button_1 = MyButton(self.frame1.frame, 'Animate', self.animate1, 0.05, fb_rely_secondary)
        self.frame1_canvas = MyCanvas(self.frame1.frame)
        self.frame1_cycle = MyCycleButton(self.frame1.frame,
                                          ['Basic', 'Momentum', 'Energy'],
                                          [self.scales.frame, self.frame1a.frame, self.frame1b.frame,
                                           self.frame1c.frame],
                                          0.85, fb_rely_secondary
                                          )

        self.create_frame1a()
        self.create_frame1b()
        self.create_frame1c()

        self.frame1a.frame.tkraise()

    def create_frame2(self):
        if dev:
            print '[main] frame2 objects created'

        self.main_label_2 = MyLabel(self.frame2.frame, 'Rotating Circle', 0.40, 0.05)
        self.main_label_2.label.configure(font=MyFonts['ExtraLargeBold'])
        self.main_label_2.label.place(relwidth=0.20)

        self.animate_button_2 = MyButton(self.frame2.frame, 'Animate', self.animate2, 0.05, fb_rely_secondary)
        self.frame2_canvas = MyCanvas(self.frame2.frame)
        self.frame2_cycle = MyCycleButton(self.frame2.frame,
                                          ['Basic', 'Momentum', 'Energy'],
                                          [self.scales.frame, self.frame2a.frame, self.frame2b.frame,
                                           self.frame2c.frame],
                                          0.85, fb_rely_secondary
                                          )

        self.create_frame2a()
        self.create_frame2b()
        self.create_frame2c()

        self.frame2a.frame.tkraise()

    def create_frame3(self):
        if dev:
            print '[main] frame3 objects created'

        self.main_label_3 = MyLabel(self.frame3.frame, 'Rolling Circle', 0.40, 0.05)
        self.main_label_3.label.configure(font=MyFonts['ExtraLargeBold'])
        self.main_label_3.label.place(relwidth=0.20)

        self.animate_button_3 = MyButton(self.frame3.frame, 'Animate', self.animate3, 0.05, fb_rely_secondary)
        self.frame3_canvas = MyCanvas(self.frame3.frame)
        self.frame3_cycle = MyCycleButton(self.frame3.frame,
                                          ['Basic', 'Momentum', 'Energy'],
                                          [self.scales.frame, self.frame3a.frame, self.frame3b.frame,
                                           self.frame3c.frame],
                                          0.85, fb_rely_secondary
                                          )

        self.create_frame3a()
        self.create_frame3b()
        self.create_frame3c()

        self.frame3a.frame.tkraise()

    def create_frame1a(self):
        self.frame1a_entry1 = MyOutputEntry(self.frame1a.frame, 'Moment of Inertia (kgm²)', 0.20, 0.25)

        self.calculate_button_1a = MyImageButton(self.frame1a.frame, GrayScale(20),
                                                 CreateTkImage('data/images/calculator.png', 48, 48),
                                                 self.calculate_1a, 0.75, 0.25)
        self.calculate_button_1a.button.configure(bg=GrayScale(20), activebackground=GrayScale(20))
        self.calculate_button_1a.button.place(relwidth=0.10, relheight=0.10)

        if tooltips:
            CreateToolTip(self.frame1a_entry1.label, 'I = MR²')

    def create_frame1b(self):
        self.frame1b_entry1 = MyOutputEntry(self.frame1b.frame, 'Moment of Inertia (kgm²)', 0.20, 0.25)
        self.frame1b_entry2 = MyOutputEntry(self.frame1b.frame, 'Angular Momentum (kgm²/s)', 0.20, 0.40)

        self.calculate_button_1b = MyImageButton(self.frame1b.frame, GrayScale(20),
                                                 CreateTkImage('data/images/calculator.png', 48, 48),
                                                 self.calculate_1b, 0.75, 0.25)
        self.calculate_button_1b.button.configure(bg=GrayScale(20), activebackground=GrayScale(20))
        self.calculate_button_1b.button.place(relwidth=0.10, relheight=0.10)

        if tooltips:
            CreateToolTip(self.frame1b_entry1.label, 'I = MR²')
            CreateToolTip(self.frame1b_entry2.label, 'L = Iw')

    def create_frame1c(self):
        self.frame1c_entry1 = MyOutputEntry(self.frame1c.frame, 'Moment of Inertia (kgm²)', 0.20, 0.25)
        self.frame1c_entry2 = MyOutputEntry(self.frame1c.frame, 'Rotational Kinetic Energy (J)', 0.20, 0.40)

        self.calculate_button_1c = MyImageButton(self.frame1c.frame, GrayScale(20),
                                                 CreateTkImage('data/images/calculator.png', 48, 48),
                                                 self.calculate_1c, 0.75, 0.25)
        self.calculate_button_1c.button.configure(bg=GrayScale(20), activebackground=GrayScale(20))
        self.calculate_button_1c.button.place(relwidth=0.10, relheight=0.10)

        if tooltips:
            CreateToolTip(self.frame1c_entry1.label, 'I = MR²')
            CreateToolTip(self.frame1c_entry2.label, 'RKE = ½ Iw²')

    def create_frame2a(self):
        self.frame2a_entry1 = MyOutputEntry(self.frame2a.frame, 'Moment of Inertia (kgm²)', 0.20, 0.25)

        self.calculate_button_2a = MyImageButton(self.frame2a.frame, GrayScale(20),
                                                 CreateTkImage('data/images/calculator.png', 48, 48),
                                                 self.calculate_2a, 0.75, 0.25)
        self.calculate_button_2a.button.configure(bg=GrayScale(20), activebackground=GrayScale(20))
        self.calculate_button_2a.button.place(relwidth=0.10, relheight=0.10)

        if tooltips:
            CreateToolTip(self.frame2a_entry1.label, 'I = ½ MR²')

    def create_frame2b(self):
        self.frame2b_entry1 = MyOutputEntry(self.frame2b.frame, 'Moment of Inertia (kgm²)', 0.20, 0.25)
        self.frame2b_entry2 = MyOutputEntry(self.frame2b.frame, 'Angular Momentum (kgm²/s)', 0.20, 0.40)

        self.calculate_button_2b = MyImageButton(self.frame2b.frame, GrayScale(20),
                                                 CreateTkImage('data/images/calculator.png', 48, 48),
                                                 self.calculate_2b, 0.75, 0.25)
        self.calculate_button_2b.button.configure(bg=GrayScale(20), activebackground=GrayScale(20))
        self.calculate_button_2b.button.place(relwidth=0.10, relheight=0.10)

        if tooltips:
            CreateToolTip(self.frame2b_entry1.label, 'I = ½ MR²')
            CreateToolTip(self.frame2b_entry2.label, 'L = Iw')

    def create_frame2c(self):
        self.frame2c_entry1 = MyOutputEntry(self.frame2c.frame, 'Moment of Inertia (kgm²)', 0.20, 0.25)
        self.frame2c_entry2 = MyOutputEntry(self.frame2c.frame, 'Rotational Kinetic Energy (J)', 0.20, 0.40)

        self.calculate_button_2c = MyImageButton(self.frame2c.frame, GrayScale(20),
                                                 CreateTkImage('data/images/calculator.png', 48, 48),
                                                 self.calculate_2c, 0.75, 0.25)
        self.calculate_button_2c.button.configure(bg=GrayScale(20), activebackground=GrayScale(20))
        self.calculate_button_2c.button.place(relwidth=0.10, relheight=0.10)

        if tooltips:
            CreateToolTip(self.frame2c_entry1.label, 'I = ½ MR²')
            CreateToolTip(self.frame2c_entry2.label, 'RKE = ½ Iw²')

    def create_frame3a(self):
        self.frame3a_entry1 = MyOutputEntry(self.frame3a.frame, 'Moment of Inertia (kgm²)', 0.20, 0.25)

        self.calculate_button_3a = MyImageButton(self.frame3a.frame, GrayScale(20),
                                                 CreateTkImage('data/images/calculator.png', 48, 48),
                                                 self.calculate_3a, 0.75, 0.25)
        self.calculate_button_3a.button.configure(bg=GrayScale(20), activebackground=GrayScale(20))
        self.calculate_button_3a.button.place(relwidth=0.10, relheight=0.10)

        if tooltips:
            CreateToolTip(self.frame3a_entry1.label, 'I = ½ MR²')

    def create_frame3b(self):
        self.frame3b_entry1 = MyOutputEntry(self.frame3b.frame, 'Moment of Inertia (kgm²)', 0.20, 0.25)
        self.frame3b_entry2 = MyOutputEntry(self.frame3b.frame, 'Angular Momentum (kgm²/s)', 0.20, 0.40)
        self.frame3b_entry3 = MyOutputEntry(self.frame3b.frame, 'Linear Momentum (kgm/s)', 0.20, 0.55)

        self.calculate_button_3b = MyImageButton(self.frame3b.frame, GrayScale(20),
                                                 CreateTkImage('data/images/calculator.png', 48, 48),
                                                 self.calculate_3b, 0.75, 0.25)
        self.calculate_button_3b.button.configure(bg=GrayScale(20), activebackground=GrayScale(20))
        self.calculate_button_3b.button.place(relwidth=0.10, relheight=0.10)

        if tooltips:
            CreateToolTip(self.frame3b_entry1.label, 'I = ½ MR²')
            CreateToolTip(self.frame3b_entry2.label, 'L = Iw')
            CreateToolTip(self.frame3b_entry3.label, 'p = MV')

    def create_frame3c(self):
        self.frame3c_entry1 = MyOutputEntry(self.frame3c.frame, 'Moment of Inertia (kgm²)', 0.20, 0.25)
        self.frame3c_entry2 = MyOutputEntry(self.frame3c.frame, 'Rotational Kinetic Energy (J)', 0.20, 0.40)
        self.frame3c_entry3 = MyOutputEntry(self.frame3c.frame, 'Linear Kinetic Energy (J)', 0.20, 0.55)
        self.frame3c_entry4 = MyOutputEntry(self.frame3c.frame, 'Total Kinetic Energy (J)', 0.20, 0.70)

        self.calculate_button_3c = MyImageButton(self.frame3c.frame, GrayScale(20),
                                                 CreateTkImage('data/images/calculator.png', 48, 48),
                                                 self.calculate_3c, 0.75, 0.25)
        self.calculate_button_3c.button.configure(bg=GrayScale(20), activebackground=GrayScale(20))
        self.calculate_button_3c.button.place(relwidth=0.10, relheight=0.10)

        if tooltips:
            CreateToolTip(self.frame3c_entry1.label, 'I = ½ MR²')
            CreateToolTip(self.frame3c_entry2.label, 'RKE = ½ Iw²')
            CreateToolTip(self.frame3c_entry3.label, 'LKE = ½ MV²')
            CreateToolTip(self.frame3c_entry4.label, 'TKE = RKE + LKE')

    def flip_main_pf1(self):
        self.main_pf1.frame.tkraise()
        self.flip_frame1()
        self.parent.geometry(
            main_geometry + '+' + str(self.parent.winfo_screenwidth() / 2 - main_width / 2) + '+' + str(
                self.parent.winfo_screenheight() / 2 - main_height / 2))

        self.in_animation_settings = False

    def flip_main_pf2(self):
        if self.fr0:
            self.create_animation_frame()
            self.fr0 = False

        self.main_pf2.frame.tkraise()
        self.parent.geometry(
            start_geometry + '+' + str(self.parent.winfo_screenwidth() / 2 - start_width / 2) + '+' + str(
                self.parent.winfo_screenheight() / 2 - start_height / 2))

        self.in_animation_settings = True

    def flip_frame1(self):
        self.frame1.frame.tkraise()
        self.frame1a.frame.tkraise()
        self.scales.frame.tkraise()

    def flip_frame2(self):
        self.frame2.frame.tkraise()
        self.frame2a.frame.tkraise()
        self.scales.frame.tkraise()

    def flip_frame3(self):
        self.frame3.frame.tkraise()
        self.frame3a.frame.tkraise()
        self.scales.frame.tkraise()

    def calculate_1a(self):
        var1 = self.radius_scale.scale.get()
        var2 = self.mass_scale.scale.get()
        ans1 = Moment_Inertia(particle_constant, var1, var2)
        self.frame1a_entry1.entry.delete(0, END)
        self.frame1a_entry1.entry.insert(0, round(ans1, 2))

    # calculate 1b
    def calculate_1b(self):
        var1 = self.radius_scale.scale.get()
        var2 = self.mass_scale.scale.get()
        var3 = self.ang_vel_scale.scale.get()
        ans1 = Moment_Inertia(particle_constant, var1, var2)
        ans2 = Angular_Momentum(ans1, var3)
        self.frame1b_entry1.entry.delete(0, END)
        self.frame1b_entry1.entry.insert(0, round(ans1, 2))
        self.frame1b_entry2.entry.delete(0, END)
        self.frame1b_entry2.entry.insert(0, round(ans2, 2))

    # calculate 1c
    def calculate_1c(self):
        var1 = self.radius_scale.scale.get()
        var2 = self.mass_scale.scale.get()
        var3 = self.ang_vel_scale.scale.get()
        ans1 = Moment_Inertia(particle_constant, var1, var2)
        ans2 = Rotational_Kinetic_Energy(ans1, var3)
        self.frame1c_entry1.entry.delete(0, END)
        self.frame1c_entry1.entry.insert(0, round(ans1, 2))
        self.frame1c_entry2.entry.delete(0, END)
        self.frame1c_entry2.entry.insert(0, round(ans2, 2))

    # calculate 2a
    def calculate_2a(self):
        var1 = self.radius_scale.scale.get()
        var2 = self.mass_scale.scale.get()
        ans1 = Moment_Inertia(circle_constant, var1, var2)
        self.frame2a_entry1.entry.delete(0, END)
        self.frame2a_entry1.entry.insert(0, round(ans1, 2))

    # calculate 2b
    def calculate_2b(self):
        var1 = self.radius_scale.scale.get()
        var2 = self.mass_scale.scale.get()
        var3 = self.ang_vel_scale.scale.get()
        ans1 = Moment_Inertia(circle_constant, var1, var2)
        ans2 = Angular_Momentum(ans1, var3)
        self.frame2b_entry1.entry.delete(0, END)
        self.frame2b_entry1.entry.insert(0, round(ans1, 2))
        self.frame2b_entry2.entry.delete(0, END)
        self.frame2b_entry2.entry.insert(0, round(ans2, 2))

    # calculate 2c
    def calculate_2c(self):
        var1 = self.radius_scale.scale.get()
        var2 = self.mass_scale.scale.get()
        var3 = self.ang_vel_scale.scale.get()
        ans1 = Moment_Inertia(circle_constant, var1, var2)
        ans2 = Rotational_Kinetic_Energy(ans1, var3)
        self.frame2c_entry1.entry.delete(0, END)
        self.frame2c_entry1.entry.insert(0, round(ans1, 2))
        self.frame2c_entry2.entry.delete(0, END)
        self.frame2c_entry2.entry.insert(0, round(ans2, 2))

    # calculate 3a
    def calculate_3a(self):
        var1 = self.radius_scale.scale.get()
        var2 = self.mass_scale.scale.get()
        ans1 = Moment_Inertia(circle_constant, var1, var2)
        self.frame3a_entry1.entry.delete(0, END)
        self.frame3a_entry1.entry.insert(0, round(ans1, 2))

    # calculate 3b
    def calculate_3b(self):
        var1 = self.radius_scale.scale.get()
        var2 = self.mass_scale.scale.get()
        var3 = self.ang_vel_scale.scale.get()
        var4 = atl(var3, var1)
        ans1 = Moment_Inertia(circle_constant, var1, var2)
        ans2 = Angular_Momentum(ans1, var3)
        ans3 = Linear_Momentum(var2, var4)
        self.frame3b_entry1.entry.delete(0, END)
        self.frame3b_entry1.entry.insert(0, round(ans1, 2))
        self.frame3b_entry2.entry.delete(0, END)
        self.frame3b_entry2.entry.insert(0, round(ans2, 2))
        self.frame3b_entry3.entry.delete(0, END)
        self.frame3b_entry3.entry.insert(0, round(ans3, 2))

    # calculate 3c
    def calculate_3c(self):
        var1 = self.radius_scale.scale.get()
        var2 = self.mass_scale.scale.get()
        var3 = self.ang_vel_scale.scale.get()
        var4 = atl(var3, var1)
        ans1 = Moment_Inertia(circle_constant, var1, var2)
        ans2 = Rotational_Kinetic_Energy(ans1, var3)
        ans3 = Linear_Kinetic_Energy(var2, var4)
        ans4 = TKE(ans2, ans3)
        self.frame3c_entry1.entry.delete(0, END)
        self.frame3c_entry1.entry.insert(0, round(ans1, 2))
        self.frame3c_entry2.entry.delete(0, END)
        self.frame3c_entry2.entry.insert(0, round(ans2, 2))
        self.frame3c_entry3.entry.delete(0, END)
        self.frame3c_entry3.entry.insert(0, round(ans3, 2))
        self.frame3c_entry4.entry.delete(0, END)
        self.frame3c_entry4.entry.insert(0, round(ans4, 2))

    # animate orbiting particle
    def animate1(self):
        orbiting_particle_animation(self.parent,
                                    self.frame1_canvas.canvas,
                                    float(canvas_width) / 2.0,
                                    float(canvas_height) / 2.0,
                                    float(self.radius_scale.scale.get()) * float(self.len_mult_scale.scale.get()),
                                    float(self.ang_vel_scale.scale.get()) / float(self.time_factor_scale.scale.get()),
                                    self.granularity_scale.scale.get()
                                    )

    # animate rotating circle
    def animate2(self):
        rotating_circle_animation(self.parent,
                                  self.frame2_canvas.canvas,
                                  float(canvas_width) / 2.0,
                                  float(canvas_height) / 2.0,
                                  float(self.radius_scale.scale.get()) * float(self.len_mult_scale.scale.get()),
                                  float(self.ang_vel_scale.scale.get()) / float(
                                      self.time_factor_scale.scale.get()),
                                  self.granularity_scale.scale.get()
                                  )

    # animate rolling circle
    def animate3(self):
        rolling_circle_animation(self.parent,
                                 self.frame3_canvas.canvas,
                                 float(canvas_width) / 2.0,
                                 float(canvas_height) / 2.0,
                                 float(self.radius_scale.scale.get()) * float(self.len_mult_scale.scale.get()),
                                 float(self.ang_vel_scale.scale.get()) / float(self.time_factor_scale.scale.get()),
                                 self.granularity_scale.scale.get()
                                 )
