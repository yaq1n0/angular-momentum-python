# variables imported form config

# imports
from data.userconfig import width as config_width
from data.userconfig import height as config_height
from data.userconfig import font as config_font
from data.userconfig import font_size as config_font_size
from data.userconfig import enable_tooltips as tooltips
from data.userconfig import enable_developer as dev

# MyFonts dictionary
MyFonts = {'Default': (config_font, config_font_size),
           'DefaultBold': (config_font, config_font_size, 'bold'),
           'Small': (config_font, int(round(config_font_size * 0.75, 0))),
           'SmallBold': (config_font, int(round(config_font_size * 0.75, 0)), 'bold'),
           'Large': (config_font, int(round(config_font_size * 1.25, 0))),
           'LargeBold': (config_font, int(round(config_font_size * 1.25, 0)), 'bold'),
           'ExtraLarge': (config_font, int(round(config_font_size * 1.50, 0))),
           'ExtraLargeBold': (config_font, int(round(config_font_size * 1.50, 0)), 'bold')
           }
