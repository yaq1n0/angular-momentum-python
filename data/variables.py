# project variables

# imports
from config import width as config_width
from config import height as config_height
from config import font as config_font
from config import font_size as config_font_size
from config import enable_developer as dev

# validation checks for config
if type(config_width) != int:
    print "Please use an integer value for width"
if type(config_height) != int:
    print "please use an integer value for height"
if type(config_font) != str:
    print "please use a string for font"
if type(config_font_size) != int:
    print "please use an integer value for font_size"
if type(dev) != bool:
    print 'please use either "True" or "False" boolean values'

# defining colors
# grayscale
colors = ["#FFFFFF",
          "#D3D3D3",
          "#A9A9A9",
          "#696969",
          "#000000"
          ]

# special colors
color_green = "#77dd77"
color_red = "#FF6961"

# frame background and foreground
fbg = colors[3]
ffg = colors[0]

# creating my font using config_font and config_font_size
MyFont = (config_font, config_font_size)

# creating geometry values
# main geometry
main_width = config_width
main_height = config_height
main_geometry = str(main_width) + "x" + str(main_height)

# game geometry (set to the same as main)
game_width = main_width
game_height = main_height
game_geometry = main_geometry

# cheatsheet geometry
cheatsheet_width = 1280
cheatsheet_height = 1120
cheatsheet_geometry = str(cheatsheet_width) + "x" + str(cheatsheet_height)

# documentation geometry
documentation_width = 1280
documentation_height = 720
documentation_geometry = str(documentation_width) + "x" + str(documentation_height)

# start geometry
start_height = main_height
start_width = start_height / 2
start_geometry = str(start_width) + "x" + str(start_height)

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

# for myclasses
# scale relative sizing
scale_relwidth = 0.10
scale_relheight = 0.08

# for func1 (calculations)
# moment of inertia constants
particle_constant = 1.0
circle_constant = 0.5

# for func2 (animations)
# orbiting particle vars
part_radius = 20.0

# rotating circle vars
circum_width = 5.0
spoke_width = 5.0
spoke_number = 4
spoke_step = 360.0 / spoke_number

# moving platform vars
platform_width = 2.0
