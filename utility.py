import numpy as np

# Constants
H = 0.001
t_max = 70
t_0 = 0
ALPHA = -1
BETA = 1
GAMMA = 0.25
OMEGA = 1.4
A = 0.2


# DuffingPotenital
def potential(x):
    return ALPHA / 2 * x * x + BETA / 4 * x * x * x * x


# Gibt Array mit allen x und V(x) Werten des DuffingPotenitials aus
def init_Potential(x_min, x_max):
    x = x_min
    X = []
    pot = []
    while x < x_max:
        X.append(x)
        pot.append(potential(x))
        x += H
    return [X, pot]


# Antreibende Kraft
def F(t):
    return A * np.cos(OMEGA * t)


# Löst die DGl des DuffingOszillators und
# gibt Array mit Geschw. und entsprechender Auslenkung  zurück
def RK2(x_0, v_0, amplitude):
    x = x_0
    v = v_0
    t = t_0
    v_n = v
    x_n = x
    X = []
    V = []
    time = []

    def v_dot(T, x, v):
        return amplitude * np.cos(OMEGA * T) - GAMMA * v - ALPHA * x - BETA * x * x * x

    def force(t):
        return amplitude * np.cos(OMEGA * t)

    while t < t_max:
        time.append(t)
        X.append(x)
        V.append(v)
        k1_x = H * v
        k2_x = H * (v + H / 2 * (force(t) - GAMMA * v - ALPHA * x - BETA * x * x * x))
        k1_v = H * (force(t) - GAMMA * v - ALPHA * x - BETA * x * x * x)
        k2_v = H * v_dot(t + H / 2, x + k1_x / 2, v + k1_v / 2)
        x_n = x + k2_x
        v_n = v + k2_v
        x = x_n
        v = v_n
        t += H
    return [time, X, V]
