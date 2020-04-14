# main file

# importing default python modules
from Tkinter import *

import random
import os
import sys

# importing custom python modules

# importing custom modules
import myclasses
import myfunctions
import myvars

# space to test code

print "hello there"

# creating root
root = Tk()
root.title("Rotational Motion")
root.geometry(myvars.start_geometry)
root.configure(bg=myvars.colors[4])

# base frames
start_bf = myclasses.MyFrame(root, myvars.colors[4])
main_bf = myclasses.MyFrame(root, myvars.colors[4])
game_bf = myclasses.MyFrame(root, myvars.colors[4])
cheatsheet_bf = myclasses.MyFrame(root, myvars.colors[4])
documentation_bf = myclasses.MyFrame(root, myvars.colors[4])

# raising start_bf and setting window size
start_bf.frame.tkraise()


# restart function
def restart(event):
    # code from "https://blog.petrzemek.net/2014/03/23/restarting-a-python-script-within-itself/"
    os.execv(sys.executable, ['python'] + sys.argv)


def restart1():
    os.execv(sys.executable, ['python'] + sys.argv)


# creating program-wide binds
root.bind("<Control-r>", restart)


# goto functions
def goto(bf):
    start_bf.frame.destroy()
    bf.frame.tkraise()


def goto_main():
    root.geometry(myvars.root_geometry)

    cheatsheet_bf.frame.destroy()
    game_bf.frame.destroy()
    documentation_bf.frame.destroy()

    goto(main_bf)


def goto_game():
    root.geometry(myvars.root_geometry)
    root.title("Quiz Game")
    main_bf.frame.destroy()
    cheatsheet_bf.frame.destroy()
    documentation_bf.frame.destroy()

    goto(game_bf)


def goto_cheatsheet():
    root.geometry(myvars.cheatsheet_geometry)
    root.title("CheatSheet")
    main_bf.frame.destroy()
    game_bf.frame.destroy()
    documentation_bf.frame.destroy()

    goto(cheatsheet_bf)


def goto_documentation():
    root.geometry(myvars.root_geometry)
    root.title("Documentation")

    main_bf.frame.destroy()
    cheatsheet_bf.frame.destroy()
    game_bf.frame.destroy()

    goto(documentation_bf)


# start_bf objects
title_label = myclasses.MyLabel(start_bf.frame, "Welcome!", 0.25, 0.05)
title_label.label.configure(bg=myvars.colors[4])
title_label.label.place(relwidth=0.5)

button1 = myclasses.MyButton(start_bf.frame, "Main", goto_main, 0.25, 0.15)
button1.button.place(relwidth=0.5)

button2 = myclasses.MyButton(start_bf.frame, "Quiz Game", goto_game, 0.25, 0.30)
button2.button.place(relwidth=0.5)

button3 = myclasses.MyButton(start_bf.frame, "CheatSheet", goto_cheatsheet, 0.25, 0.45)
button3.button.place(relwidth=0.5)

button4 = myclasses.MyButton(start_bf.frame, "Documentation", goto_documentation, 0.25, 0.60)
button4.button.place(relwidth=0.5)

footnote_label = myclasses.MyLabel(start_bf.frame,
                                   "created by: \n Yaqin Hasan \n Lian Chao Hooi \n Ibraheem El-Nahta \n Jaden Pang",
                                   0.25, 0.70
                                   )
footnote_label.label.configure(bg=myvars.colors[4], fg=myvars.colors[3])
footnote_label.label.place(relwidth=0.5, relheight=0.25)

# main_bf objects

# creating frames
main_pf1 = myclasses.MyFrame(main_bf.frame, myvars.colors[4])
main_pf2 = myclasses.MyFrame(main_bf.frame, myvars.colors[4])
frame1 = myclasses.MyFrameWBP(main_bf.frame, myvars.colors[4], myvars.frame_bottom_pad1)
frame2 = myclasses.MyFrameWBP(main_bf.frame, myvars.colors[4], myvars.frame_bottom_pad1)
frame3 = myclasses.MyFrameWBP(main_bf.frame, myvars.colors[4], myvars.frame_bottom_pad1)
frame1a = myclasses.MyFrameWBP(frame1.frame, myvars.colors[3], myvars.frame_bottom_pad2)
frame1b = myclasses.MyFrameWBP(frame1.frame, myvars.colors[3], myvars.frame_bottom_pad2)
frame1c = myclasses.MyFrameWBP(frame1.frame, myvars.colors[3], myvars.frame_bottom_pad2)
frame2a = myclasses.MyFrameWBP(frame2.frame, myvars.colors[3], myvars.frame_bottom_pad2)
frame2b = myclasses.MyFrameWBP(frame2.frame, myvars.colors[3], myvars.frame_bottom_pad2)
frame2c = myclasses.MyFrameWBP(frame2.frame, myvars.colors[3], myvars.frame_bottom_pad2)
frame3a = myclasses.MyFrameWBP(frame3.frame, myvars.colors[3], myvars.frame_bottom_pad2)
frame3b = myclasses.MyFrameWBP(frame3.frame, myvars.colors[3], myvars.frame_bottom_pad2)
frame3c = myclasses.MyFrameWBP(frame3.frame, myvars.colors[3], myvars.frame_bottom_pad2)


# frame flip functions
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


# frame navigation buttons

enter_as = myclasses.MyButton(main_pf1.frame, "Animation Settings", flip_main_pf2, 0.05, myvars.fb_rely_primary)
exit_as = myclasses.MyButton(main_pf2.frame, "Exit", flip_main_pf1, 0.05, myvars.fb_rely_primary)
fb1 = myclasses.MyButton(main_pf1.frame, "Orbiting Particle", flip_frame1, 0.55, myvars.fb_rely_primary)
fb2 = myclasses.MyButton(main_pf1.frame, "Rotating Circle", flip_frame2, 0.70, myvars.fb_rely_primary)
fb3 = myclasses.MyButton(main_pf1.frame, "Rolling Circle", flip_frame3, 0.85, myvars.fb_rely_primary)
fb1a = myclasses.MyButton(frame1.frame, "Basic", flip_frame1a, 0.55, myvars.fb_rely_secondary)
fb1b = myclasses.MyButton(frame1.frame, "Momentum", flip_frame1b, 0.70, myvars.fb_rely_secondary)
fb1c = myclasses.MyButton(frame1.frame, "Energy", flip_frame1c, 0.85, myvars.fb_rely_secondary)
fb2a = myclasses.MyButton(frame2.frame, "Basic", flip_frame2a, 0.55, myvars.fb_rely_secondary)
fb2b = myclasses.MyButton(frame2.frame, "Momentum", flip_frame2b, 0.70, myvars.fb_rely_secondary)
fb2c = myclasses.MyButton(frame2.frame, "Energy", flip_frame2c, 0.85, myvars.fb_rely_secondary)
fb3a = myclasses.MyButton(frame3.frame, "Basic", flip_frame3a, 0.55, myvars.fb_rely_secondary)
fb3b = myclasses.MyButton(frame3.frame, "Momentum", flip_frame3b, 0.70, myvars.fb_rely_secondary)
fb3c = myclasses.MyButton(frame3.frame, "Energy", flip_frame3c, 0.85, myvars.fb_rely_secondary)

# setting default frame order
flip_main_pf2()
flip_main_pf1()
flip_frame3()
flip_frame2()
flip_frame1()

# main_pf2 (animation settings) objects

main_pf2_title = myclasses.MyLabel(main_pf2.frame, "Animation Settings", 0.05, 0.05)
main_pf2_title.label.configure(bg=myvars.colors[4])

time_factor_scale = myclasses.MyScale(main_pf2.frame, "Time Factor", 0.05, 0.15)
len_mult_scale = myclasses.MyScale(main_pf2.frame, "Length Multiplier", 0.05, 0.30)
granularity_scale = myclasses.MyScale(main_pf2.frame, "Granularity", 0.05, 0.45)

time_factor_scale.scale.configure(from_=1, to=100, resolution=1, bg=myvars.colors[4])
len_mult_scale.scale.configure(from_=1, to=100, resolution=1, bg=myvars.colors[4])
granularity_scale.scale.configure(from_=1, to=90, resolution=5, bg=myvars.colors[4])

time_factor_scale.label.configure(bg=myvars.colors[4])
len_mult_scale.label.configure(bg=myvars.colors[4])
granularity_scale.label.configure(bg=myvars.colors[4])

time_factor_scale.scale.set(5)
len_mult_scale.scale.set(10)
granularity_scale.scale.set(15)


# calculation functions

# calculate 1a
def calculate_1a():
    var1 = frame1a_scale1.scale.get()
    var2 = frame1a_scale2.scale.get()
    ans1 = myfunctions.Moment_Inertia(myvars.particle_constant, var1, var2)
    frame1a_entry1.entry.delete(0, END)
    frame1a_entry1.entry.insert(0, round(ans1, 2))


# calculate 1b
def calculate_1b():
    var1 = frame1b_scale1.scale.get()
    var2 = frame1b_scale2.scale.get()
    var3 = frame1b_scale3.scale.get()
    ans1 = myfunctions.Moment_Inertia(myvars.particle_constant, var1, var2)
    ans2 = myfunctions.Angular_Momentum(ans1, var3)
    frame1b_entry1.entry.delete(0, END)
    frame1b_entry1.entry.insert(0, round(ans1, 2))
    frame1b_entry2.entry.delete(0, END)
    frame1b_entry2.entry.insert(0, round(ans2, 2))


# calculate 1c
def calculate_1c():
    var1 = frame1c_scale1.scale.get()
    var2 = frame1c_scale2.scale.get()
    var3 = frame1c_scale3.scale.get()
    ans1 = myfunctions.Moment_Inertia(myvars.particle_constant, var1, var2)
    ans2 = myfunctions.Rotational_Kinetic_Energy(ans1, var3)
    frame1c_entry1.entry.delete(0, END)
    frame1c_entry1.entry.insert(0, round(ans1, 2))
    frame1c_entry2.entry.delete(0, END)
    frame1c_entry2.entry.insert(0, round(ans2, 2))


# calculate 2a
def calculate_2a():
    var1 = frame2a_scale1.scale.get()
    var2 = frame2a_scale2.scale.get()
    ans1 = myfunctions.Moment_Inertia(myvars.circle_constant, var1, var2)
    frame2a_entry1.entry.delete(0, END)
    frame2a_entry1.entry.insert(0, round(ans1, 2))


# calculate 2b
def calculate_2b():
    var1 = frame2b_scale1.scale.get()
    var2 = frame2b_scale2.scale.get()
    var3 = frame2b_scale3.scale.get()
    ans1 = myfunctions.Moment_Inertia(myvars.circle_constant, var1, var2)
    ans2 = myfunctions.Angular_Momentum(ans1, var3)
    frame2b_entry1.entry.delete(0, END)
    frame2b_entry1.entry.insert(0, round(ans1, 2))
    frame2b_entry2.entry.delete(0, END)
    frame2b_entry2.entry.insert(0, round(ans2, 2))


# calculate 2c
def calculate_2c():
    var1 = frame2c_scale1.scale.get()
    var2 = frame2c_scale2.scale.get()
    var3 = frame2c_scale3.scale.get()
    ans1 = myfunctions.Moment_Inertia(myvars.circle_constant, var1, var2)
    ans2 = myfunctions.Rotational_Kinetic_Energy(ans1, var3)
    frame2c_entry1.entry.delete(0, END)
    frame2c_entry1.entry.insert(0, round(ans1, 2))
    frame2c_entry2.entry.delete(0, END)
    frame2c_entry2.entry.insert(0, round(ans2, 2))


# calculate 3a
def calculate_3a():
    var1 = frame3a_scale1.scale.get()
    var2 = frame3a_scale2.scale.get()
    ans1 = myfunctions.Moment_Inertia(myvars.circle_constant, var1, var2)
    frame3a_entry1.entry.delete(0, END)
    frame3a_entry1.entry.insert(0, round(ans1, 2))


# calculate 3b
def calculate_3b():
    var1 = frame3b_scale1.scale.get()
    var2 = frame3b_scale2.scale.get()
    var3 = frame3b_scale3.scale.get()
    var4 = myfunctions.atl(var3, var1)
    ans1 = myfunctions.Moment_Inertia(myvars.circle_constant, var1, var2)
    ans2 = myfunctions.Angular_Momentum(ans1, var3)
    ans3 = myfunctions.Linear_Momentum(var2, var4)
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
    var4 = myfunctions.atl(var3, var1)
    ans1 = myfunctions.Moment_Inertia(myvars.circle_constant, var1, var2)
    ans2 = myfunctions.Rotational_Kinetic_Energy(ans1, var3)
    ans3 = myfunctions.Linear_Kinetic_Energy(var2, var4)
    ans4 = myfunctions.TKE(ans2, ans3)
    frame3c_entry1.entry.delete(0, END)
    frame3c_entry1.entry.insert(0, round(ans1, 2))
    frame3c_entry2.entry.delete(0, END)
    frame3c_entry2.entry.insert(0, round(ans2, 2))
    frame3c_entry3.entry.delete(0, END)
    frame3c_entry3.entry.insert(0, round(ans3, 2))
    frame3c_entry4.entry.delete(0, END)
    frame3c_entry4.entry.insert(0, round(ans4, 2))


# animation functions

# animate orbiting particle
def animate_orbiting_particle(canvas, radius, ang_vel):
    myfunctions.animate_orbiting_particle(root,
                                          canvas,
                                          float(myvars.canvas_width) / 2.0,
                                          float(myvars.canvas_height) / 2.0,
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
    myfunctions.animate_rotating_circle(root,
                                        canvas,
                                        float(myvars.canvas_width) / 2.0,
                                        float(myvars.canvas_height) / 2.0,
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
    myfunctions.animate_rolling_circle(root,
                                       canvas,
                                       float(myvars.canvas_width) / 2.0,
                                       float(myvars.canvas_height) / 2.0,
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

main_label_1a = myclasses.MyLabel(frame1a.frame, "Orbiting Particle Basics", 0.05, 0.05)
calculate_button_1a = myclasses.MyButton(frame1a.frame, "Calculate", calculate_1a, 0.70, 0.90)
animate_button_1a = myclasses.MyButton(frame1a.frame, "Animate", animate_1a, 0.85, 0.90)
frame1a_scale1 = myclasses.MyScale(frame1a.frame, "Radius (m)", 0.05, 0.20)
frame1a_scale2 = myclasses.MyScale(frame1a.frame, "Mass (kg)", 0.05, 0.35)
frame1a_scale3 = myclasses.MyScale(frame1a.frame, "Angular Velocity (rad/s)", 0.05, 0.50)
frame1a_entry1 = myclasses.MyEntry(frame1a.frame, "Moment of Inertia (kgm^2)", 0.85, 0.20)
frame1a_canvas1 = myclasses.MyCanvas(frame1a.frame)

# frame1b objects

main_label_1b = myclasses.MyLabel(frame1b.frame, "Orbiting Particle Momentum", 0.05, 0.05)
calculate_button_1b = myclasses.MyButton(frame1b.frame, "Calculate", calculate_1b, 0.70, 0.90)
animate_button_1b = myclasses.MyButton(frame1b.frame, "Animate", animate_1b, 0.85, 0.90)
frame1b_scale1 = myclasses.MyScale(frame1b.frame, "Radius (m)", 0.05, 0.20)
frame1b_scale2 = myclasses.MyScale(frame1b.frame, "Mass (kg)", 0.05, 0.35)
frame1b_scale3 = myclasses.MyScale(frame1b.frame, "Angular Velocity (rad/s)", 0.05, 0.50)
frame1b_entry1 = myclasses.MyEntry(frame1b.frame, "Moment of Inertia (kgm^2)", 0.85, 0.20)
frame1b_entry2 = myclasses.MyEntry(frame1b.frame, "Angular Momentum (kgm^2/s)", 0.85, 0.35)
frame1b_canvas1 = myclasses.MyCanvas(frame1b.frame)

# frame1c objects

main_label_1c = myclasses.MyLabel(frame1c.frame, "Orbiting Particle Energy", 0.05, 0.05)
calculate_button_1c = myclasses.MyButton(frame1c.frame, "Calculate", calculate_1c, 0.70, 0.90)
animate_button_1c = myclasses.MyButton(frame1c.frame, "Animate", animate_1c, 0.85, 0.90)
frame1c_scale1 = myclasses.MyScale(frame1c.frame, "Radius (m)", 0.05, 0.20)
frame1c_scale2 = myclasses.MyScale(frame1c.frame, "Mass (kg)", 0.05, 0.35)
frame1c_scale3 = myclasses.MyScale(frame1c.frame, "Angular Velocity (rad/s)", 0.05, 0.50)
frame1c_entry1 = myclasses.MyEntry(frame1c.frame, "Moment of Inertia (kgm^2)", 0.85, 0.20)
frame1c_entry2 = myclasses.MyEntry(frame1c.frame, "Rotational Kinetic Energy (J)", 0.85, 0.35)
frame1c_canvas1 = myclasses.MyCanvas(frame1c.frame)

# frame2a objects

main_label_2a = myclasses.MyLabel(frame2a.frame, "Rotating Circle Basics", 0.05, 0.05)
calculate_button_2a = myclasses.MyButton(frame2a.frame, "Calculate", calculate_2a, 0.70, 0.90)
animate_button_2a = myclasses.MyButton(frame2a.frame, "Animate", animate_2a, 0.85, 0.90)
frame2a_scale1 = myclasses.MyScale(frame2a.frame, "Radius (m)", 0.05, 0.20)
frame2a_scale2 = myclasses.MyScale(frame2a.frame, "Mass (kg)", 0.05, 0.35)
frame2a_scale3 = myclasses.MyScale(frame2a.frame, "Angular Velocity (rad/s)", 0.05, 0.50)
frame2a_entry1 = myclasses.MyEntry(frame2a.frame, "Moment of Inertia (kgm^2)", 0.85, 0.20)
frame2a_canvas1 = myclasses.MyCanvas(frame2a.frame)

# frame2b objects

main_label_2b = myclasses.MyLabel(frame2b.frame, "Rotating Circle Momentum", 0.05, 0.05)
calculate_button_2b = myclasses.MyButton(frame2b.frame, "Calculate", calculate_2b, 0.70, 0.90)
animate_button_2b = myclasses.MyButton(frame2b.frame, "Animate", animate_2b, 0.85, 0.90)
frame2b_scale1 = myclasses.MyScale(frame2b.frame, "Radius (m)", 0.05, 0.20)
frame2b_scale2 = myclasses.MyScale(frame2b.frame, "Mass (kg)", 0.05, 0.35)
frame2b_scale3 = myclasses.MyScale(frame2b.frame, "Angular Velocity (rad/s)", 0.05, 0.50)
frame2b_entry1 = myclasses.MyEntry(frame2b.frame, "Moment of Inertia (kgm^2)", 0.85, 0.20)
frame2b_entry2 = myclasses.MyEntry(frame2b.frame, "Angular Momentum (kgm^2/s)", 0.85, 0.35)
frame2b_canvas1 = myclasses.MyCanvas(frame2b.frame)

# frame2c objects

main_label_2c = myclasses.MyLabel(frame2c.frame, "Rotating Circle Energy", 0.05, 0.05)
calculate_button_2c = myclasses.MyButton(frame2c.frame, "Calculate", calculate_2c, 0.70, 0.90)
animate_button_2c = myclasses.MyButton(frame2c.frame, "Animate", animate_2c, 0.85, 0.90)
frame2c_scale1 = myclasses.MyScale(frame2c.frame, "Radius (m)", 0.05, 0.20)
frame2c_scale2 = myclasses.MyScale(frame2c.frame, "Mass (kg)", 0.05, 0.35)
frame2c_scale3 = myclasses.MyScale(frame2c.frame, "Angular Velocity (rad/s)", 0.05, 0.50)
frame2c_entry1 = myclasses.MyEntry(frame2c.frame, "Moment of Inertia (kgm^2)", 0.85, 0.20)
frame2c_entry2 = myclasses.MyEntry(frame2c.frame, "Rotational Kinetic Energy (J)", 0.85, 0.35)
frame2c_canvas1 = myclasses.MyCanvas(frame2c.frame)

# frame3a objects

main_label_3a = myclasses.MyLabel(frame3a.frame, "Rolling Circle Basics", 0.05, 0.05)
calculate_button_3a = myclasses.MyButton(frame3a.frame, "Calculate", calculate_3a, 0.70, 0.90)
animate_button_3a = myclasses.MyButton(frame3a.frame, "Animate", animate_3a, 0.85, 0.90)
frame3a_scale1 = myclasses.MyScale(frame3a.frame, "Radius (m)", 0.05, 0.20)
frame3a_scale2 = myclasses.MyScale(frame3a.frame, "Mass (kg)", 0.05, 0.35)
frame3a_scale3 = myclasses.MyScale(frame3a.frame, "Angular Velocity (rad/s)", 0.05, 0.50)
frame3a_entry1 = myclasses.MyEntry(frame3a.frame, "Moment of Inertia (kgm^2)", 0.85, 0.20)
frame3a_canvas1 = myclasses.MyCanvas(frame3a.frame)

# frame3b objects

main_label_3b = myclasses.MyLabel(frame3b.frame, "Rolling Circle Momentum", 0.05, 0.05)
calculate_button_3b = myclasses.MyButton(frame3b.frame, "Calculate", calculate_3b, 0.70, 0.90)
animate_button_3b = myclasses.MyButton(frame3b.frame, "Animate", animate_3b, 0.85, 0.90)
frame3b_scale1 = myclasses.MyScale(frame3b.frame, "Radius (m)", 0.05, 0.20)
frame3b_scale2 = myclasses.MyScale(frame3b.frame, "Mass (kg)", 0.05, 0.35)
frame3b_scale3 = myclasses.MyScale(frame3b.frame, "Angular Velocity (rad/s)", 0.05, 0.50)
frame3b_entry1 = myclasses.MyEntry(frame3b.frame, "Moment of Inertia (kgm^2)", 0.85, 0.20)
frame3b_entry2 = myclasses.MyEntry(frame3b.frame, "Angular Momentum (kgm^2/s)", 0.85, 0.35)
frame3b_entry3 = myclasses.MyEntry(frame3b.frame, "Linear Momentum (kgm/s)", 0.85, 0.50)
frame3b_canvas1 = myclasses.MyCanvas(frame3b.frame)

# frame3c objects

main_label_3c = myclasses.MyLabel(frame3c.frame, "Rolling Circle Energy", 0.05, 0.05)
calculate_button_3c = myclasses.MyButton(frame3c.frame, "Calculate", calculate_3c, 0.70, 0.90)
animate_button_3c = myclasses.MyButton(frame3c.frame, "Animate", animate_3c, 0.85, 0.90)
frame3c_scale1 = myclasses.MyScale(frame3c.frame, "Radius (m)", 0.05, 0.2)
frame3c_scale2 = myclasses.MyScale(frame3c.frame, "Mass (kg)", 0.05, 0.35)
frame3c_scale3 = myclasses.MyScale(frame3c.frame, "Angular Velocity (rad/s)", 0.05, 0.50)
frame3c_entry1 = myclasses.MyEntry(frame3c.frame, "Moment of Inertia (kgm^2)", 0.85, 0.20)
frame3c_entry2 = myclasses.MyEntry(frame3c.frame, "Rotational Kinetic Energy (J)", 0.85, 0.35)
frame3c_entry3 = myclasses.MyEntry(frame3c.frame, "Linear Kinetic Energy (J)", 0.85, 0.50)
frame3c_entry4 = myclasses.MyEntry(frame3c.frame, "Total Kinetic Energy (J)", 0.85, 0.65)
frame3c_canvas1 = myclasses.MyCanvas(frame3c.frame)

# game_bf objects

# end screen objects
end_label = Label(game_bf.frame)
end_label.configure(text="You have gone through all the questions \n please come back later for more")
end_label.configure(bg=myvars.colors[4], fg=myvars.colors[0])
end_label.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.45)

end_button = myclasses.MyButton(game_bf.frame, "Relaunch", restart1, 0.45, 0.50)

# questions
q1 = myclasses.MyQuestion(game_bf.frame,
                          "What is the moment of inertia, I for a disc?",
                          "I = MR^2",
                          "I = 1/12 *  ML^2",
                          "I = 1/2 *  MR^2",
                          "I = 1/2 *  Mk^2",
                          "This is the Moment of Inertia for a particle.",
                          "This is the Moment of Inertia for a stick.",
                          "This is the Moment of Inertia for a disc.",
                          "This Moment of Inertia is for a particle of a disc and involves k, \nwhich is the radius of gyration.",
                          3
                          )

q2 = myclasses.MyQuestion(game_bf.frame,
                          "What is the Rotational Kinetic Energy of a rolling disc?",
                          "0.5 * mv^2",
                          "0.25 * mr^2w^2",
                          "0.5 * mr^2",
                          "0.25 * Iw^2",
                          "This is a formula for Linear Kinetic Energy.",
                          "For a rolling disc, the Rotational Kinetic Energy is given as, \nRKE = 0.5 * Iw^2 = 0.5 * (0.5 * mr^2)w^2 = 0.25 * mr^2w^2 ",
                          "This is the Moment of Inertia of a disc. \nNote: This formula does not involve any kind of velocity. \nThus, it cannot be Kinetic Energy.",
                          "For a rolling disc, the Rotational Kinetic Energy is given as, \nRKE = 0.5 * Iw^2. \n\nWhen the Moment of Inertia of the disc is substituted, \nthen only the 0.25 appear.",
                          2
                          )

q3 = myclasses.MyQuestion(game_bf.frame,
                          "What is the angular momentum, L for an orbiting particle?",
                          "L = mr^2w",
                          "L = mv",
                          "L = wr",
                          "L = mr^2",
                          "The angular momentum for an orbiting paticle is given as, \nL = Iw. \n\nThus, when the Moment of Inertia(I) of a disc is substituted, \nL = mr^2w ",
                          "Recall that LINEAR Momentum is the product of mass and velocity. \np = mv",
                          "This formula is used to find linear velocity. \nv = wr",
                          "This formula is the Moment of Inertia for a particle. \nI = mr^2",
                          1
                          )

q4 = myclasses.MyQuestion(game_bf.frame,
                          "Rate of change of angular momentum is equal to ___________?",
                          "torque",
                          "force",
                          "moment of inertia",
                          "angular velocity",
                          "Torque is the rate of change of angular momentum.",
                          "Force is the rate of change of LINEAR momentum.",
                          "Moment of Inertia is the product of mass and square of distance.",
                          "Angular Velocity is the rate of change of Angular Displacement in radians per second.",
                          1
                          )

q5 = myclasses.MyQuestion(game_bf.frame,
                          "What is the unit for Angular Momentum?",
                          "kgms^-1",
                          "kgm^2(s^-2)",
                          "kgm^2(s^-1)",
                          "kgm^2",
                          "This unit is for LINEAR Momentum. \nLinear and Angular Momentum have different units due to involving different quantities. \np = mv = kgms^-1",
                          "This unit is for Torque. \nTorque is the product of Moment of Inertia and Angular Acceleration. \nT = Ia = kgm^2(s^-2)",
                          "This is the unit for Angular Momentum. \nL = Iw = (MR^2)w = (kgm^2)s^-1",
                          "This is the unit for Moment of Inertia. \nI = mr^2 = kgm^2",
                          3
                          )

q6 = myclasses.MyQuestion(game_bf.frame,
                          "What real force keeps a satellite in a circular orbit around the earth?",
                          "Thrust",
                          "Gravity",
                          "Centripetal force",
                          "There is no force in space",
                          "This is a propulsive force. ",
                          "Gravitational pull of earth acts on the satellite which keeps the satellite in a circular orbit \naround the earth provided its velocity balances the gravitational force.",
                          "Centripetal force is just a net force.",
                          "Gravitational force exists in space.",
                          2
                          )

q7 = myclasses.MyQuestion(game_bf.frame,
                          "The velocity is always __________ to the line of a circle.",
                          "tangent",
                          "towards the center",
                          "outwards",
                          "inwards",
                          "Velocity acts tangent to a circle.",
                          "Centripetal force acts towards the center of a circle.",
                          "Invalid answer.",
                          "Invalid answer.",
                          1
                          )

q8 = myclasses.MyQuestion(game_bf.frame,
                          "What is the force that keeps an object in circular motion?",
                          "Centrifugal force",
                          "Centripetal force",
                          "Center-fleeing force",
                          "Gravitational Force",
                          "Centrifugal force is the tendency of an object to \nfly away from the center of a curved path.",
                          "Centripetal force is the net force keeping an object in circular motion. \nThe resultant force of all real forces acting on the object, \nthat acts towards the centre of the circular path is responsible for its circular motion.",
                          "This force is also called Centrifugal Force which is \nthe tendency of an object to fly away from the center of a curved path.",
                          "This is an attractive force which occurs between \nmasses of objects and it is not a net force.",
                          2
                          )

# shuffling questions
qlist = [q1, q2, q3, q4, q5, q6, q7, q8]
random.shuffle(qlist)

for q in qlist:
    q.pf.frame.tkraise()

# cheatsheet_bf objects

cheatsheet_img = myfunctions.MyImage("cheatsheet.jpg", myvars.cheatsheet_width, myvars.cheatsheet_height)
cheatsheet_label = Label(cheatsheet_bf.frame, image=cheatsheet_img)
cheatsheet_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# documentation_bf objects

'''
documentation_img = myfunctions.MyImage("documentation.jpg", myvars.documentation_width, myvars.documentation_height)
documentation_label = Label(documentation_bf.frame, image=documentation_img)
documentation_label.place(relx=0, rely=0, relwidth=1, relheight=1)
'''

root.mainloop()
