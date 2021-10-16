# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 20:56:43 2021

@author: Dell
"""
import matplotlib.pyplot as plt
import math
import numpy as np
import sklearn.preprocessing as skl

"""
This first simulation only deals with equally spaced linear arrays (ESLA). The elements, 
however, can be excited as you wish. 

UPDATE 11/08/2021 : RESULTS NOW CONCORD WITH THE  TEXTBOOK P.280 (300)
"""
#all the parameters below can be changed from simulation to simulation 


def ComputeAF(lam, d, alpha, n, dt, A, R_up) : 
    theta = 0.0  #we input degrees, but cos converts it to rad
    AF = [] # array factor
    while (theta < math.pi):    
        phi = 2*math.pi/lam * d * math.cos(theta) + alpha #rads
        i = 0
        AF_sum = 0.0
        tmp = 0
        while ( i < n):
            tmp  = math.cos(i * phi)
            AF_sum += A[i] * tmp  #temporarily changed to uniform excitation
            i += 1
        AF.append(AF_sum)
        theta += dt
    return AF


def ComputeF(AF, g_a, dt, R_up) : #Computes the full radiation pattern
    F  = [] # full pattern 
    i = 0.0
    while (i < math.pi):
        F[i] = AF[i] * g_a[i]
        i += dt
    return F


def PlotAF(AF, dt, R_up, unit): #Plots AF with respect to phi
    a = []
    i = 0
    while ( i < math.pi):
       a.append(i)
       i += dt
    plt.scatter(a, AF, color='green', marker='o', label='AF')
    plt.xlabel('phi(rad)')
    plt.ylabel('')
    plt.legend(loc='upper right')
    plt.text(0, 4, "Array factor")
    plt.show()
    return

def PlotF(F, dt, R_up):  #Plots the full radiation pattern
    a = []
    i = 0
    while ( i < R_up):
        a.append(i)
        i += dt
    plt.scatter(a, F, color='green', marker='o', label='F')
    plt.xlabel('phi(rad)')
    plt.legend(loc='upper right')
    plt.show()
    return 

def PrintHB(lam, n, d, alpha):  #prints the half-power beamdwidth
    HB = 0.886 * lam/(n * d * math.sin(alpha))
    print(HB*57.3) # to print in deg
    return

'''PlotHB is not completed yet '''
def PlotHB(lam, n, d): #plots HB vs angle 
    a = []
    arrHB = []
    i, HB, alpha = 0, 0, 0
    while ( i < 180):
        a.append(i)
        alpha = -2*math.pi/lam*d*math.cos(i/57.3)#input in rad
        HB = 0.886 * lam/(n * d * math.sin(alpha))#gives HF in rad
        arrHB.append(HB*57.3) #append it in deg
        i += dt
    plt.scatter(a, arrHB, color='green', marker='o', label='F')
    plt.xlabel('phi(rad)')
    plt.legend(loc='upper right')
    plt.show()
    return

"parameters"
lam = 0.33  # lambda 
d = lam/2   #distance between elments 
alpha = 3.14/4 #-2*math.pi/lam*d*math.cos(0.25*math.pi)# phase shift introduced during excitation(rad) 
#when using the scanning formula, 

n = 4  # number of elements in the array  
dt = 0.01 # step over theta variable 
A = [1.0, 1.0, 1.0, 1.0, 1.0]  # amplitude of nth element  
g_a = [0.0, 1.0, 1.0, 1.0, 0.0] # element pattern   

R_up = ( alpha + 2*math.pi/lam * d) #upper bound of visible range (phi variable)

"plotting the AF"
AF1 = ComputeAF(lam, d, alpha, n, dt, A, R_up)
PlotAF(AF1, dt, R_up, "theta") 
 
#F1 = ComputeF(AF1, g_a, dt)
#PlotF(F1, dt)

"plotting HB"
PrintHB(lam, 4, 0.15, 45)  #prints half-power beamwidth (nD >> lam)
PlotHB(lam, 4, 0.15)









