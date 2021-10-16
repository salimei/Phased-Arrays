# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 11:05:18 2020

@author: Salim : )
"""
import matplotlib.pyplot as plt
import numpy as np
import math 
# The ground station is defined as the ground point 

# POWER AT RECEIVER AS A FUNCTION OF DISTANCE (IDEAL SCENARIO)
a, b, b_best = [], [], []
h = 10              # the step
y, x, y_best = 0, 0, 0         # y is Pr and x is the distance


#Parameters to play with, no need to fiddle with the rest of the code
max_distance = 100 # max distance between the rocket and the receiver
P_t = 20              # Power at transmitter (Dbm)  (22 in theory)
VSWR_TX = 2
VSWR_RX = 2
D_t = 1           #  isotropic directivity of the transmitting antenna (Dbi)
D_r = 1            #  isotropic directivity of the receiving antenna (Dbi)
wavelength = 0.333  # wavelength of transmission (m)

#  Do not touch 
Mismatch_loss_TX = -10*math.log10(1 - ((VSWR_TX - 1)/(VSWR_TX+1))**2)  #mismatch at Tx antenna
print("Mismatch loss (Db) TX: {}".format(Mismatch_loss_TX))
Mismatch_loss_RX = -10*math.log10(1 - ((VSWR_RX - 1)/(VSWR_RX+1))**2)  #mismatch at RX antenna
while x <= max_distance + h: 
    #At each distance point, this code will caculate the Power at the receiver,
    #then it will store it in a list.
    a.append(x)
    b.append(y)
    b_best.append(y_best)
    
    x = x + h
    y = P_t + D_t + D_r + 20*math.log10(wavelength/ (4*math.pi *x)) - Mismatch_loss_TX - Mismatch_loss_RX
    y_best = 20 + 2 + 2 + 20*math.log10(wavelength/ (4*math.pi *x))
     
# experimental results of integration testing with Zheng and Marco, May 9th 2021    
lat_gps = [45.5055389, 45.5055730, 45.5055333, 45.5054918, 45.5054743, 45.5054369, 
           45.5054190, 45.5053900, 45.5053680, 45.5053298] 
lon_gps = [-73.5806062, -73.5805655, -73.5804518, -73.5803609, -73.5803144, -73.5801931,
           -73.5801533, -73.5800835, -73.5800495, -73.5799189]   
radius = 6367.371 # radius earth at ground level at rutherford field    
lat_us, lon_us = 45.5052543, -73.5796006
d_gps = []
n, temp = 0, 0
while n < 10:
    temp1 = math.sin(lon_us) * math.sin(lon_gps[n]) * math.cos(lat_us-lat_gps[n])
    temp2 = math.cos(lon_us)*math.cos(lon_gps[n])
    temp = temp1 + temp2
    d_gps.append(math.sqrt(2*(radius**2) -2*(radius**2) * temp ))
    n += 1
# RS: received power as displayed by the XCTU     
RS = [-76, -68, -67, -64, -63, -58, -62, -56, -53, -40]

#This code displays the results 
plt.scatter(a, b_best, color='green', marker='o', label='Power at receiver as a function of distance (best case)')
plt.scatter(a, b, color='red', marker='o', label='Power at receiver as a function of distance (worst case)')
plt.scatter(d_gps, RS, color = 'blue', marker='x', label='Measured Received Power (experimental)')
plt.xlabel('distance(m)')
plt.ylabel('Power at receiver (dBm)')
plt.legend(loc='upper right')
#plt.text(6000, -20, "Directivity transmitting antenna: {}".format(D_t))
#plt.text(6000, -30, "Directivity receiving antenna: {}".format(D_r))
#plt.text(6000, -40,  "Power at 13km: {}".format(int(b[int(max_distance/h)])))
plt.show()

print(b[int(max_distance/h)])
print(b[10])

#Fresnel Zone (a fancy way to say multipathing )

#The goal is to keep the first Fresnel zone (an ellipse with foci Rx and Tx)
#free of any object. The following equation gives the radius of the first 
#Fresnel zone with respect to the distance between Tx and Rx AND the frequency.

F1 = 0 #Radius of the first Fresnel zone (km)
c = 8.656 # constant, look wiki for derivation
D = 0; # distance from Rx to Tx (m)
f_g = 0.9 # frequency (Ghz)

#NOTICE: I used the same variable names above and below. Careful, this 
# means the value of the variable above will be overwritten at run time.

a, b = [], []
h = 0.01              # the step
max_distance = 9 # max distance between the rocket and the receiver (km)
while D <= max_distance + h: 
    #At each distance point, this code will caculate the Power at the receiver,
    #then it will store it in a list.
    a.append(D)
    b.append(F1)
    
    D = D + h
    F1 = c * math.sqrt(D/f_g)   
               
#This code displays the results 
plt.scatter(a, b, color='blue', marker='x', label='Radius of first Fresnel zone as a function of distance')
plt.xlabel('distance(km)')
plt.ylabel('Radius (m)')
plt.legend(loc='lower right')
plt.show()

print(b[int(max_distance/h)])
print(b[10])











