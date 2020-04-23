# for main component

# imports
from data.myvariables import main_width, main_height

# creating canvas vars
# canvas size vars relative to main
canvas_window_ratio = 0.25
canvas_width = canvas_height = main_width * canvas_window_ratio

# canvas placing vars relative to main
frame_height = main_height * (0.9 ** 2)
canvas_relx = 1.5 * canvas_window_ratio
canvas_rely = ((frame_height - canvas_height) / 2) / frame_height

# creating frame bottom pad and frame button rely position variables
# frame bottom padding variable
frame_bottom_pad1 = 0.1
frame_bottom_pad2 = 0.1 / 0.9

# frame button rely variable
fb_rely_primary = (1.0 - frame_bottom_pad1) + 0.025
fb_rely_secondary = (1.0 - frame_bottom_pad2) + (0.025 / 0.9)
