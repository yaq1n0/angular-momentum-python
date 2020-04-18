# main file

# imports
from Tkinter import *
from os import execv
from sys import executable, argv
from myclasses import MyButton, MyCanvas, MyEntry, MyFrame, MyFrameWBP, MyLabel, MyScale
from func1 import Moment_Inertia
from func1 import Angular_Momentum, Linear_Momentum
from func1 import Rotational_Kinetic_Energy, Linear_Kinetic_Energy, TKE
from func1 import atl
from func2 import orbiting_particle_animation, rotating_circle_animation, rolling_circle_animation
from myvars import colors
from myvars import start_geometry, main_geometry, game_geometry, cheatsheet_geometry, documentation_geometry
from myvars import cheatsheet_width, cheatsheet_height
from myvars import documentation_width, documentation_height
from myvars import frame_bottom_pad1, frame_bottom_pad2, fb_rely_primary, fb_rely_secondary
from myvars import canvas_width, canvas_height
from myvars import particle_constant, circle_constant
from game import run_game
from images import run_cheatsheet, run_documentation

# space to test code

print ''

# creating root
root = Tk()
root.title('Rotational Motion')
root.geometry(start_geometry)
root.resizable(False, False)
root.configure(bg=colors[4])

# base frames
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


# goto functions
def goto_start():
    root.geometry(start_geometry)
    root.title('Rotational Motion')
    start_bf.frame.tkraise()


def goto_main():
    root.geometry(main_geometry)
    root.title('Rotational Motion')
    main_bf.frame.tkraise()


def goto_game():
    root.geometry(game_geometry)
    root.title('Quiz Game')
    run_game(game_bf.frame)
    game_bf.frame.tkraise()


def goto_cheatsheet():
    root.geometry(cheatsheet_geometry)
    root.title('CheatSheet')
    run_cheatsheet(cheatsheet_bf.frame)
    cheatsheet_bf.frame.tkraise()


def goto_documentation():
    root.geometry(documentation_geometry)
    root.title('Documentation')
    run_documentation(documentation_bf.frame)
    documentation_bf.frame.tkraise()


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

# main_bf objects

# creating frames
main_pf1 = MyFrame(main_bf.frame, colors[4])
main_pf2 = MyFrame(main_bf.frame, colors[4])
frame1 = MyFrameWBP(main_bf.frame, colors[4], frame_bottom_pad1)
frame2 = MyFrameWBP(main_bf.frame, colors[4], frame_bottom_pad1)
frame3 = MyFrameWBP(main_bf.frame, colors[4], frame_bottom_pad1)
frame1a = MyFrameWBP(frame1.frame, colors[3], frame_bottom_pad2)
frame1b = MyFrameWBP(frame1.frame, colors[3], frame_bottom_pad2)
frame1c = MyFrameWBP(frame1.frame, colors[3], frame_bottom_pad2)
frame2a = MyFrameWBP(frame2.frame, colors[3], frame_bottom_pad2)
frame2b = MyFrameWBP(frame2.frame, colors[3], frame_bottom_pad2)
frame2c = MyFrameWBP(frame2.frame, colors[3], frame_bottom_pad2)
frame3a = MyFrameWBP(frame3.frame, colors[3], frame_bottom_pad2)
frame3b = MyFrameWBP(frame3.frame, colors[3], frame_bottom_pad2)
frame3c = MyFrameWBP(frame3.frame, colors[3], frame_bottom_pad2)


# flip frame functions
def flip_main_pf1():
    main_pf1.frame.tkraise()
    frame1.frame.tkraise()
    frame1a.frame.tkraise()


def flip_main_pf2():
    main_pf2.frame.tkraise()


def flip_frame1():
    frame1.frame.tkraise()
    frame1a.frame.tkraise()


def flip_frame2():
    frame2.frame.tkraise()
    frame2a.frame.tkraise()


def flip_frame3():
    frame3.frame.tkraise()
    frame3a.frame.tkraise()


def flip_frame1a():
    frame1a.frame.tkraise()


def flip_frame1b():
    frame1b.frame.tkraise()


def flip_frame1c():
    frame1c.frame.tkraise()


def flip_frame2a():
    frame2a.frame.tkraise()


def flip_frame2b():
    frame2b.frame.tkraise()


def flip_frame2c():
    frame2c.frame.tkraise()


def flip_frame3a():
    frame3a.frame.tkraise()


def flip_frame3b():
    frame3b.frame.tkraise()


def flip_frame3c():
    frame3c.frame.tkraise()


# setting default frame order
flip_main_pf2()
flip_main_pf1()
flip_frame3()
flip_frame2()
flip_frame1()

# frame navigation buttons
enter_as = MyButton(main_pf1.frame, 'Animation Settings', flip_main_pf2, 0.05, fb_rely_primary)
exit_as = MyButton(main_pf2.frame, 'Exit', flip_main_pf1, 0.05, fb_rely_primary)
fb1 = MyButton(main_pf1.frame, 'Orbiting Particle', flip_frame1, 0.55, fb_rely_primary)
fb2 = MyButton(main_pf1.frame, 'Rotating Circle', flip_frame2, 0.70, fb_rely_primary)
fb3 = MyButton(main_pf1.frame, 'Rolling Circle', flip_frame3, 0.85, fb_rely_primary)
fb1a = MyButton(frame1.frame, 'Basic', flip_frame1a, 0.55, fb_rely_secondary)
fb1b = MyButton(frame1.frame, 'Momentum', flip_frame1b, 0.70, fb_rely_secondary)
fb1c = MyButton(frame1.frame, 'Energy', flip_frame1c, 0.85, fb_rely_secondary)
fb2a = MyButton(frame2.frame, 'Basic', flip_frame2a, 0.55, fb_rely_secondary)
fb2b = MyButton(frame2.frame, 'Momentum', flip_frame2b, 0.70, fb_rely_secondary)
fb2c = MyButton(frame2.frame, 'Energy', flip_frame2c, 0.85, fb_rely_secondary)
fb3a = MyButton(frame3.frame, 'Basic', flip_frame3a, 0.55, fb_rely_secondary)
fb3b = MyButton(frame3.frame, 'Momentum', flip_frame3b, 0.70, fb_rely_secondary)
fb3c = MyButton(frame3.frame, 'Energy', flip_frame3c, 0.85, fb_rely_secondary)


# main_pf2 (animation settings) objects
main_pf2_title = MyLabel(main_pf2.frame, 'Animation Settings', 0.05, 0.05)
main_pf2_title.label.configure(bg=colors[4])

time_factor_scale = MyScale(main_pf2.frame, 'Time Factor', 0.05, 0.15)
len_mult_scale = MyScale(main_pf2.frame, 'Length Multiplier', 0.05, 0.30)
granularity_scale = MyScale(main_pf2.frame, 'Granularity', 0.05, 0.45)

time_factor_scale.scale.configure(from_=1, to=100, resolution=1, bg=colors[4])
len_mult_scale.scale.configure(from_=1, to=100, resolution=1, bg=colors[4])
granularity_scale.scale.configure(from_=5, to=90, resolution=5, bg=colors[4])

time_factor_scale.label.configure(bg=colors[4])
len_mult_scale.label.configure(bg=colors[4])
granularity_scale.label.configure(bg=colors[4])

time_factor_scale.scale.set(5)
len_mult_scale.scale.set(10)
granularity_scale.scale.set(15)


# calculate 1a
def calculate_1a():
    var1 = frame1a_scale1.scale.get()
    var2 = frame1a_scale2.scale.get()
    ans1 = Moment_Inertia(particle_constant, var1, var2)
    frame1a_entry1.entry.delete(0, END)
    frame1a_entry1.entry.insert(0, round(ans1, 2))


# calculate 1b
def calculate_1b():
    var1 = frame1b_scale1.scale.get()
    var2 = frame1b_scale2.scale.get()
    var3 = frame1b_scale3.scale.get()
    ans1 = Moment_Inertia(particle_constant, var1, var2)
    ans2 = Angular_Momentum(ans1, var3)
    frame1b_entry1.entry.delete(0, END)
    frame1b_entry1.entry.insert(0, round(ans1, 2))
    frame1b_entry2.entry.delete(0, END)
    frame1b_entry2.entry.insert(0, round(ans2, 2))


# calculate 1c
def calculate_1c():
    var1 = frame1c_scale1.scale.get()
    var2 = frame1c_scale2.scale.get()
    var3 = frame1c_scale3.scale.get()
    ans1 = Moment_Inertia(particle_constant, var1, var2)
    ans2 = Rotational_Kinetic_Energy(ans1, var3)
    frame1c_entry1.entry.delete(0, END)
    frame1c_entry1.entry.insert(0, round(ans1, 2))
    frame1c_entry2.entry.delete(0, END)
    frame1c_entry2.entry.insert(0, round(ans2, 2))


# calculate 2a
def calculate_2a():
    var1 = frame2a_scale1.scale.get()
    var2 = frame2a_scale2.scale.get()
    ans1 = Moment_Inertia(circle_constant, var1, var2)
    frame2a_entry1.entry.delete(0, END)
    frame2a_entry1.entry.insert(0, round(ans1, 2))


# calculate 2b
def calculate_2b():
    var1 = frame2b_scale1.scale.get()
    var2 = frame2b_scale2.scale.get()
    var3 = frame2b_scale3.scale.get()
    ans1 = Moment_Inertia(circle_constant, var1, var2)
    ans2 = Angular_Momentum(ans1, var3)
    frame2b_entry1.entry.delete(0, END)
    frame2b_entry1.entry.insert(0, round(ans1, 2))
    frame2b_entry2.entry.delete(0, END)
    frame2b_entry2.entry.insert(0, round(ans2, 2))


# calculate 2c
def calculate_2c():
    var1 = frame2c_scale1.scale.get()
    var2 = frame2c_scale2.scale.get()
    var3 = frame2c_scale3.scale.get()
    ans1 = Moment_Inertia(circle_constant, var1, var2)
    ans2 = Rotational_Kinetic_Energy(ans1, var3)
    frame2c_entry1.entry.delete(0, END)
    frame2c_entry1.entry.insert(0, round(ans1, 2))
    frame2c_entry2.entry.delete(0, END)
    frame2c_entry2.entry.insert(0, round(ans2, 2))


# calculate 3a
def calculate_3a():
    var1 = frame3a_scale1.scale.get()
    var2 = frame3a_scale2.scale.get()
    ans1 = Moment_Inertia(circle_constant, var1, var2)
    frame3a_entry1.entry.delete(0, END)
    frame3a_entry1.entry.insert(0, round(ans1, 2))


# calculate 3b
def calculate_3b():
    var1 = frame3b_scale1.scale.get()
    var2 = frame3b_scale2.scale.get()
    var3 = frame3b_scale3.scale.get()
    var4 = atl(var3, var1)
    ans1 = Moment_Inertia(circle_constant, var1, var2)
    ans2 = Angular_Momentum(ans1, var3)
    ans3 = Linear_Momentum(var2, var4)
    frame3b_entry1.entry.delete(0, END)
    frame3b_entry1.entry.insert(0, round(ans1, 2))
    frame3b_entry2.entry.delete(0, END)
    frame3b_entry2.entry.insert(0, round(ans2, 2))
    frame3b_entry3.entry.delete(0, END)
    frame3b_entry3.entry.insert(0, round(ans3, 2))


# calculate 3c
def calculate_3c():
    var1 = frame3c_scale1.scale.get()
    var2 = frame3c_scale2.scale.get()
    var3 = frame3c_scale3.scale.get()
    var4 = atl(var3, var1)
    ans1 = Moment_Inertia(circle_constant, var1, var2)
    ans2 = Rotational_Kinetic_Energy(ans1, var3)
    ans3 = Linear_Kinetic_Energy(var2, var4)
    ans4 = TKE(ans2, ans3)
    frame3c_entry1.entry.delete(0, END)
    frame3c_entry1.entry.insert(0, round(ans1, 2))
    frame3c_entry2.entry.delete(0, END)
    frame3c_entry2.entry.insert(0, round(ans2, 2))
    frame3c_entry3.entry.delete(0, END)
    frame3c_entry3.entry.insert(0, round(ans3, 2))
    frame3c_entry4.entry.delete(0, END)
    frame3c_entry4.entry.insert(0, round(ans4, 2))


# animate orbiting particle
def animate_orbiting_particle(canvas, radius, ang_vel):
    orbiting_particle_animation(root,
                                canvas,
                                float(canvas_width) / 2.0,
                                float(canvas_height) / 2.0,
                                float(radius.get()) * float(len_mult_scale.scale.get()),
                                float(ang_vel.get()) / float(time_factor_scale.scale.get()),
                                granularity_scale.scale.get()
                                )


# animate 1a
def animate_1a():
    global frame1a_canvas1, frame1a_scale1, frame1a_scale3
    animate_orbiting_particle(frame1a_canvas1.canvas,
                              frame1a_scale1.scale,
                              frame1a_scale3.scale
                              )


# animate 1b
def animate_1b():
    animate_orbiting_particle(frame1b_canvas1.canvas,
                              frame1b_scale1.scale,
                              frame1b_scale3.scale
                              )


# animate 1c
def animate_1c():
    animate_orbiting_particle(frame1c_canvas1.canvas,
                              frame1c_scale1.scale,
                              frame1c_scale3.scale
                              )


# animate rotating circle
def animate_rotating_circle(canvas, radius, ang_vel):
    rotating_circle_animation(root,
                              canvas,
                              float(canvas_width) / 2.0,
                              float(canvas_height) / 2.0,
                              float(radius.get()) * float(len_mult_scale.scale.get()),
                              float(ang_vel.get()) / float(time_factor_scale.scale.get()),
                              granularity_scale.scale.get()
                              )


# animate 2a
def animate_2a():
    animate_rotating_circle(frame2a_canvas1.canvas,
                            frame2a_scale1.scale,
                            frame2a_scale3.scale
                            )


# animate 2b
def animate_2b():
    animate_rotating_circle(frame2b_canvas1.canvas,
                            frame2b_scale1.scale,
                            frame2b_scale3.scale
                            )


# animate 2c
def animate_2c():
    animate_rotating_circle(frame2c_canvas1.canvas,
                            frame2c_scale1.scale,
                            frame2c_scale3.scale
                            )


def animate_rolling_circle(canvas, radius, ang_vel):
    rolling_circle_animation(root,
                             canvas,
                             float(canvas_width) / 2.0,
                             float(canvas_height) / 2.0,
                             float(radius.get()) * float(len_mult_scale.scale.get()),
                             float(ang_vel.get()) / float(time_factor_scale.scale.get()),
                             granularity_scale.scale.get()
                             )


def animate_3a():
    animate_rolling_circle(frame3a_canvas1.canvas,
                           frame3a_scale1.scale,
                           frame3a_scale3.scale
                           )


def animate_3b():
    animate_rolling_circle(frame3b_canvas1.canvas,
                           frame3b_scale1.scale,
                           frame3b_scale3.scale
                           )


def animate_3c():
    animate_rolling_circle(frame3c_canvas1.canvas,
                           frame3c_scale1.scale,
                           frame3c_scale3.scale
                           )


# frame1a objects
main_label_1a = MyLabel(frame1a.frame, 'Orbiting Particle Basics', 0.05, 0.05)
calculate_button_1a = MyButton(frame1a.frame, 'Calculate', calculate_1a, 0.70, 0.90)
animate_button_1a = MyButton(frame1a.frame, 'Animate', animate_1a, 0.85, 0.90)
frame1a_scale1 = MyScale(frame1a.frame, 'Radius (m)', 0.05, 0.20)
frame1a_scale2 = MyScale(frame1a.frame, 'Mass (kg)', 0.05, 0.35)
frame1a_scale3 = MyScale(frame1a.frame, 'Angular Velocity (rad/s)', 0.05, 0.50)
frame1a_entry1 = MyEntry(frame1a.frame, 'Moment of Inertia (kgm^2)', 0.85, 0.20)
frame1a_canvas1 = MyCanvas(frame1a.frame)

# frame1b objects
main_label_1b = MyLabel(frame1b.frame, 'Orbiting Particle Momentum', 0.05, 0.05)
calculate_button_1b = MyButton(frame1b.frame, 'Calculate', calculate_1b, 0.70, 0.90)
animate_button_1b = MyButton(frame1b.frame, 'Animate', animate_1b, 0.85, 0.90)
frame1b_scale1 = MyScale(frame1b.frame, 'Radius (m)', 0.05, 0.20)
frame1b_scale2 = MyScale(frame1b.frame, 'Mass (kg)', 0.05, 0.35)
frame1b_scale3 = MyScale(frame1b.frame, 'Angular Velocity (rad/s)', 0.05, 0.50)
frame1b_entry1 = MyEntry(frame1b.frame, 'Moment of Inertia (kgm^2)', 0.85, 0.20)
frame1b_entry2 = MyEntry(frame1b.frame, 'Angular Momentum (kgm^2/s)', 0.85, 0.35)
frame1b_canvas1 = MyCanvas(frame1b.frame)

# frame1c objects
main_label_1c = MyLabel(frame1c.frame, 'Orbiting Particle Energy', 0.05, 0.05)
calculate_button_1c = MyButton(frame1c.frame, 'Calculate', calculate_1c, 0.70, 0.90)
animate_button_1c = MyButton(frame1c.frame, 'Animate', animate_1c, 0.85, 0.90)
frame1c_scale1 = MyScale(frame1c.frame, 'Radius (m)', 0.05, 0.20)
frame1c_scale2 = MyScale(frame1c.frame, 'Mass (kg)', 0.05, 0.35)
frame1c_scale3 = MyScale(frame1c.frame, 'Angular Velocity (rad/s)', 0.05, 0.50)
frame1c_entry1 = MyEntry(frame1c.frame, 'Moment of Inertia (kgm^2)', 0.85, 0.20)
frame1c_entry2 = MyEntry(frame1c.frame, 'Rotational Kinetic Energy (J)', 0.85, 0.35)
frame1c_canvas1 = MyCanvas(frame1c.frame)

# frame2a objects
main_label_2a = MyLabel(frame2a.frame, 'Rotating Circle Basics', 0.05, 0.05)
calculate_button_2a = MyButton(frame2a.frame, 'Calculate', calculate_2a, 0.70, 0.90)
animate_button_2a = MyButton(frame2a.frame, 'Animate', animate_2a, 0.85, 0.90)
frame2a_scale1 = MyScale(frame2a.frame, 'Radius (m)', 0.05, 0.20)
frame2a_scale2 = MyScale(frame2a.frame, 'Mass (kg)', 0.05, 0.35)
frame2a_scale3 = MyScale(frame2a.frame, 'Angular Velocity (rad/s)', 0.05, 0.50)
frame2a_entry1 = MyEntry(frame2a.frame, 'Moment of Inertia (kgm^2)', 0.85, 0.20)
frame2a_canvas1 = MyCanvas(frame2a.frame)

# frame2b objects
main_label_2b = MyLabel(frame2b.frame, 'Rotating Circle Momentum', 0.05, 0.05)
calculate_button_2b = MyButton(frame2b.frame, 'Calculate', calculate_2b, 0.70, 0.90)
animate_button_2b = MyButton(frame2b.frame, 'Animate', animate_2b, 0.85, 0.90)
frame2b_scale1 = MyScale(frame2b.frame, 'Radius (m)', 0.05, 0.20)
frame2b_scale2 = MyScale(frame2b.frame, 'Mass (kg)', 0.05, 0.35)
frame2b_scale3 = MyScale(frame2b.frame, 'Angular Velocity (rad/s)', 0.05, 0.50)
frame2b_entry1 = MyEntry(frame2b.frame, 'Moment of Inertia (kgm^2)', 0.85, 0.20)
frame2b_entry2 = MyEntry(frame2b.frame, 'Angular Momentum (kgm^2/s)', 0.85, 0.35)
frame2b_canvas1 = MyCanvas(frame2b.frame)

# frame2c objects
main_label_2c = MyLabel(frame2c.frame, 'Rotating Circle Energy', 0.05, 0.05)
calculate_button_2c = MyButton(frame2c.frame, 'Calculate', calculate_2c, 0.70, 0.90)
animate_button_2c = MyButton(frame2c.frame, 'Animate', animate_2c, 0.85, 0.90)
frame2c_scale1 = MyScale(frame2c.frame, 'Radius (m)', 0.05, 0.20)
frame2c_scale2 = MyScale(frame2c.frame, 'Mass (kg)', 0.05, 0.35)
frame2c_scale3 = MyScale(frame2c.frame, 'Angular Velocity (rad/s)', 0.05, 0.50)
frame2c_entry1 = MyEntry(frame2c.frame, 'Moment of Inertia (kgm^2)', 0.85, 0.20)
frame2c_entry2 = MyEntry(frame2c.frame, 'Rotational Kinetic Energy (J)', 0.85, 0.35)
frame2c_canvas1 = MyCanvas(frame2c.frame)

# frame3a objects
main_label_3a = MyLabel(frame3a.frame, 'Rolling Circle Basics', 0.05, 0.05)
calculate_button_3a = MyButton(frame3a.frame, 'Calculate', calculate_3a, 0.70, 0.90)
animate_button_3a = MyButton(frame3a.frame, 'Animate', animate_3a, 0.85, 0.90)
frame3a_scale1 = MyScale(frame3a.frame, 'Radius (m)', 0.05, 0.20)
frame3a_scale2 = MyScale(frame3a.frame, 'Mass (kg)', 0.05, 0.35)
frame3a_scale3 = MyScale(frame3a.frame, 'Angular Velocity (rad/s)', 0.05, 0.50)
frame3a_entry1 = MyEntry(frame3a.frame, 'Moment of Inertia (kgm^2)', 0.85, 0.20)
frame3a_canvas1 = MyCanvas(frame3a.frame)

# frame3b objects
main_label_3b = MyLabel(frame3b.frame, 'Rolling Circle Momentum', 0.05, 0.05)
calculate_button_3b = MyButton(frame3b.frame, 'Calculate', calculate_3b, 0.70, 0.90)
animate_button_3b = MyButton(frame3b.frame, 'Animate', animate_3b, 0.85, 0.90)
frame3b_scale1 = MyScale(frame3b.frame, 'Radius (m)', 0.05, 0.20)
frame3b_scale2 = MyScale(frame3b.frame, 'Mass (kg)', 0.05, 0.35)
frame3b_scale3 = MyScale(frame3b.frame, 'Angular Velocity (rad/s)', 0.05, 0.50)
frame3b_entry1 = MyEntry(frame3b.frame, 'Moment of Inertia (kgm^2)', 0.85, 0.20)
frame3b_entry2 = MyEntry(frame3b.frame, 'Angular Momentum (kgm^2/s)', 0.85, 0.35)
frame3b_entry3 = MyEntry(frame3b.frame, 'Linear Momentum (kgm/s)', 0.85, 0.50)
frame3b_canvas1 = MyCanvas(frame3b.frame)

# frame3c objects
main_label_3c = MyLabel(frame3c.frame, 'Rolling Circle Energy', 0.05, 0.05)
calculate_button_3c = MyButton(frame3c.frame, 'Calculate', calculate_3c, 0.70, 0.90)
animate_button_3c = MyButton(frame3c.frame, 'Animate', animate_3c, 0.85, 0.90)
frame3c_scale1 = MyScale(frame3c.frame, 'Radius (m)', 0.05, 0.2)
frame3c_scale2 = MyScale(frame3c.frame, 'Mass (kg)', 0.05, 0.35)
frame3c_scale3 = MyScale(frame3c.frame, 'Angular Velocity (rad/s)', 0.05, 0.50)
frame3c_entry1 = MyEntry(frame3c.frame, 'Moment of Inertia (kgm^2)', 0.85, 0.20)
frame3c_entry2 = MyEntry(frame3c.frame, 'Rotational Kinetic Energy (J)', 0.85, 0.35)
frame3c_entry3 = MyEntry(frame3c.frame, 'Linear Kinetic Energy (J)', 0.85, 0.50)
frame3c_entry4 = MyEntry(frame3c.frame, 'Total Kinetic Energy (J)', 0.85, 0.65)
frame3c_canvas1 = MyCanvas(frame3c.frame)

root.mainloop()
