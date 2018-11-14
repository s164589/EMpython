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

print(func.getPolarization(H_0real, H_0imag))

print(func.getRightOrLeftPolH_field(H_0real, H_0imag, betaVec))

print(func.findMajorAndMinorSemiAxes(H_0real, H_0imag))
