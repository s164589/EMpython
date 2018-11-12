# -*- coding: utf-8 -*-

import math


# omega = 2 * pi * f
def findOmegaWithFreq(freq):
    omega = 2 * math.pi * f
    return omega

# freq = omega / (2 * pi)
def findFreqWithOmega(omega):
    freq = omega / (2 * math.pi)
    return freq

# beta = 2 * pi / lambda
def findBetaWithLamb(lamb):
    beta = (2 * math.pi) / lamb
    return lamb



print("Enter frequency (Hz): ")
f = int(input())

omega = findOmegaWithFreq(f)
freq = findFreqWithOmega(omega)

print("Omega: ", omega, " rad/s", "Frequency: ", freq, " Hz")














