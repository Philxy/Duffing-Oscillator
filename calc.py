"""
Berechnung von Zeit-Auslenkung-Diagrammen oder Phasenraumtrajektorien
des Duffing DuffingOszillators
"""
import numpy as np
import matplotlib.pyplot as plt
import utility

solution = utility.RK2(1, 0, 0.2)

plt.xlabel("t")
plt.ylabel("x")
plt.title("$\omega = $" + str(utility.OMEGA) + r"   $\alpha = $"+ str(utility.ALPHA) + r"   $\beta = $"+ str(utility.BETA) + "   $A= $" + str(utility.A) +"   $\gamma = $"  + str(utility.GAMMA))
plt.plot(solution[0], solution[1])
plt.show()
