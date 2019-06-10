#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This code models and references symbols from the paper 'Experimental 
Realization of Full Control of Reflected Waves with Subwavelength Acoustic 
Metasurfaces' by Yong Li et al.

The symbols t, d, l and w refer to the dimensions of the labyrinthian passage,
which is subfigure C in Figure 1:
	t: Outer width
	d: Channel width
	l: Bar length
	w: Bar width

All measurements are in metres.

Tallulah GILLIARD 
t.gilliard@gmail.com
Sussex University
'''
import cmath
import math
import numpy as np

#==============================================================================

#======== VALUES <
freq = 3430. # article [1]
wlen = 343. / freq
K0 = (2. * math.pi) / wlen

ax = (wlen / 8.)
ay = (wlen / 8.)
w = .001 # 1mm
t = 0.0014 # VARIABLE BRIQUE 1
numBars = 5. # VARIABLE BRIQUE 1
d = (ax/numBars) - w
l = ay - (2.*t) - d
#======== VALUES >

#==============================================================================
#https://stackoverflow.com/questions/16001157/simpsons-rule-in-python
def SimpsonIntegration(integrand,lower,upper,*args):    
    panels = 100000 #iterations
    limits = [lower, upper] #interval
    h = ( limits[1] - limits[0] ) / (2 * panels)
    n = (2 * panels) + 1
    x = np.linspace(limits[0],limits[1],n)
    y = integrand(x,*args)

    I = 0
    start = -2
    for looper in range(0,panels):
        start += 2 #step of two
        counter = 0
        for looper in range(start, start+3):
            counter += 1
            if (counter ==1 or counter == 3):
                I += ((h/3) * y[looper])
            else:
                I += ((h/3) * 4 * y[looper])
    return I
#==============================================================================
def Kyn():
    # LOOP (begening)
    n = A # based on A loops
    Kyn = (n * np.pi) / (l + d)
    return Kyn

#==============================================================================
def phi(x,a,b):

    restemp = ((K0) ** 2 ) - ((Kyn()) ** 2)
    a = A
    b = t
    
    #======== delta <
    if a == 0:
        delta=math.sqrt(2)
    else:
        delta = 1
    #======== delta >
    
    
    #======== PHI formula (11) <
    if restemp > 0: # positive case
        restemp = restemp
        a = math.sqrt(restemp)
        finalres = delta*np.cos(a * (x - b))
    else: # negative case
        restemp = - restemp
        a = math.sqrt(restemp)
        e1 = (np.exp(-(a * (x - b))))
        e2 = (np.exp(+(a * (x - b))))
        finalres = delta*((e1 + e2) /2)
    restemp = finalres
    #======== PHI formula (11) >
    
    return finalres #np.cos(a * x) + b

#==============================================================================
  
def alphabeta():
    alpha = 0.
    beta = 0.
    
    # Top of page 4
    Kxn1 = cmath.sqrt((K0**2) - (Kyn**2))
            
    # Equation 14
    exp =  1j * Kxn1 * d
    leftFraction = (K0 * d) /\
    (Kxn1 * (l + d))
    
    addedAlpha = (1. + cmath.exp(2. * exp)) /\
    (1. - cmath.exp(2. * exp))
    
    addedBeta  = (2. * cmath.exp(exp))       /\
    (1. - cmath.exp(2. * exp))
    
    alpha += addedAlpha * leftFraction * phi1 * phi1
    beta  += addedBeta  * leftFraction * phi1 * phi2
        
    return phi1,phi2

#==============================================================================

# phi1 and phi2
for A in range(0,10):
    phi1 = (1 / d) * SimpsonIntegration(phi,t,t+d,A,1) #SimpsonIntegration(f,lower,upper,a,b)   
    #print("FINAL RESULT : ",I)
    print("phi1 :", phi1)
    phi2 = (1 / d) * SimpsonIntegration(phi,t+l,t+l+d,A,1) #SimpsonIntegration(f,lower,upper,a,b)   
    #print("FINAL RESULT : ",I)
    print("phi2 :", phi2)
    



