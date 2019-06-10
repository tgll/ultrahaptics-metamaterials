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
			sumIterations = 100000

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

	# Top of page 4
	def Kyn(self, n):
		return (float(n) * math.pi) / (self.l + self.d)

	# Top of page 4
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
		
		for i in range(1, n/2 + 1):
			k += 4.0 * f(x, kyn)
			x += 2.0 * h

		x = a + 2.0 * h
		for i in range(1, n/2):
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

			# print "addedAlpha {}\t\t\t addedBeta {}\t phi1 {}\t phi2 {}\t Kxn {}\t Kyn {} exp {}".format(addedAlpha, addedBeta, phi1, phi2, Kxn, self.Kyn(n), cmath.exp(exp))

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

# def plotRange(freq, ay, ax, ws, bS):
# 	waveLen = 343.0 / freq
# 	# t = waveLen / 40.0
# 	# w = waveLen / 20.0

# 	t = 0.0003
# 	# w = 0.0003

# 	fig, ax = plt.subplots(1)
# 	plt.ylabel('Bar widths, (wavelength/w)')
# 	plt.xlabel('Bar spacing, (wavelength/bS)')

# 	results = np.zeros((len(ws), len(bS)))

# 	for i, width in enumerate(ws):
# 		for j, spacing in enumerate(bS):
# 			w = width
# 			d = spacing
# 			l = ay - (2.0*t) - d
# 			limit = (4 * w) + (3 * d)

# 			if l < 0.0 or limit > ax:
# 				results[i][j] = 0
# 				print "ERROR. l:{}, limit:{}".format(l, limit)
# 			else:
# 				try:
# 					model = AcousticModeler(freq, t, d, l, w)
# 					result = (model.getMatrix() * np.matrix([[0],[1]]))[0]
# 					results[i][j] = math.atan2(result.imag, result.real) % (2.0 * cmath.pi)
# 				except ZeroDivisionError:
# 					results[i][j] = 0
			
# 			# if results[i][j] > 1.0:
# 			# 	results[i][j] = 1.0
# 			# if results[i][j] < -1.0:
# 			# 	results[i][j] = -1.0


# 	p = ax.pcolormesh(results, label='Test')
# 	ax.set_xticks(range(len(bS)))
# 	ax.set_xticklabels(bS, rotation='vertical')

# 	ax.set_yticks(range(len(ws)))
# 	ax.set_yticklabels(ws)
# 	fig.colorbar(p)

# 	fig.savefig('freq {}. ay {}mm. width {}-{}mm. bar {}-{}mm .png'.format(freq, ay*1000, ws[0]*1000, ws[-1]*1000, bS[0]*1000, bS[-1]*1000))



# def plotBarRange():
# 	freq = 64000.0
# 	ax = 0.007
# 	ay = 0.006
# 	t = 0.0003
# 	w = 0.0003
# 	numBars = 2.0
# 	accuracy = 100

# 	# 22.5, 45.0, ..., 337.5
# 	targetPhaseAngles = np.linspace(0.0, 2.0*cmath.pi, endpoint=True, num=17)[1:-1]
	
# 	# results
# 	foundPhaseAngles = np.zeros(15)
# 	foundPhasePositions = np.zeros(15)
# 	currentError = np.ones(15) * math.pi * 2.0

# 	dMax = min(ay-(2.0*t), (ax - (numBars*w))/(numBars-1.0))
	
# 	barSpacing = np.linspace(dMax, 0.0001, num=accuracy)
# 	barLengths = np.array([ay - (2.0*t) - d for d in barSpacing])
	
# 	phase = np.zeros(accuracy)

# 	for i, (d, l) in enumerate(zip(barSpacing, barLengths)):
# 		try:
# 			model = AcousticModeler(freq, t, d, l, w)
# 			result = (model.getMatrix() * np.matrix([[0],[1]]))[0]
# 			phase[i] = r = math.atan2(result.imag, result.real) % (2.0 * math.pi)

# 			for i, target in enumerate(targetPhaseAngles):
# 				diff = math.fabs(target - r)
# 				if diff < currentError[i]:
# 					currentError[i] = diff
# 					foundPhaseAngles[i] = r
# 					foundPhasePositions[i] = d


# 		except ZeroDivisionError:
# 			phase[i] = 0

# 	for t, e, d in zip(targetPhaseAngles, currentError, foundPhasePositions):
# 		print "Target: {}, error: {}, gap: {}".format(math.degrees(t), math.degrees(e), d)

# 	plt.figure(1)
# 	plt.ylabel('Phase')
# 	plt.xlabel('d')
# 	plt.plot(barSpacing*1000.0, phase)
# 	plt.plot(foundPhasePositions*1000.0, foundPhaseAngles, marker=u"o")
# 	plt.ylim([0, 2*math.pi])
# 	plt.legend(loc="upper left")
# 	plt.show()

# def plotBrickRange():
# 	freq = 40000
# 	waveLen = 343.0 / freq
# 	t = waveLen / 20.0
# 	w = waveLen / 20.0
# 	A = np.matrix([[0],[1]])


# 	targetPhaseAngles = np.linspace(0.0, 2.0*cmath.pi, endpoint=True, num=17)[1:-1]
# 	actualPhaseAngles = [math.radians(x) for x in \
# 							[ 23.3,   47.5,  67.4,  89.7, 115.6, 134.4, 159.3, \
# 							  177.3, 204.8, 226.2, 246.4, 271.4, 295.3, 315.0, 335.3]]
	
# 	barLengths      = [x*waveLen for x in [0.062, 0.092, 0.112, 0.132, 0.152, 0.162, 0.171, 0.191, 0.221, 0.241, 0.251, 0.271, 0.281, 0.301, 0.321]]
# 	interBarSpacing = [x*waveLen for x in [0.216, 0.212, 0.207, 0.189, 0.161, 0.166, 0.171, 0.134, 0.257, 0.234, 0.230, 0.207, 0.203, 0.175, 0.152]]

# 	measuredBarLengths = [x*0.001 for x in [0.5386, 0.7967, 0.8661, 1.1410, 1.3131, 1.3991, 1.4852, 1.6573, 1.9155, 2.0876, 2.1736, 2.3458, 2.4318, 2.6039, 2.7760]]
# 	measuredBarSpacing = [x*0.001 for x in [1.8720, 1.8325, 1.7930, 1.6352, 1.3984, 1.4379, 1.4773, 1.1616, 1.8046, 1.5968, 1.5573, 1.3600, 1.3205, 1.0837, 0.8864]]

# 	blocks = zip(barLengths, interBarSpacing)
# 	x = range(1, 16)
# 	results = np.zeros(15)

# 	for i, block in enumerate(blocks):
# 		l = measuredBarLengths[i]
# 		d = measuredBarSpacing[i]

# 		model = AcousticModeler(freq, t, d, l, w)
# 		result = (model.getMatrix() * A)[0]
# 		atanresult = math.atan2(result.imag, result.real)
# 		# print "Real: {}, imaginary: {}, arctan: {}".format(result.real, result.imag, atanresult)
# 		results[i] = math.atan2(result.imag, result.real) % (2.0 * cmath.pi)

# 	plt.figure(1)
# 	plt.ylabel('Phase difference (radians)')
# 	plt.xlabel('Brick')
# 	# plt.plot(x, targetPhaseAngles, label="Target phase angle")
# 	plt.plot(x, results, label="Result")
# 	plt.xlim([1, 15])

# 	plt.legend(loc="upper left")
# 	plt.show()

def main():
	# freq = 64000.0
	# ax = 0.007
	# ay = 0.006
	# d = 0.001
	# t = 0.0003
	# w = 0.0003
	# l = ay - (2.0*t) - d
	# model = AcousticModeler(freq, t, d, l, w)
	# print model.getMatrix()

	# plotBrickRange()
	plotBarRange()
	# ax = 0.008
	# ay = 0.006
	# t = 0.0003
	# # ays = np.arange(0.004, 0.007, 0.0005)
	# # for ay in ays:
	# 	# interBarSpacing = np.arange(ay-(2.0*t), 0.0002, -0.0001) # 0.1 mm
	# 	# barWidths = np.arange(0.5, (ax - (3*ay) - (6*t))/4, -0.005)

	# dMax = ay-(2.0*t)
	# interBarSpacing = np.linspace(dMax, 0.0001, num=100)
	# barWidths = np.linspace(0.0005, (ax - dMax)/4.0, num=100)

	# plotRange(64000, ay, ax, barWidths, interBarSpacing)
	# print "DONE"

if __name__ == "__main__":
	main()
