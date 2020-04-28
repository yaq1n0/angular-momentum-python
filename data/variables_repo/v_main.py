# for main component

# imports
from data.myvariables import main_width, main_height

# creating canvas vars
# canvas size vars relative to main
canvas_width = 0.25 * main_width
canvas_height = 0.25 * (16.0 / 9.0) * main_height

# canvas placing vars relative to main
canvas_relx = 0.375
canvas_rely = 0.20

# creating frame bottom pad and frame button rely position variables
# frame bottom padding variable
frame_bottom_pad1 = 0.1
frame_bottom_pad2 = 0.1 / 0.9

# frame button rely variable
fb_rely_primary = (1.0 - frame_bottom_pad1) + 0.025
fb_rely_secondary = (1.0 - frame_bottom_pad2) + (0.025 / 0.9)
