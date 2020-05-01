# consolidate variables into one file

# imports
from data.variables_repo.v_config import config_width, config_height, config_font, config_font_size, \
    tooltips, dev, MyFonts

from data.variables_repo.v_geometry import main_width, main_height, main_geometry, \
    game_width, game_height, game_geometry, \
    cheatsheet_width, cheatsheet_height, cheatsheet_geometry, \
    documentation_width, documentation_height, documentation_geometry, \
    start_width, start_height, start_geometry

from data.variables_repo.v_modules import ask_again_list, \
    canvas_width, canvas_height, canvas_relx, canvas_rely, \
    frame_bottom_pad1, frame_bottom_pad2, fb_rely_primary, fb_rely_secondary, \
    scale_relwidth, scale_relheight, particle_constant, circle_constant, \
    part_radius, circum_width, spoke_width, spoke_step, platform_width, \
    color_green, color_red

from data.programconfig.main import ask_goto_start_again_bool, ask_goto_documentation_again_bool, \
    ask_radius_error_bool, ask_ang_vel_error_bool
