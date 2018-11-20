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

## Test functions
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


## Opgave 3 test (23/11-2018)
# Non magnetic
mu_r = 1
epsilon_r = 8
sigma = 0.43
freq = 250 * 10**6

omega = func.findOmega_Freq(freq)

# Spørgsmål 2
print("Medium quality: ", func.qualityOfConDie(sigma, func.findOmega_Freq(250*(10**6)), epsilon_r))

# Spørgsmål 3
print("Intrinsic impedance: ", func.findInIm(mu_r, epsilon_r, sigma, omega))

# Spørgsmål 4
beta = func.findBeta(mu_r, epsilon_r, sigma, omega)
print(beta)
Up = omega / beta
print("Up: ", Up)

# Spørgsmål 5
mu_r = 1
epsilon_r = 1
sigma = 67 * 10**6
freq = 3 * 10**9
plated = 10 * 10**(-6)

print("R_s: ", func.findSurfaceRis(mu_r, sigma, freq))

# Spørgsmål 6
omega = func.findOmega_Freq(freq)
alpha = func.findAlpha(mu_r, epsilon_r, sigma, omega)
skinDepth = func.findSkinDepth_alpha(alpha)

print("Skin depth: ", skinDepth)

# Spørgsmål 7
thickness = 10 * 10**(-6)

print("Is surface thick enough: ", func.isSurfaceInfinite(thickness, skinDepth))

# Spørgsmål 8

mu_r = 3.4
epsilon_r = 12.1
sigma = 100 * 10**(-3)
freq = 10 * 10**12

omega = func.findOmega_Freq(freq)

print("n_c: ", func.findComRefraction(mu_r, epsilon_r, sigma, omega))

# Spørgsmål 10

# Non magnetic
mu_r = 1

n = 1.544

# Maybe if SiO_2 have same conductivity as pure silicon
sigma = 4.4*10**(-4) # 0

epsilon_r = func.findEpsilon(mu_r, n)

eta = func.findInImLossLess(mu_r, epsilon_r)

E_0 = [1, 1.j, np.sqrt(3)]
betaVec = [np.sqrt(3), 0, -1]

print("S: ", func.findPower_EfieldEtaBetaEV(E_0, eta, betaVec))

# Spørgsmål 11

epsilon_r = 9
mu_r = 1
sigma = 0
eta = func.findInImLossLess(mu_r, epsilon_r)

epsilon_r_2 = 16
mu_r_2 = 1
sigma_2 = 0
eta_2 = func.findInImLossLess(mu_r_2, epsilon_r_2)

n_vector = [0, 10, 0]
betaVec = [1, 2, 0]
E_0 = [0, 0, 4]

print("TE or TM: ", func.TeTmPolarization(E_0, betaVec, n_vector))

tau = func.getTauPerpendicular(betaVec, n_vector, eta, eta_2)

# Spørgsmål 12



print("Power transmitted: ", func.getTransmittedPowerDensityPerpendicular(E_0, betaVec, n_vector, eta, eta_2), " %")

