# variables imported form config

# imports
from config import width as config_width
from config import height as config_height
from config import font as config_font
from config import font_size as config_font_size
from config import enable_developer as dev
from config import enable_tooltips as tooltips

# default config error states
c_error = False
c_error_text = ''

# validation checks for config
if type(config_width) != int:
    c_error = True
    c_error_text = "Please use an integer value for width"
if type(config_height) != int:
    c_error = True
    c_error_text = "please use an integer value for height"
if type(config_font) != str:
    c_error = True
    c_error_text = "please use a string for font"
if type(config_font_size) != int:
    c_error = True
    c_error_text = "please use an integer value for font_size"
if type(dev) != bool:
    c_error = True
    c_error_text = 'please use either "True" or "False" boolean values'
if type(tooltips) != bool:
    c_error = True
    c_error_text = 'please use either "True" or "False" boolean values'

# setting default developer settings (for the Supreme Leader)
dev_settings = True
if dev and dev_settings:
    config_width = 1280
    config_height = 720
    config_font = 'Arial'
    config_font_size = 12
    tooltips = True

# creating my font using config_font and config_font_size
MyFont = (config_font, config_font_size)
MyFontB = (config_font, config_font_size, 'bold')

# different sizes
MyFontS = (config_font, int(round(config_font_size * 0.75, 0)))
MyFontL = (config_font, int(round(config_font_size * 1.25, 0)))
MyFontXL = (config_font, int(round(config_font_size * 1.50, 0)))

# bold variations
MyFontSB = (config_font, int(round(config_font_size * 0.75, 0)), 'bold')
MyFontLB = (config_font, int(round(config_font_size * 1.25, 0)), 'bold')
MyFontXLB = (config_font, int(round(config_font_size * 1.50, 0)), 'bold')
