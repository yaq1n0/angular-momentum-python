# program configuration functions

# imports


# defining functions
# set boolean values to False
def setRadiusFalse():
    with open('data/myvariables/bool_radius.py', 'w') as myfile:
        myfile.write('ask_radius_error_bool = False\n')


def setAngVelFalse():
    with open('data/myvariables/bool_angvel.py', 'w') as myfile:
        myfile.write('ask_ang_vel_error_bool = False\n')


def setGotoStartFalse():
    with open('data/myvariables/bool_start.py', 'w') as myfile:
        myfile.write('ask_goto_start_again_bool = False\n')


def setGotoDocFalse():
    with open('data/myvariables/bool_doc.py', 'w') as myfile:
        myfile.write('ask_goto_documentation_again_bool = False\n')


# set boolean values to True
def setRadiusTrue():
    with open('data/myvariables/bool_radius.py', 'w') as myfile:
        myfile.write('ask_radius_error_bool = True\n')


def setAngVelTrue():
    with open('data/myvariables/bool_angvel.py', 'w') as myfile:
        myfile.write('ask_ang_vel_error_bool = True\n')


def setGotoStartTrue():
    with open('data/myvariables/bool_start.py', 'w') as myfile:
        myfile.write('ask_goto_start_again_bool = True\n')


def setGotoDocTrue():
    with open('data/myvariables/bool_doc.py', 'w') as myfile:
        myfile.write('ask_goto_documentation_again_bool = True\n')


# set all boolean values back to True (default)
def setAllTrue():
    setRadiusTrue()
    setAngVelTrue()
    setGotoStartTrue()
    setGotoDocTrue()
