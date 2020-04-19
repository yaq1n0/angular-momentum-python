# calculation functions


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
