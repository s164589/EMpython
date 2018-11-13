# -*- coding: utf-8 -*-

import math
import numpy as np




## E_0real and E_0imag are real vectors
def isWaveLinearPol(E_0real, E_0imag):
    cross = np.cross(E_0real, E_0imag)

    if(np.equal(cross, 0).all()):
        return True
    else:
        return False

def isWaveCircularPol(E_0real, E_0imag):
    if(np.equal(np.absolute(E_0real))):
        return False
    elif(np.equal(np.absolute(E_0imag))):
        return False

#betaVec
#rVec


#E_0 = E_0real + j * E_0imag

# Polarization is the relationshiå between  E_0real + E_0imag

## Linear polarization

E_0real = [0,0.j,0.j]
E_0imag = [1,1.j,8]

print(isWaveCircularPol(E_0real,E_0imag))
print("Hej")

