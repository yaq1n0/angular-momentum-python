# for all components

# imports
from data.myvariables.userconfig import font as config_font
from data.myvariables.userconfig import font_size as config_font_size

ask_again_list = ['Do Not Ask Again?', 'Do you want to disable further alerts like this?']

MyFonts = {
    'Default': (config_font, config_font_size),
    'DefaultBold': (config_font, config_font_size, 'bold'),
    'Small': (config_font, int(round(config_font_size * 0.75, 0))),
    'SmallBold': (config_font, int(round(config_font_size * 0.75, 0)), 'bold'),
    'Large': (config_font, int(round(config_font_size * 1.25, 0))),
    'LargeBold': (config_font, int(round(config_font_size * 1.25, 0)), 'bold'),
    'ExtraLarge': (config_font, int(round(config_font_size * 1.50, 0))),
    'ExtraLargeBold': (config_font, int(round(config_font_size * 1.50, 0)), 'bold')
}
