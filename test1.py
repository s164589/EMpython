# -*- coding: utf-8 -*-
import math
import json
import numpy as np

import transform
import intrinsicPolarization as inPol


mu_zero = 4 * math.pi * pow(10, -7)
epsilon_zero = 8.854 * pow(10, -12)

## JSON Test lookup table
with open("materials.json", "r") as material_file:
    data = json.load(material_file)

print(mu_zero)
print(epsilon_zero)
print(data["material"]["Gold"])
print(data["material"]["Bismuth"])
print(data["material"])

print(transform.findFreqWithOmega(50*math.pi))

E_0real = [0,0.j,0.j]
E_0imag = [1,1.j,8]

print(inPol.getPolarization(E_0real, E_0imag))

