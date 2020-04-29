# for other modules

# imports
from data.myvariables import main_width, main_height

# for all
ask_again_list = ['Do Not Ask Again?', 'Do you want to disable further alerts like this?']

# for main component
# creating canvas vars
# canvas size vars relative to main
canvas_width = 0.34 * main_width
canvas_height = 0.34 * (16.0 / 9.0) * main_height

# canvas placing vars relative to main
canvas_relx = 0.33
canvas_rely = 0.20

# creating frame bottom pad and frame button rely position variables
# frame bottom padding variable
frame_bottom_pad1 = 0.1
frame_bottom_pad2 = 0.1 / 0.9

# frame button rely variable
fb_rely_primary = (1.0 - frame_bottom_pad1) + 0.025
fb_rely_secondary = (1.0 - frame_bottom_pad2) + (0.025 / 0.9)

# for c_other
# scale relative sizing
scale_relwidth = 0.10
scale_relheight = 0.08

# for f_calculations
# moment of inertia constants
particle_constant = 1.0
circle_constant = 0.5

# for f_animations
# orbiting particle vars
part_radius = 20.0

# rotating circle vars
circum_width = 5.0
spoke_width = 5.0
spoke_number = 4
spoke_step = 360.0 / spoke_number

# moving platform vars
platform_width = 2.0

# for c_game
# custom colors
color_green = '#008000'
color_red = '#800000'
