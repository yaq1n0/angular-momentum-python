# contains all custom functions

# importing python modules
from Tkinter import *
import tkMessageBox
import math

# importing personal modules
import myvars
import myclasses


# CreateToolTip function for ToolTip object
def CreateToolTip(widget, text):
    # instantizing toolTip instance of ToolTip class
    toolTip = myclasses.ToolTip(widget)

    # binding enter event to showtip method
    def enter(event):
        toolTip.showtip(text)

    # binding leave event to hidetip method
    def leave(event):
        toolTip.hidetip()

    # binging enter and leave
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


# PlaceHolder function for whatever
def PlaceHolder():
    tkMessageBox.showinfo("placeholder", "feature to be added or enabled in later version")


# finding moment of inertia
def Moment_Inertia(constant, radius, mass):
    return float(constant) * float(mass) * (float(radius) ** 2.0)


# finding angular momentum
def Angular_Momentum(inertia, omega):
    return float(inertia) * float(omega)


# finding linear momentum
def Linear_Momentum(mass, velocity):
    return float(mass) * float(velocity)


# finding rotational kinetic energy
def Rotational_Kinetic_Energy(inertia, omega):
    return 0.5 * float(inertia) * (float(omega) ** 2.0)


# finding linear kinetic energy
def Linear_Kinetic_Energy(mass, velocity):
    return 0.5 * float(mass) * (float(velocity) ** 2.0)


# finding total kinetic energy
def TKE(rotational, linear):
    return float(rotational) + float(linear)


# convert degrees to radians
def dtr(theta):
    tmpvar = math.pi / 180.0
    return float(theta) * float(tmpvar)


# convert angular velocity to frequency
def rtf(rad):
    tmpvar = 2.0 * math.pi
    return float(rad) / float(tmpvar)


# convert frequency to angular_velocity
def ftr(freq):
    tmpvar = 2.0 * math.pi
    return float(tmpvar) * float(freq)


# convert angular velocity into linear velocity
def atl(ang_vel, radius):
    return float(ang_vel) * float(radius)


# line at theta degrees from x_pos, y_pos to x, y (for animate_rotating_circle)
def ttl(canvas, x_pos, y_pos, radius, theta):
    x = x_pos + (float(radius) * math.sin(dtr(theta)))
    y = y_pos + (float(-radius) * math.cos(dtr(theta)))
    return canvas.create_line(x_pos, y_pos, x, y, width=myvars.spoke_width)


def animate_orbiting_particle(root,
                              canvas,
                              x_pos,
                              y_pos,
                              radius,
                              ang_vel,
                              granularity
                              ):
    canvas.delete(ALL)

    # center_particle
    canvas.create_oval(x_pos - myvars.part_radius,
                       y_pos - myvars.part_radius,
                       x_pos + myvars.part_radius,
                       y_pos + myvars.part_radius,
                       fill=myvars.colors[4]
                       )

    # orbit_path
    canvas.create_oval(x_pos - radius,
                       y_pos - radius,
                       x_pos + radius,
                       y_pos + radius
                       )

    # orbiting particle
    while True:
        for theta in range(0, 360, int(granularity)):
            ref_ms = int(1000 * ((1.0 / float(ang_vel)) / (360.0 / float(granularity))))
            x = x_pos + (float(radius) * math.sin(dtr(theta)))
            y = y_pos + (float(-radius) * math.cos(dtr(theta)))
            orb_part = canvas.create_oval(x - myvars.part_radius,
                                          y - myvars.part_radius,
                                          x + myvars.part_radius,
                                          y + myvars.part_radius,
                                          fill=myvars.colors[4]
                                          )
            canvas.update()
            root.after(ref_ms, canvas.delete(orb_part))


def animate_rotating_circle(root,
                            canvas,
                            x_pos,
                            y_pos,
                            radius,
                            ang_vel,
                            granularity):
    canvas.delete(ALL)

    # circumference
    canvas.create_oval(x_pos - radius,
                       y_pos - radius,
                       x_pos + radius,
                       y_pos + radius,
                       width=myvars.circum_width
                       )

    # center
    canvas.create_oval(x_pos - (float(radius) / 50.0),
                       y_pos - (float(radius) / 50.0),
                       x_pos + (float(radius) / 50.0),
                       y_pos + (float(radius) / 50.0),
                       width=myvars.circum_width
                       )

    while True:
        for theta in range(0, 360, int(granularity)):
            ref_ms = int(1000 * ((1.0 / float(ang_vel)) / (360.0 / float(granularity))))

            line1 = ttl(canvas, x_pos, y_pos, radius, theta + (0 * myvars.spoke_step))
            line2 = ttl(canvas, x_pos, y_pos, radius, theta + (1 * myvars.spoke_step))
            line3 = ttl(canvas, x_pos, y_pos, radius, theta + (2 * myvars.spoke_step))
            line4 = ttl(canvas, x_pos, y_pos, radius, theta + (3 * myvars.spoke_step))

            canvas.update()
            root.after(ref_ms, canvas.delete(line1, line2, line3, line4))


def animate_rolling_circle(root,
                           canvas,
                           x_pos,
                           y_pos,
                           radius,
                           ang_vel,
                           granularity
                           ):
    circumference = 2.0 * math.pi * float(radius)
    arc_len = float(granularity) / 360.0 * float(circumference)

    line_step = int(radius)

    ref_ms = int(1000 * ((1.0 / float(ang_vel)) / (360.0 / float(granularity))))

    px_pos = x_pos - (2 * float(radius))
    py_pos = y_pos + radius + (0.5 * myvars.circum_width)
    platform_len = 4.0 * float(radius)
    platform_thickness = float(platform_len) / 10.0

    canvas.delete(ALL)

    rec_num = 0

    while True:
        for theta in range(0, 360, int(granularity)):

            # circumference
            canvas.create_oval(x_pos - radius,
                               y_pos - radius,
                               x_pos + radius,
                               y_pos + radius,
                               width=myvars.circum_width
                               )

            # center
            canvas.create_oval(x_pos - (float(radius) / 50.0),
                               y_pos - (float(radius) / 50.0),
                               x_pos + (float(radius) / 50.0),
                               y_pos + (float(radius) / 50.0),
                               width=myvars.circum_width
                               )

            # platform outline
            canvas.create_rectangle(px_pos,
                                    py_pos,
                                    px_pos + platform_len,
                                    py_pos + platform_thickness,
                                    width=myvars.platform_width
                                    )

            # rotating spokes
            for line_theta in range(theta, theta + 360, int(myvars.spoke_step)):
                ttl(canvas, x_pos, y_pos, radius, line_theta)

            # moving platform
            rec_num += 1

            line_xpos = px_pos + platform_len - (rec_num * arc_len)

            # checking line_xpos validity and correcting if invalid
            if line_xpos <= px_pos + platform_len - line_step:
                rec_num = 0
                line_xpos = px_pos + platform_len - (rec_num * arc_len)

            # drawing vertical platform lines
            for line_pos in range(int(line_xpos), int(px_pos), -line_step):
                canvas.create_line(line_pos, py_pos, line_pos, py_pos + platform_thickness)

            # refreshing the canvas with all components drawn
            canvas.update()

            # deleting all components after ref_ms
            root.after(ref_ms, canvas.delete(ALL))
