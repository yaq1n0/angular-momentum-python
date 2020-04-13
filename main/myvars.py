
# contains all project variables

# defining colors
colors = ["#FFFFFF",
          "#D3D3D3",
          "#A9A9A9",
          "#696969",
          "#000000"
          ]

color_green = "#77dd77"
color_red = "#FF6961"

fbg = colors[3]
ffg = colors[0]

# root geometry
root_width = 1280
root_height = 720
root_geometry = str(root_width) + "x" + str(root_height)

# start geometry
start_width = 360
start_height = 720
start_geometry = str(start_width) + "x" + str(start_height)

# cheatsheet geometry
cheatsheet_width = 850
cheatsheet_height = 750
cheatsheet_geometry = str(cheatsheet_width) + "x" + str(cheatsheet_height)

# frame bottom padding variable
frame_bottom_pad1 = 0.1
frame_bottom_pad2 = 0.1 / 0.9

# frame button rely variable
fb_rely_primary = (1.0 - frame_bottom_pad1) + 0.025
fb_rely_secondary = (1.0 - frame_bottom_pad2) + (0.025 / 0.9)

# scale rel sizing
scale_relwidth = 0.10
scale_relheight = 0.08

# moment of inertia constants
particle_constant = 1.0
circle_constant = 0.5

# canvas size vars
canvas_window_ratio = 0.25
canvas_width = canvas_height = root_width * canvas_window_ratio

# canvas placing vars
frame_height = root_height * (0.9 ** 2)
canvas_relx = 1.5 * canvas_window_ratio
canvas_rely = ((frame_height - canvas_height) / 2) / frame_height

# orbiting particle vars
part_radius = 20.0

# rotating circle vars
circum_width = 5.0
spoke_width = 5.0
spoke_number = 4
spoke_step = 360.0 / spoke_number

# moving platform vars
platform_width = 2.0
