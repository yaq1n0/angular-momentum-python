# Rotational Dynamics Py
This was a group coursework from my Engineering Foundation Year at University of Southampton's Malaysia Campus. 
It was a software engineering group project where the goal was to create a python app using tkinter as an educational aide to a certain mechanics topic. 

We chose to create a rotational dyamics (angular momentum and inertia) calculator and visualizer. 
I was the only one with any real programming experience, so 99% of the code here is mine, albeit a much younger and less skilled version of myself. 

However, despite my lack of experience at the time, I saw the potential of repurposing the bulk of the GUI code for this app into a desktop app template that I can use in the future for rapic prototyping. 
This app was made in python2, which was already deprecated at the time, because of an outdated coursework spec. And I haven't felt the need to update it. 
If you want to run it, use python 2.7 and tkinter. It should work, though you might also have to fix some minor bugs before it runs, entropy is real. 

# Desktop App Template
This project was later forked into [desktop-app-template](https://github.com/yaq1n0/desktop-app-template). 
Which has python 3 support and will be carried over into the future :)

# How to get this ancient thing to work :p
Tested on a Ubuntu 22 VM because I didn't want to have to install python 2 onto any of my physical machines. 
<br>As always, start with. 
<br>```sudo apt-get update -y; sudo apt-get upgrade```

### install python 2
```sudo apt-get install python2```

### install python-tk (for python2)
```sudo apt-get install python-tk```

### install pip for python 2
``` wget https://bootstrap.pypa.io/pip/2.7/get-pip.py ```
``` python2 get-pip.py ```

### use pip to install pillow 
``` python2 -m pip install Pillow ```
