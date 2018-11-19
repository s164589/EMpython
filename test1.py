# -*- coding: utf-8 -*-
import math
import json
import numpy as np

import transform
import functions as func


mu_zero = 4 * math.pi * pow(10, -7)
epsilon_zero = 8.854 * pow(10, -12)

## JSON Test lookup table
#with open("materials.json", "r") as material_file:
#    data = json.load(material_file)

#print(mu_zero)
#print(epsilon_zero)
#print(data["material"]["Gold"])
#print(data["material"]["Bismuth"])
#print(data["material"])

## Transform test
#print(transform.findFreqWithOmega(50*math.pi))


## Intrinsic polarization test


H_0 = [1, np.complex(0, np.sqrt(2)), 1]
H_0real, H_0imag = func.splitRealImag(H_0)
betaVec =  [-32.329/np.sqrt(2), 0, 32.329/np.sqrt(2)]

mu_r = 1
epsilon_r = 47

# Finds polarization
print(func.getPolarization(H_0real, H_0imag))
# Finds left or right polarized
print(func.getRightOrLeftPolH_field(H_0real, H_0imag, betaVec))
# Finds major or minor semi axis
print(func.findMajorAndMinorSemiAxis(H_0real, H_0imag))
# Findes frequency 
print("Freq: ", func.findFreq_MuEpBeta(mu_r, epsilon_r, betaVec))

omega = func.findOmega_Freq(250000000)
print("E_0: ",func.findE0_BetaOmegaEpH0(betaVec, omega, epsilon_r, H_0))

print(np.sqrt((mu_zero*mu_r)/(epsilon_zero*epsilon_r)))


## Opgave 3 test
# Non magnetic
mu_r = 1
epsilon_r = 8
sigma = 0.43
freq = 250 * 10**6

omega = func.findOmega_Freq(freq)

print("Medium quality: ", func.qualityOfConDie(sigma, func.findOmega_Freq(250*(10**6)), epsilon_r))

print("Intrinsic impedance: ", func.findInIm(mu_r, epsilon_r, sigma, omega))