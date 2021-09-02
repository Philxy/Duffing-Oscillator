"""
Dieses kleine Programm animiert das  (x,v)-Phasenraumdiagramm des Duffing-Oszillators.

Dazu wird die  2d GrafikLibrary PyGame benutzt die man vor dem Ausführen ggf.
vorher mit pip installieren muss.

Im Fenster ist auf der horizontalen ist die Auslenkung x und auf der vertikalen
die Geschw. v aufgetragen.

Amerkungen:
Bei der Ausführung des Programms kann es leider sein,
dass die Geschwindigkeit der Animation von der Hardware abhängt weil die Darstellung
und Berechnung gleichzeitig geschehen. Falls zu langsamoder zu schnell einfach
an der Variable "SPEED" rumspielen oder Schrittweite "H"
ändern.

Das Programm ist eigentlich für viele Massenpunkte und beliebige Kräfte ausgelegt
funktioniert aber natürlich auch für eine eindimensionale Bewegung.
"""
import numpy as np
import pygame

H = 0.005
t = 0
SPEED = 5


# Berechne Ort und Geschw. im nächten Zeitschritt mit Runge-Kutta-2nd
def next_step(x, y, vx, vy, t, m, F):
    k2_x = H * (vx + H/2 * F(x, y, vx, vy, m, t)[0])
    k1_vx = H * F(x, y, vx, vy, m, t)[0]
    k2_vx = H * F(x, y, vx + k1_vx/2, vy, m, t + H/2)[0]
    x_n = x + k2_x
    vx_n = vx + k2_vx
    k2_y = H * (vy + H/2 * F(x, y, vx, vy, m, t)[1])
    k1_vy = H * F(x, y, vx, vy, m, t)[1]
    k2_vy = H * F(x, y, vx, vy + k1_vy/2, m, t + H/2)[1]
    y_n = y + k2_y
    vy_n = vy + k2_vy
    return [x_n, y_n, vx_n, vy_n, t + H]


# Antreibende Kraft
def F(x, y, vx, vy, m, t):
    return [-x*x*x + x - 0.1*vx + 50*np.sin(1.5*t), 0]


class Mass:
    def __init__(self, x, y, vx, vy, m, radius):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.m = m
        self.radius = radius

        # update velocity and position
    def update(self, time):
        calc = next_step(self.x, self.y, self.vx, self.vy, time, self.m, F)
        self.x = calc[0]
        self.y = calc[1]
        self.vx = calc[2]
        self.vy = calc[3]


pygame.init()
frame_size = 500  # windowsize
size = 150  # bereich der simulation
scaling = frame_size/size # skalierungsfaktor zwischen und simulation

objects = []  # massen des oszillators

m = Mass(0, 0, 0, 0, 1, 2)
objects.append(m)

screen = pygame.display.set_mode([frame_size, frame_size])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((25, 25, 112))
    pygame.draw.circle(screen, (255, 255, 0), (int(frame_size/2), int(frame_size/2)), 1)

    for m in objects:
        m.update(t)

    t += H

    for m in objects:
        pygame.draw.circle(screen, (135,206,235), (int(10*m.x * scaling + frame_size/2), int((2*m.vx * scaling) + frame_size/2)), int(m.radius * scaling))

    pygame.time.wait(SPEED)
    pygame.display.flip()
pygame.quit()
