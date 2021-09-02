import utility
import numpy as np
import matplotlib.pyplot as plt


solution = utility.RK2(0,0, 1.1)
x_values = []
v_values = []

dt = 2*np.pi/utility.OMEGA
dt_0 = 20
index = int(dt/utility.H)
i = dt_0*index

while i < len(solution[1]):
    x_values.append(solution[1][i])
    v_values.append(solution[2][i])
    i+=index


plt.plot(solution[1], solution[2], linewidth=0.5, color="0")
plt.plot(x_values, v_values, ".")




plt.xlabel("x")
plt.ylabel("v")
plt.title(r"$t_n= $" + str(dt_0)+ r"$T$" +"$,\ldots,$"+ str(int(utility.t_max/(np.pi*2/utility.OMEGA)))+"$T$  "+   "   $\omega = $" + str(utility.OMEGA) + r"   $\alpha = $"+ str(utility.ALPHA) + r"   $\beta = $"+ str(utility.BETA) + "   $A= $" + str(utility.A) +"   $\gamma = $"  + str(utility.GAMMA))
plt.show()
