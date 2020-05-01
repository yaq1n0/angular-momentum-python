# program configuration functions

# imports


# defining functions
def setRadiusFalse():
    with open('data/programconfig/bool_radius.py', 'w') as myfile:
        myfile.write('ask_radius_error_bool = False\n')


def setAngVelFalse():
    with open('data/programconfig/bool_angvel.py', 'w') as myfile:
        myfile.write('ask_ang_vel_error_bool = False\n')


def setGotoStartFalse():
    with open('data/programconfig/bool_start.py', 'w') as myfile:
        myfile.write('ask_goto_start_again_bool = False\n')


def setGotoDocFalse():
    with open('data/programconfig/bool_doc.py', 'w') as myfile:
        myfile.write('ask_goto_documentation_again_bool = False\n')


def setRadiusTrue():
    with open('data/programconfig/bool_radius.py', 'w') as myfile:
        myfile.write('ask_radius_error_bool = True\n')


def setAngVelTrue():
    with open('data/programconfig/bool_angvel.py', 'w') as myfile:
        myfile.write('ask_ang_vel_error_bool = True\n')


def setGotoStartTrue():
    with open('data/programconfig/bool_start.py', 'w') as myfile:
        myfile.write('ask_goto_start_again_bool = True\n')


def setGotoDocTrue():
    with open('data/programconfig/bool_doc.py', 'w') as myfile:
        myfile.write('ask_goto_documentation_again_bool = True\n')


def setAllTrue():
    setRadiusTrue()
    setAngVelTrue()
    setGotoStartTrue()
    setGotoDocTrue()
