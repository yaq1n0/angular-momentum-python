# for main component

# imports
from v_geometry import main_width, main_height

# creating canvas vars
canvas_relx = 0.33
canvas_rely = 0.20
canvas_width = 0.34 * main_width
canvas_height = 0.34 * (16.0 / 9.0) * main_height
# creating frame padding
frame_bottom_pad1 = 0.1
frame_bottom_pad2 = 0.1 / 0.9
# creating frame button relative positioning based on frame bottom padding
fb_rely_primary = (1.0 - frame_bottom_pad1) + 0.025
fb_rely_secondary = (1.0 - frame_bottom_pad2) + (0.025 / 0.9)
