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
	l: Bar length
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

		self.computeMatrix1()

	#============ page 4 / left side ===========================================

	# Top of page 4 left
	def Kyn(self, n):
		return (float(n) * math.pi) / (self.l + self.d)

	# Top of page 4 left
	def Kxn(self, n):
		return cmath.sqrt((self.K0**2) - (self.Kyn(n)**2))

	# Equation 11
	def phiY(self, y, n):
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
			phi1 = (1.0 / self.d) * self.simpsonIntegration(self.phiY, self.t,          self.t + self.d,          self.simpsonIterations, n)
			phi2 = (1.0 / self.d) * self.simpsonIntegration(self.phiY, self.t + self.l, self.t + self.d + self.l, self.simpsonIterations, n)

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

	def computeMatrix1(self):
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

		self.matrix1 = np.matrix1([[mA, mB], [mC, mD]])

	def getMatrix1(self):
		return self.matrix1

	#============ page 4 / right side ==========================================
	
	# Top of page 4 right
	def Kynp(self, n):
		return (float(n) * math.pi) / (self.l + self.d + self.t)

	# Top of page 4 right
	def Kxnp(self, n):
		return cmath.sqrt((self.k**2) - (self.Kynp(n)**2)) # c est quoi k ??? self.k

	# Equation 19
	def psiY(self, y, n):
		delta = 1.0 if (n == 0) else 0
		return math.sqrt(2.0 - delta) * math.cos(self.Kynp(n) * y) # ??? whats y

	def computeAlphaBetaPrim(self, iterations): #not sure for this fuction
		alpha = 0.0
		beta = 0.0
		
		for n in range(self.sumIterations):
			# Equation ??? where is psi prime
			psip = 

			sumprime += (self.K0 / Kxnp) * ((pship)**2)
			
			alphap = (ay / d) + sumprime
			betap = (ay / d) + sumprime 

		return alphap, betap

	def computeMatrix2(self):
		alphap, betap = self.computeAlphaBetaPrim(self.sumIterations)

		# The rest is equation 13.
		exp = 1j * self.K0 * self.w

		mE = (1 - (betap / 2)) * cmath.exp(-exp)
		mF = (betap / 2) * cmath.exp(-exp)
		mG = 1 + (alphap / 2)
		mH = - (d / 2)
		self.matrix2 = np.matrix2([[mE, mF], [mG, mH]])

	def getMatrix2(self):
		return self.matrix2

	# Equation 23
	def R0(self):
		upper = (1 - alpha) * m_11 + (1 + alpha) * cmath.exp(-exp) * m_21
		lower = (1 - alpha) * m_12 + (1 + alpha) * cmath.exp(-exp) * m_22
		return ( upper / lower )

	# Matrix 24
	def M(self):
		#self.matrix2 * matrix (16)
		return M


	#===========================================================================
def main():

	# PARAMETERS
	freq = 3430.0 #fixed 
	ax = 0.01250 #fixed 
	ay = 0.01250 #fixed
	d = 0.0031667 #variable
	t = 0.004 #variable
	w = 0.001 #fixed
	numBars = 2 #variable (total number of bars - 1)
	l = ay - (2.0*t) - d
	
	# code for "single" through brick
	model_single = AcousticModeler(freq, t, d, l, w)
	M1 = model_single.getMatrix1()**numBars
	C = (M1 * np.matrix1([[0],[1]]))[0] # matrix (12)
	result_single = math.atan2(C.imag, C.real) % (2.0 * math.pi)

	# code for "return" through brick  
	model_return = AcousticModeler(freq, t, d, l, w)
	M2 = model_return.getMatrix2()**numBars
	A = (M2 * np.matrix2([[0],[1]]))[0] # matrix (20)
	result_return = math.atan2(A.imag, A.real) % (2.0 * math.pi)

	# PRINTING RESULTS SINGLE
  #in radians
	print ("delay in radians (single) :")
	print (result_single) 
  #in degrees
	print("delay in degrees (single) :")
	print (math.degrees(result_single)
	# PRINTING RESULTS RETURN
  #in radians
	print ("delay in radians (return) :")
	print (result_return) 
  #in degrees
	print("delay in degrees (return) :")
	print (math.degrees(result_return))
	# FINAL RESULT
	print ("FINAL DELAY (arg(R0)):")
	print ()

if __name__ == "__main__":
    main()
