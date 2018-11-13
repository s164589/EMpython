# -*- coding: utf-8 -*-
import math
import json
import numpy as np

import transform
import intrinsicPolarization as inPol


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
E_0real = [0,9,0]
E_0imag = [9,0,0]

print(inPol.getPolarization(E_0real, E_0imag))

