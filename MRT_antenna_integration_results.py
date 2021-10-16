# -*- coding: utf-8 -*-
"""
Created on Mon May 10 11:59:00 2021

@author: Dell
"""
import numpy as np
import matplotlib.pyplot as plt

# recall :  P_r = P_t + D_t + D_r + 20*log10(lambda/(4*pi*d))
#     P_r - P_t = c + D_t,  where c = D_r +  20*log10(lambda/(4*pi*d))

p = 3.1415

#plot A 
# to get positive D_t, I did 85-RSSI

#theta = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330] #deg
theta = [0, p/6, 2*p/6, 3*p/6, 4*p/6, 5*p/6, 6*p/6, 7*p/6, 8*p/6, 9*p/6, 10*p/6, 11*p/6, 2*p]
r = [4, 14, 14, 9, 9, 9, 4, 16, 14, 10, 4, 5, 4]


ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(17)
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.set_yticklabels([])
plt.text(0, 0, "Peak to Peak : 12 dBi")
ax.grid(True)

ax.set_title("Directivity vs Angle (900Mhz) ", va='bottom')
plt.show()

#plot B 
# to get positive D_t, I did 100-RSSI

theta = [0, p/6, 2*p/6, 3*p/6, 4*p/6, 5*p/6, 6*p/6, 7*p/6, 8*p/6, 9*p/6, 10*p/6, 11*p/6, 2*p]
r = [7, 6, 15, 14, 5, 7, 15, 4, 8, 15, 12, 7, 13]


ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(17)
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.set_yticklabels([])
plt.text(0, 0, "Peak to Peak : 11 dBi")
ax.grid(True)

ax.set_title("Directivity vs Angle (900Mhz) ", va='bottom')
plt.show()

#plot C-1
# to get positive D_t, I did 110-RSSI

theta = [0, p/6, 2*p/6, 3*p/6, 4*p/6, 5*p/6, 6*p/6, 7*p/6, 8*p/6, 9*p/6, 10*p/6, 11*p/6]
r = [4, 10, 12, 12, 10, 12, 18, 11, 5, 11, 7, 10]

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(20)
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.set_yticklabels([])
plt.text(0, 0, "Peak to Peak : 14 dBi")
ax.grid(True)

ax.set_title("Directivity vs Angle (900Mhz) ", va='bottom')
plt.show()

#plot C-2

theta = [0, p/6, 2*p/6, 3*p/6, 4*p/6, 5*p/6, 6*p/6, 7*p/6, 8*p/6, 9*p/6, 10*p/6, 11*p/6]
r = [9, 1, 10, 10, 9, 5, 5, 9, 6, 10, 4, 8]

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(12)
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.set_yticklabels([])
plt.text(0, 0, "Peak to Peak : 6 dBi")
ax.grid(True)

ax.set_title("Directivity vs Angle (900Mhz) ", va='bottom')
plt.show()

#plot D 






