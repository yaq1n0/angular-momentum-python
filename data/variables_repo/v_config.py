# variables imported form config

# imports
from config import width as config_width
from config import height as config_height
from config import font as config_font
from config import font_size as config_font_size
from config import enable_developer as dev
from config import enable_tooltips as tooltips

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

# creating my font using config_font and config_font_size
MyFont = (config_font, config_font_size)
