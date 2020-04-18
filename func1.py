# calculation functions

# imports
from math import pi, sin, cos
from myvars import spoke_width


# finding moment of inertia
def Moment_Inertia(constant, radius, mass):
    return float(constant) * float(mass) * (float(radius) ** 2.0)


# finding angular momentum
def Angular_Momentum(inertia, omega):
    return float(inertia) * float(omega)


# finding linear momentum
def Linear_Momentum(mass, velocity):
    return float(mass) * float(velocity)


# finding rotational kinetic energy
def Rotational_Kinetic_Energy(inertia, omega):
    return 0.5 * float(inertia) * (float(omega) ** 2.0)


# finding linear kinetic energy
def Linear_Kinetic_Energy(mass, velocity):
    return 0.5 * float(mass) * (float(velocity) ** 2.0)


# finding total kinetic energy
def TKE(rotational, linear):
    return float(rotational) + float(linear)


# convert degrees to radians
def dtr(theta):
    tmpvar = pi / 180.0
    return float(theta) * float(tmpvar)


# convert angular velocity to frequency
def rtf(rad):
    tmpvar = 2.0 * pi
    return float(rad) / float(tmpvar)


# convert frequency to angular_velocity
def ftr(freq):
    tmpvar = 2.0 * pi
    return float(tmpvar) * float(freq)


# convert angular velocity into linear velocity
def atl(ang_vel, radius):
    return float(ang_vel) * float(radius)


# line at theta degrees from x_pos, y_pos to x, y (for animate_rotating_circle)
def ttl(canvas, x_pos, y_pos, radius, theta):
    x = x_pos + (float(radius) * sin(dtr(theta)))
    y = y_pos + (float(-radius) * cos(dtr(theta)))
    return canvas.create_line(x_pos, y_pos, x, y, width=spoke_width)
