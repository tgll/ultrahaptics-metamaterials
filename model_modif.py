#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cmath
import math
import matplotlib.pyplot as plt
import numpy as np


'''
This code models and references symbols from the paper 'Experimental 
Realization of Full Control of Reflected Waves with Subwavelength Acoustic 
Metasurfaces' by Yong Li et al.

The symbols t, d, l and w refer to the dimensions of the labyrinthian passage,
which is subfigure C in Figure 1:
	t: Outer width
	d: Channel width
	l: Channel length
	w: Bar width

All measurements are in metres.
'''

class AcousticModeler(object):
	def __init__(self, freq, t, d, l, w, simpsonIterations=None, sumIterations=None):
		if simpsonIterations == None:
			simpsonIterations = 100

		if sumIterations == None:
			sumIterations = 1000

		self.t = float(t)
		self.d = float(d)
		self.l = float(l)
		self.w = float(w)
		self.freq = float(freq)
		self.simpsonIterations = simpsonIterations
		self.sumIterations = sumIterations

		wlen = 343.0 / self.freq
		self.K0 = (2.0 * math.pi) / wlen

		self.computeMatrix()

	#============ page 4 / left side ===========================================

	# Top of page 4 left
	def Kyn(self, n):
		return (float(n) * math.pi) / (self.l + self.d)

	# Top of page 4 left
	def Kxn(self, n):
		return cmath.sqrt((self.K0**2) - (self.Kyn(n)**2))

	# Equation 11
	def deltaY(self, y, n):
		delta = 1.0 if (n == 0) else 0
		return math.sqrt(2.0 - delta) * math.cos(self.Kyn(n) * (y - self.t))

	# Code from https://stackoverflow.com/questions/16001157/simpsons-rule-in-python
	def simpsonIntegration(self, f, a, b, n, kyn):
		h = (b - a) / n
		k = 0.0
		x = a + h
		
		for i in range(1, n//2 + 1):
			k += 4.0 * f(x, kyn)
			x += 2.0 * h

		x = a + 2.0 * h
		for i in range(1, n//2):
			k += 2.0 * f(x, kyn)
			x += 2.0 * h
		
		return (h / 3.0) * (f(a, kyn) + f(b, kyn) + k)

	def computeAlphaBeta(self, iterations):
		alpha = 0.0
		beta = 0.0
		
		for n in range(self.sumIterations):
			# Equation 15
			phi1 = (1.0 / self.d) * self.simpsonIntegration(self.deltaY, self.t,          self.t + self.d,          self.simpsonIterations, n)
			phi2 = (1.0 / self.d) * self.simpsonIntegration(self.deltaY, self.t + self.l, self.t + self.d + self.l, self.simpsonIterations, n)

			# Top of page 4
			Kxn = cmath.sqrt((self.K0**2) - (self.Kyn(n)**2))

			# Equation 14
			exp =  1j * Kxn * self.d
			leftFraction = (self.K0 * self.d) /\
					       (Kxn * (self.l + self.d))

			addedAlpha = (1.0 + cmath.exp(2.0 * exp)) /\
						 (1.0 - cmath.exp(2.0 * exp))

			addedBeta  = (2.0 * cmath.exp(exp))       /\
				         (1.0 - cmath.exp(2.0 * exp))

			alpha += addedAlpha * leftFraction * phi1 * phi1
			beta  += addedBeta  * leftFraction * phi1 * phi2

		return alpha, beta

	def computeMatrix(self):
		alpha, beta = self.computeAlphaBeta(self.sumIterations)

		# The rest is equation 13.
		exp = 1j * self.K0 * self.w

		mA = ((beta**2) - (alpha**2) + 1.0) /\
			  (2.0 * beta)
		mB =-(((beta**2) - (alpha + 1.0)**2)  /\
		      (2.0 * beta)) * cmath.exp(-exp)
		mC = (((beta**2) -((alpha - 1.0)**2)) /\
			  (2.0 * beta)) * cmath.exp(exp)
		mD = -mA

		self.matrix = np.matrix([[mA, mB], [mC, mD]])

	def getMatrix(self):
		return self.matrix

	#============ page 4 / right side ==========================================
	
	# Top of page 4 right
	def Kpyn(self, n):
		return (float(n) * math.pi) / (self.l + self.d + self.t)

	# Top of page 4 right
	def Kpxn(self, n):
		return cmath.sqrt((self.K0**2) - (self.Kyn(n)**2))

	#===========================================================================
def main():
    #brick n1
	freq = 3430.0 #fixed 
	ax = 0.01250 #fixed 
	ay = 0.01250 #fixed
	d = 0.0031667 #variable
	t = 0.004 #variable
	w = 0.001 #fixed
	numBars = 2 #variable (total number of bars - 1)
	l = ay - (2.0*t) - d
	
	model = AcousticModeler(freq, t, d, l, w)
	M = model.getMatrix()**numBars
	C = (M * np.matrix([[0],[1]]))[0]
	result = math.atan2(C.imag, C.real) % (2.0 * math.pi)

  #in radians
	print ("delay in radians :")
	print (result) 
  #in degrees
	print("delay in degrees :")
	print (math.degrees(result))

if __name__ == "__main__":
    main()
