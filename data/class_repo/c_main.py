# main component class

# imports
from Tkinter import END
from c_other import MyFrame, MyFrameWBP, MyCanvas, MyLabel, MyScale, MyEntry, MyButton
from data.myfunctions import \
    atl, Moment_Inertia, Angular_Momentum, Linear_Momentum, \
    Rotational_Kinetic_Energy, Linear_Kinetic_Energy, TKE, \
    orbiting_particle_animation, rotating_circle_animation, rolling_circle_animation
from data.variables import \
    dev, colors, frame_bottom_pad1, frame_bottom_pad2, \
    fb_rely_primary, fb_rely_secondary, canvas_width, canvas_height, \
    particle_constant, circle_constant


class MyMainFrame(object):
    def __init__(self, parent):
        # assigning parameters to attributes
        self.parent = parent

        # creating first run variables
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

        # creating frames, navigation buttons and animation frame
        self.create_frames()
        self.create_nav()
        self.create_animation_frame()

        # select frames (main_pf1, frame1, frame1a)
        self.flip_main_pf1()
        self.flip_frame1()

    def create_frames(self):
        if dev:
            print '[main] frames created'

        self.main_bf = MyFrame(self.parent, colors[4])
        self.main_pf1 = MyFrame(self.main_bf.frame, colors[4])
        self.main_pf2 = MyFrame(self.main_bf.frame, colors[4])
        self.frame1 = MyFrameWBP(self.main_bf.frame, colors[4], frame_bottom_pad1)
        self.frame2 = MyFrameWBP(self.main_bf.frame, colors[4], frame_bottom_pad1)
        self.frame3 = MyFrameWBP(self.main_bf.frame, colors[4], frame_bottom_pad1)
        self.frame1a = MyFrameWBP(self.frame1.frame, colors[3], frame_bottom_pad2)
        self.frame1b = MyFrameWBP(self.frame1.frame, colors[3], frame_bottom_pad2)
        self.frame1c = MyFrameWBP(self.frame1.frame, colors[3], frame_bottom_pad2)
        self.frame2a = MyFrameWBP(self.frame2.frame, colors[3], frame_bottom_pad2)
        self.frame2b = MyFrameWBP(self.frame2.frame, colors[3], frame_bottom_pad2)
        self.frame2c = MyFrameWBP(self.frame2.frame, colors[3], frame_bottom_pad2)
        self.frame3a = MyFrameWBP(self.frame3.frame, colors[3], frame_bottom_pad2)
        self.frame3b = MyFrameWBP(self.frame3.frame, colors[3], frame_bottom_pad2)
        self.frame3c = MyFrameWBP(self.frame3.frame, colors[3], frame_bottom_pad2)

    def create_nav(self):
        if dev:
            print '[main] navigation buttons created'

        self.enter_as = MyButton(self.main_pf1.frame, 'Animation Settings', self.flip_main_pf2, 0.05, fb_rely_primary)
        self.exit_as = MyButton(self.main_pf2.frame, 'Exit', self.flip_main_pf1, 0.05, fb_rely_primary)
        self.fb1 = MyButton(self.main_pf1.frame, 'Orbiting Particle', self.flip_frame1, 0.55, fb_rely_primary)
        self.fb2 = MyButton(self.main_pf1.frame, 'Rotating Circle', self.flip_frame2, 0.70, fb_rely_primary)
        self.fb3 = MyButton(self.main_pf1.frame, 'Rolling Circle', self.flip_frame3, 0.85, fb_rely_primary)
        self.fb1a = MyButton(self.frame1.frame, 'Basic', self.flip_frame1a, 0.55, fb_rely_secondary)
        self.fb1b = MyButton(self.frame1.frame, 'Momentum', self.flip_frame1b, 0.70, fb_rely_secondary)
        self.fb1c = MyButton(self.frame1.frame, 'Energy', self.flip_frame1c, 0.85, fb_rely_secondary)
        self.fb2a = MyButton(self.frame2.frame, 'Basic', self.flip_frame2a, 0.55, fb_rely_secondary)
        self.fb2b = MyButton(self.frame2.frame, 'Momentum', self.flip_frame2b, 0.70, fb_rely_secondary)
        self.fb2c = MyButton(self.frame2.frame, 'Energy', self.flip_frame2c, 0.85, fb_rely_secondary)
        self.fb3a = MyButton(self.frame3.frame, 'Basic', self.flip_frame3a, 0.55, fb_rely_secondary)
        self.fb3b = MyButton(self.frame3.frame, 'Momentum', self.flip_frame3b, 0.70, fb_rely_secondary)
        self.fb3c = MyButton(self.frame3.frame, 'Energy', self.flip_frame3c, 0.85, fb_rely_secondary)

    def create_animation_frame(self):
        if dev:
            print '[main] animation frame objects created'

        self.main_pf2_title = MyLabel(self.main_pf2.frame, 'Animation Settings', 0.05, 0.05)
        self.main_pf2_title.label.configure(bg=colors[4])

        self.time_factor_scale = MyScale(self.main_pf2.frame, 'Time Factor', 0.05, 0.15)
        self.len_mult_scale = MyScale(self.main_pf2.frame, 'Length Multiplier', 0.05, 0.30)
        self.granularity_scale = MyScale(self.main_pf2.frame, 'Granularity', 0.05, 0.45)

        self.time_factor_scale.scale.configure(from_=1, to=100, resolution=1, bg=colors[4])
        self.len_mult_scale.scale.configure(from_=1, to=100, resolution=1, bg=colors[4])
        self.granularity_scale.scale.configure(from_=5, to=90, resolution=5, bg=colors[4])

        self.time_factor_scale.label.configure(bg=colors[4])
        self.len_mult_scale.label.configure(bg=colors[4])
        self.granularity_scale.label.configure(bg=colors[4])

        self.time_factor_scale.scale.set(5)
        self.len_mult_scale.scale.set(10)
        self.granularity_scale.scale.set(15)

    def create_frame1a(self):
        if dev:
            print '[main] frame1a objects created'

        self.main_label_1a = MyLabel(self.frame1a.frame, 'Orbiting Particle Basics', 0.05, 0.05)
        self.calculate_button_1a = MyButton(self.frame1a.frame, 'Calculate', self.calculate_1a, 0.70, 0.90)
        self.animate_button_1a = MyButton(self.frame1a.frame, 'Animate', self.animate_1a, 0.85, 0.90)
        self.frame1a_scale1 = MyScale(self.frame1a.frame, 'Radius (m)', 0.05, 0.20)
        self.frame1a_scale2 = MyScale(self.frame1a.frame, 'Mass (kg)', 0.05, 0.35)
        self.frame1a_scale3 = MyScale(self.frame1a.frame, 'Angular Velocity (rad/s)', 0.05, 0.50)
        self.frame1a_entry1 = MyEntry(self.frame1a.frame, 'Moment of Inertia (kgm^2)', 0.85, 0.20)
        self.frame1a_canvas1 = MyCanvas(self.frame1a.frame)

    def create_frame1b(self):
        if dev:
            print '[main] frame1b objects created'

        self.main_label_1b = MyLabel(self.frame1b.frame, 'Orbiting Particle Momentum', 0.05, 0.05)
        self.calculate_button_1b = MyButton(self.frame1b.frame, 'Calculate', self.calculate_1b, 0.70, 0.90)
        self.animate_button_1b = MyButton(self.frame1b.frame, 'Animate', self.animate_1b, 0.85, 0.90)
        self.frame1b_scale1 = MyScale(self.frame1b.frame, 'Radius (m)', 0.05, 0.20)
        self.frame1b_scale2 = MyScale(self.frame1b.frame, 'Mass (kg)', 0.05, 0.35)
        self.frame1b_scale3 = MyScale(self.frame1b.frame, 'Angular Velocity (rad/s)', 0.05, 0.50)
        self.frame1b_entry1 = MyEntry(self.frame1b.frame, 'Moment of Inertia (kgm^2)', 0.85, 0.20)
        self.frame1b_entry2 = MyEntry(self.frame1b.frame, 'Angular Momentum (kgm^2/s)', 0.85, 0.35)
        self.frame1b_canvas1 = MyCanvas(self.frame1b.frame)

    def create_frame1c(self):
        if dev:
            print '[main] frame1c objects created'

        self.main_label_1c = MyLabel(self.frame1c.frame, 'Orbiting Particle Energy', 0.05, 0.05)
        self.calculate_button_1c = MyButton(self.frame1c.frame, 'Calculate', self.calculate_1c, 0.70, 0.90)
        self.animate_button_1c = MyButton(self.frame1c.frame, 'Animate', self.animate_1c, 0.85, 0.90)
        self.frame1c_scale1 = MyScale(self.frame1c.frame, 'Radius (m)', 0.05, 0.20)
        self.frame1c_scale2 = MyScale(self.frame1c.frame, 'Mass (kg)', 0.05, 0.35)
        self.frame1c_scale3 = MyScale(self.frame1c.frame, 'Angular Velocity (rad/s)', 0.05, 0.50)
        self.frame1c_entry1 = MyEntry(self.frame1c.frame, 'Moment of Inertia (kgm^2)', 0.85, 0.20)
        self.frame1c_entry2 = MyEntry(self.frame1c.frame, 'Rotational Kinetic Energy (J)', 0.85, 0.35)
        self.frame1c_canvas1 = MyCanvas(self.frame1c.frame)

    def create_frame2a(self):
        if dev:
            print '[main] frame2a objects created'

        self.main_label_2a = MyLabel(self.frame2a.frame, 'Rotating Circle Basics', 0.05, 0.05)
        self.calculate_button_2a = MyButton(self.frame2a.frame, 'Calculate', self.calculate_2a, 0.70, 0.90)
        self.animate_button_2a = MyButton(self.frame2a.frame, 'Animate', self.animate_2a, 0.85, 0.90)
        self.frame2a_scale1 = MyScale(self.frame2a.frame, 'Radius (m)', 0.05, 0.20)
        self.frame2a_scale2 = MyScale(self.frame2a.frame, 'Mass (kg)', 0.05, 0.35)
        self.frame2a_scale3 = MyScale(self.frame2a.frame, 'Angular Velocity (rad/s)', 0.05, 0.50)
        self.frame2a_entry1 = MyEntry(self.frame2a.frame, 'Moment of Inertia (kgm^2)', 0.85, 0.20)
        self.frame2a_canvas1 = MyCanvas(self.frame2a.frame)

    def create_frame2b(self):
        if dev:
            print '[main] frame2b objects created'

        self.main_label_2b = MyLabel(self.frame2b.frame, 'Rotating Circle Momentum', 0.05, 0.05)
        self.calculate_button_2b = MyButton(self.frame2b.frame, 'Calculate', self.calculate_2b, 0.70, 0.90)
        self.animate_button_2b = MyButton(self.frame2b.frame, 'Animate', self.animate_2b, 0.85, 0.90)
        self.frame2b_scale1 = MyScale(self.frame2b.frame, 'Radius (m)', 0.05, 0.20)
        self.frame2b_scale2 = MyScale(self.frame2b.frame, 'Mass (kg)', 0.05, 0.35)
        self.frame2b_scale3 = MyScale(self.frame2b.frame, 'Angular Velocity (rad/s)', 0.05, 0.50)
        self.frame2b_entry1 = MyEntry(self.frame2b.frame, 'Moment of Inertia (kgm^2)', 0.85, 0.20)
        self.frame2b_entry2 = MyEntry(self.frame2b.frame, 'Angular Momentum (kgm^2/s)', 0.85, 0.35)
        self.frame2b_canvas1 = MyCanvas(self.frame2b.frame)

    def create_frame2c(self):
        if dev:
            print '[main] frame2c objects created'

        self.main_label_2c = MyLabel(self.frame2c.frame, 'Rotating Circle Energy', 0.05, 0.05)
        self.calculate_button_2c = MyButton(self.frame2c.frame, 'Calculate', self.calculate_2c, 0.70, 0.90)
        self.animate_button_2c = MyButton(self.frame2c.frame, 'Animate', self.animate_2c, 0.85, 0.90)
        self.frame2c_scale1 = MyScale(self.frame2c.frame, 'Radius (m)', 0.05, 0.20)
        self.frame2c_scale2 = MyScale(self.frame2c.frame, 'Mass (kg)', 0.05, 0.35)
        self.frame2c_scale3 = MyScale(self.frame2c.frame, 'Angular Velocity (rad/s)', 0.05, 0.50)
        self.frame2c_entry1 = MyEntry(self.frame2c.frame, 'Moment of Inertia (kgm^2)', 0.85, 0.20)
        self.frame2c_entry2 = MyEntry(self.frame2c.frame, 'Rotational Kinetic Energy (J)', 0.85, 0.35)
        self.frame2c_canvas1 = MyCanvas(self.frame2c.frame)

    def create_frame3a(self):
        if dev:
            print '[main] frame3a objects created'

        self.main_label_3a = MyLabel(self.frame3a.frame, 'Rolling Circle Basics', 0.05, 0.05)
        self.calculate_button_3a = MyButton(self.frame3a.frame, 'Calculate', self.calculate_3a, 0.70, 0.90)
        self.animate_button_3a = MyButton(self.frame3a.frame, 'Animate', self.animate_3a, 0.85, 0.90)
        self.frame3a_scale1 = MyScale(self.frame3a.frame, 'Radius (m)', 0.05, 0.20)
        self.frame3a_scale2 = MyScale(self.frame3a.frame, 'Mass (kg)', 0.05, 0.35)
        self.frame3a_scale3 = MyScale(self.frame3a.frame, 'Angular Velocity (rad/s)', 0.05, 0.50)
        self.frame3a_entry1 = MyEntry(self.frame3a.frame, 'Moment of Inertia (kgm^2)', 0.85, 0.20)
        self.frame3a_canvas1 = MyCanvas(self.frame3a.frame)

    def create_frame3b(self):
        if dev:
            print '[main] frame3b objects created'

        self.main_label_3b = MyLabel(self.frame3b.frame, 'Rolling Circle Momentum', 0.05, 0.05)
        self.calculate_button_3b = MyButton(self.frame3b.frame, 'Calculate', self.calculate_3b, 0.70, 0.90)
        self.animate_button_3b = MyButton(self.frame3b.frame, 'Animate', self.animate_3b, 0.85, 0.90)
        self.frame3b_scale1 = MyScale(self.frame3b.frame, 'Radius (m)', 0.05, 0.20)
        self.frame3b_scale2 = MyScale(self.frame3b.frame, 'Mass (kg)', 0.05, 0.35)
        self.frame3b_scale3 = MyScale(self.frame3b.frame, 'Angular Velocity (rad/s)', 0.05, 0.50)
        self.frame3b_entry1 = MyEntry(self.frame3b.frame, 'Moment of Inertia (kgm^2)', 0.85, 0.20)
        self.frame3b_entry2 = MyEntry(self.frame3b.frame, 'Angular Momentum (kgm^2/s)', 0.85, 0.35)
        self.frame3b_entry3 = MyEntry(self.frame3b.frame, 'Linear Momentum (kgm/s)', 0.85, 0.50)
        self.frame3b_canvas1 = MyCanvas(self.frame3b.frame)

    def create_frame3c(self):
        if dev:
            print '[main] frame3c objects created'

        self.main_label_3c = MyLabel(self.frame3c.frame, 'Rolling Circle Energy', 0.05, 0.05)
        self.calculate_button_3c = MyButton(self.frame3c.frame, 'Calculate', self.calculate_3c, 0.70, 0.90)
        self.animate_button_3c = MyButton(self.frame3c.frame, 'Animate', self.animate_3c, 0.85, 0.90)
        self.frame3c_scale1 = MyScale(self.frame3c.frame, 'Radius (m)', 0.05, 0.2)
        self.frame3c_scale2 = MyScale(self.frame3c.frame, 'Mass (kg)', 0.05, 0.35)
        self.frame3c_scale3 = MyScale(self.frame3c.frame, 'Angular Velocity (rad/s)', 0.05, 0.50)
        self.frame3c_entry1 = MyEntry(self.frame3c.frame, 'Moment of Inertia (kgm^2)', 0.85, 0.20)
        self.frame3c_entry2 = MyEntry(self.frame3c.frame, 'Rotational Kinetic Energy (J)', 0.85, 0.35)
        self.frame3c_entry3 = MyEntry(self.frame3c.frame, 'Linear Kinetic Energy (J)', 0.85, 0.50)
        self.frame3c_entry4 = MyEntry(self.frame3c.frame, 'Total Kinetic Energy (J)', 0.85, 0.65)
        self.frame3c_canvas1 = MyCanvas(self.frame3c.frame)

    def flip_main_pf1(self):
        self.main_pf1.frame.tkraise()
        self.flip_frame1()

    def flip_main_pf2(self):
        if self.fr0:
            self.create_animation_frame()
            self.fr0 = False

        self.main_pf2.frame.tkraise()

    def flip_frame1(self):
        self.frame1.frame.tkraise()
        self.flip_frame1a()

    def flip_frame2(self):
        self.frame2.frame.tkraise()
        self.flip_frame2a()

    def flip_frame3(self):
        self.frame3.frame.tkraise()
        self.flip_frame3a()

    def flip_frame1a(self):
        if self.fr1:
            self.create_frame1a()
            self.fr1 = False

        self.frame1a.frame.tkraise()

    def flip_frame1b(self):
        if self.fr2:
            self.create_frame1b()
            self.fr2 = False

        self.frame1b.frame.tkraise()

    def flip_frame1c(self):
        if self.fr3:
            self.create_frame1c()
            self.fr3 = False

        self.frame1c.frame.tkraise()

    def flip_frame2a(self):
        if self.fr4:
            self.create_frame2a()
            self.fr4 = False

        self.frame2a.frame.tkraise()

    def flip_frame2b(self):
        if self.fr5:
            self.create_frame2b()
            self.fr5 = False

        self.frame2b.frame.tkraise()

    def flip_frame2c(self):
        if self.fr6:
            self.create_frame2c()
            self.fr6 = False

        self.frame2c.frame.tkraise()

    def flip_frame3a(self):
        if self.fr7:
            self.create_frame3a()
            self.fr7 = False

        self.frame3a.frame.tkraise()

    def flip_frame3b(self):
        if self.fr8:
            self.create_frame3b()
            self.fr8 = False

        self.frame3b.frame.tkraise()

    def flip_frame3c(self):
        if self.fr9:
            self.create_frame3c()
            self.fr9 = False

        self.frame3c.frame.tkraise()

    def calculate_1a(self):
        var1 = self.frame1a_scale1.scale.get()
        var2 = self.frame1a_scale2.scale.get()
        ans1 = Moment_Inertia(particle_constant, var1, var2)
        self.frame1a_entry1.entry.delete(0, END)
        self.frame1a_entry1.entry.insert(0, round(ans1, 2))

    # calculate 1b
    def calculate_1b(self):
        var1 = self.frame1b_scale1.scale.get()
        var2 = self.frame1b_scale2.scale.get()
        var3 = self.frame1b_scale3.scale.get()
        ans1 = Moment_Inertia(particle_constant, var1, var2)
        ans2 = Angular_Momentum(ans1, var3)
        self.frame1b_entry1.entry.delete(0, END)
        self.frame1b_entry1.entry.insert(0, round(ans1, 2))
        self.frame1b_entry2.entry.delete(0, END)
        self.frame1b_entry2.entry.insert(0, round(ans2, 2))

    # calculate 1c
    def calculate_1c(self):
        var1 = self.frame1c_scale1.scale.get()
        var2 = self.frame1c_scale2.scale.get()
        var3 = self.frame1c_scale3.scale.get()
        ans1 = Moment_Inertia(particle_constant, var1, var2)
        ans2 = Rotational_Kinetic_Energy(ans1, var3)
        self.frame1c_entry1.entry.delete(0, END)
        self.frame1c_entry1.entry.insert(0, round(ans1, 2))
        self.frame1c_entry2.entry.delete(0, END)
        self.frame1c_entry2.entry.insert(0, round(ans2, 2))

    # calculate 2a
    def calculate_2a(self):
        var1 = self.frame2a_scale1.scale.get()
        var2 = self.frame2a_scale2.scale.get()
        ans1 = Moment_Inertia(circle_constant, var1, var2)
        self.frame2a_entry1.entry.delete(0, END)
        self.frame2a_entry1.entry.insert(0, round(ans1, 2))

    # calculate 2b
    def calculate_2b(self):
        var1 = self.frame2b_scale1.scale.get()
        var2 = self.frame2b_scale2.scale.get()
        var3 = self.frame2b_scale3.scale.get()
        ans1 = Moment_Inertia(circle_constant, var1, var2)
        ans2 = Angular_Momentum(ans1, var3)
        self.frame2b_entry1.entry.delete(0, END)
        self.frame2b_entry1.entry.insert(0, round(ans1, 2))
        self.frame2b_entry2.entry.delete(0, END)
        self.frame2b_entry2.entry.insert(0, round(ans2, 2))

    # calculate 2c
    def calculate_2c(self):
        var1 = self.frame2c_scale1.scale.get()
        var2 = self.frame2c_scale2.scale.get()
        var3 = self.frame2c_scale3.scale.get()
        ans1 = Moment_Inertia(circle_constant, var1, var2)
        ans2 = Rotational_Kinetic_Energy(ans1, var3)
        self.frame2c_entry1.entry.delete(0, END)
        self.frame2c_entry1.entry.insert(0, round(ans1, 2))
        self.frame2c_entry2.entry.delete(0, END)
        self.frame2c_entry2.entry.insert(0, round(ans2, 2))

    # calculate 3a
    def calculate_3a(self):
        var1 = self.frame3a_scale1.scale.get()
        var2 = self.frame3a_scale2.scale.get()
        ans1 = Moment_Inertia(circle_constant, var1, var2)
        self.frame3a_entry1.entry.delete(0, END)
        self.frame3a_entry1.entry.insert(0, round(ans1, 2))

    # calculate 3b
    def calculate_3b(self):
        var1 = self.frame3b_scale1.scale.get()
        var2 = self.frame3b_scale2.scale.get()
        var3 = self.frame3b_scale3.scale.get()
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
        var1 = self.frame3c_scale1.scale.get()
        var2 = self.frame3c_scale2.scale.get()
        var3 = self.frame3c_scale3.scale.get()
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
    def animate_orbiting_particle(self, canvas, radius, ang_vel):
        orbiting_particle_animation(self.parent,
                                    canvas,
                                    float(canvas_width) / 2.0,
                                    float(canvas_height) / 2.0,
                                    float(radius.get()) * float(self.len_mult_scale.scale.get()),
                                    float(ang_vel.get()) / float(self.time_factor_scale.scale.get()),
                                    self.granularity_scale.scale.get()
                                    )

    # animate 1a
    def animate_1a(self):
        self.animate_orbiting_particle(self.frame1a_canvas1.canvas,
                                       self.frame1a_scale1.scale,
                                       self.frame1a_scale3.scale
                                       )

    # animate 1b
    def animate_1b(self):
        self.animate_orbiting_particle(self.frame1b_canvas1.canvas,
                                       self.frame1b_scale1.scale,
                                       self.frame1b_scale3.scale
                                       )

    # animate 1c
    def animate_1c(self):
        self.animate_orbiting_particle(self.frame1c_canvas1.canvas,
                                       self.frame1c_scale1.scale,
                                       self.frame1c_scale3.scale
                                       )

    # animate rotating circle
    def animate_rotating_circle(self, canvas, radius, ang_vel):
        rotating_circle_animation(self.parent,
                                  canvas,
                                  float(canvas_width) / 2.0,
                                  float(canvas_height) / 2.0,
                                  float(radius.get()) * float(self.len_mult_scale.scale.get()),
                                  float(ang_vel.get()) / float(self.time_factor_scale.scale.get()),
                                  self.granularity_scale.scale.get()
                                  )

    # animate 2a
    def animate_2a(self):
        self.animate_rotating_circle(self.frame2a_canvas1.canvas,
                                     self.frame2a_scale1.scale,
                                     self.frame2a_scale3.scale
                                     )

    # animate 2b
    def animate_2b(self):
        self.animate_rotating_circle(self.frame2b_canvas1.canvas,
                                     self.frame2b_scale1.scale,
                                     self.frame2b_scale3.scale
                                     )

    # animate 2c
    def animate_2c(self):
        self.animate_rotating_circle(self.frame2c_canvas1.canvas,
                                     self.frame2c_scale1.scale,
                                     self.frame2c_scale3.scale
                                     )

    def animate_rolling_circle(self, canvas, radius, ang_vel):
        rolling_circle_animation(self.parent,
                                 canvas,
                                 float(canvas_width) / 2.0,
                                 float(canvas_height) / 2.0,
                                 float(radius.get()) * float(self.len_mult_scale.scale.get()),
                                 float(ang_vel.get()) / float(self.time_factor_scale.scale.get()),
                                 self.granularity_scale.scale.get()
                                 )

    def animate_3a(self):
        self.animate_rolling_circle(self.frame3a_canvas1.canvas,
                                    self.frame3a_scale1.scale,
                                    self.frame3a_scale3.scale
                                    )

    def animate_3b(self):
        self.animate_rolling_circle(self.frame3b_canvas1.canvas,
                                    self.frame3b_scale1.scale,
                                    self.frame3b_scale3.scale
                                    )

    def animate_3c(self):
        self.animate_rolling_circle(self.frame3c_canvas1.canvas,
                                    self.frame3c_scale1.scale,
                                    self.frame3c_scale3.scale
                                    )
