# animation functions

# imports
from Tkinter import ALL

from tkMessageBox import askquestion

from math import pi, sin, cos

from f_other import dtr, ttl

from data.variables import colors, spoke_step, platform_width, part_radius, circum_width

radius_error_ask_bool = True
ang_vel_error_ask_bool = True


# animate orbiting particle
def orbiting_particle_animation(root,
                                canvas,
                                x_pos,
                                y_pos,
                                radius,
                                ang_vel,
                                granularity
                                ):
    global radius_error_ask_bool, ang_vel_error_ask_bool
    # checking value ranges
    if radius > 200 and radius_error_ask_bool:
        radius_error = askquestion('Run Animation',
                                   'You have selected parameters which may cause parts of the animation to be invisible, \n'
                                   'it is recommended that you modify the animation settings\n'
                                   'do you want to run the animation anyway?',
                                   icon='warning')
        if radius_error == 'no':
            return

        else:
            radius_error_ask = askquestion('Ask Again?', 'Do you want to disable further alerts like this?')

            if radius_error_ask == 'yes':
                radius_error_ask_bool = False

    if ang_vel > 15 and ang_vel_error_ask_bool:
        ang_vel_error = askquestion('Run Animation',
                                    'You have selected parameters which may cause the animation speed to be inaccurate, \n'
                                    'it is recommended that you modify the animation settings\n'
                                    'do you want to run the animation anyway?',
                                    icon='warning')

        if ang_vel_error == 'no':
            return

        else:
            ang_vel_error_ask = askquestion('Ask Again?', 'Do you want to disable further alerts like this?')

            if ang_vel_error_ask == 'yes':
                ang_vel_error_ask_bool = False

    # angular frequency defined as angular velocity / 2pi
    ang_freq = ang_vel / (2 * pi)

    # clearing canvas
    canvas.delete(ALL)

    # center_particle
    canvas.create_oval(x_pos - part_radius,
                       y_pos - part_radius,
                       x_pos + part_radius,
                       y_pos + part_radius,
                       fill=colors[4]
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
            ref_ms = int(1000 * ((1.0 / float(ang_freq)) / (360.0 / float(granularity))))
            x = x_pos + (float(radius) * sin(dtr(theta)))
            y = y_pos + (float(-radius) * cos(dtr(theta)))
            orb_part = canvas.create_oval(x - part_radius,
                                          y - part_radius,
                                          x + part_radius,
                                          y + part_radius,
                                          fill=colors[4]
                                          )
            canvas.update()
            root.after(ref_ms, canvas.delete(orb_part))


# animate rotating circle
def rotating_circle_animation(root,
                              canvas,
                              x_pos,
                              y_pos,
                              radius,
                              ang_vel,
                              granularity):
    global radius_error_ask_bool, ang_vel_error_ask_bool
    # checking value ranges
    if radius > 200 and radius_error_ask_bool:
        radius_error = askquestion('Run Animation',
                                   'You have selected parameters which may cause parts of the animation to be invisible, \n'
                                   'it is recommended that you modify the animation settings\n'
                                   'do you want to run the animation anyway?',
                                   icon='warning')
        if radius_error == 'no':
            return

        else:
            radius_error_ask = askquestion('Ask Again?', 'Do you want to disable further alerts like this?')

            if radius_error_ask == 'yes':
                radius_error_ask_bool = False

    if ang_vel > 15 and ang_vel_error_ask_bool:
        ang_vel_error = askquestion('Run Animation',
                                    'You have selected parameters which may cause the animation speed to be inaccurate, \n'
                                    'it is recommended that you modify the animation settings\n'
                                    'do you want to run the animation anyway?',
                                    icon='warning')

        if ang_vel_error == 'no':
            return

        else:
            ang_vel_error_ask = askquestion('Ask Again?', 'Do you want to disable further alerts like this?')

            if ang_vel_error_ask == 'yes':
                ang_vel_error_ask_bool = False

    # angular frequency defined as angular velocity / 2pi
    ang_freq = ang_vel / (2 * pi)

    # clearing canvas
    canvas.delete(ALL)

    # circumference
    canvas.create_oval(x_pos - radius,
                       y_pos - radius,
                       x_pos + radius,
                       y_pos + radius,
                       width=circum_width
                       )

    # center
    canvas.create_oval(x_pos - (float(radius) / 50.0),
                       y_pos - (float(radius) / 50.0),
                       x_pos + (float(radius) / 50.0),
                       y_pos + (float(radius) / 50.0),
                       width=circum_width
                       )

    while True:
        for theta in range(0, 360, int(granularity)):
            ref_ms = int(1000 * ((1.0 / float(ang_freq)) / (360.0 / float(granularity))))

            line1 = ttl(canvas, x_pos, y_pos, radius, theta + (0 * spoke_step))
            line2 = ttl(canvas, x_pos, y_pos, radius, theta + (1 * spoke_step))
            line3 = ttl(canvas, x_pos, y_pos, radius, theta + (2 * spoke_step))
            line4 = ttl(canvas, x_pos, y_pos, radius, theta + (3 * spoke_step))

            canvas.update()
            root.after(ref_ms, canvas.delete(line1, line2, line3, line4))


# animate rolling circle
def rolling_circle_animation(root,
                             canvas,
                             x_pos,
                             y_pos,
                             radius,
                             ang_vel,
                             granularity
                             ):
    global radius_error_ask_bool, ang_vel_error_ask_bool
    # checking value ranges
    if radius > 200 and radius_error_ask_bool:
        radius_error = askquestion('Run Animation',
                                   'You have selected parameters which may cause parts of the animation to be invisible, \n'
                                   'it is recommended that you modify the animation settings\n'
                                   'do you want to run the animation anyway?',
                                   icon='warning')
        if radius_error == 'no':
            return

        else:
            radius_error_ask = askquestion('Ask Again?', 'Do you want to disable further alerts like this?')

            if radius_error_ask == 'yes':
                radius_error_ask_bool = False

    if ang_vel > 15 and ang_vel_error_ask_bool:
        ang_vel_error = askquestion('Run Animation',
                                    'You have selected parameters which may cause the animation speed to be inaccurate, \n'
                                    'it is recommended that you modify the animation settings\n'
                                    'do you want to run the animation anyway?',
                                    icon='warning')

        if ang_vel_error == 'no':
            return

        else:
            ang_vel_error_ask = askquestion('Ask Again?', 'Do you want to disable further alerts like this?')

            if ang_vel_error_ask == 'yes':
                ang_vel_error_ask_bool = False

    circumference = 2.0 * pi * float(radius)
    ang_freq = ang_vel / (2 * pi)
    arc_len = float(granularity) / 360.0 * float(circumference)

    line_step = int(radius)

    ref_ms = int(1000 * ((1.0 / float(ang_freq)) / (360.0 / float(granularity))))

    px_pos = x_pos - (2 * float(radius))
    py_pos = y_pos + radius + (0.5 * circum_width)
    platform_len = 4.0 * float(radius)
    platform_thickness = float(platform_len) / 10.0

    # clearing canvas
    canvas.delete(ALL)

    rec_num = 0

    while True:
        for theta in range(0, 360, int(granularity)):

            # circumference
            canvas.create_oval(x_pos - radius,
                               y_pos - radius,
                               x_pos + radius,
                               y_pos + radius,
                               width=circum_width
                               )

            # center
            canvas.create_oval(x_pos - (float(radius) / 50.0),
                               y_pos - (float(radius) / 50.0),
                               x_pos + (float(radius) / 50.0),
                               y_pos + (float(radius) / 50.0),
                               width=circum_width
                               )

            # platform outline
            canvas.create_rectangle(px_pos,
                                    py_pos,
                                    px_pos + platform_len,
                                    py_pos + platform_thickness,
                                    width=platform_width
                                    )

            # rotating spokes
            for line_theta in range(theta, theta + 360, int(spoke_step)):
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
