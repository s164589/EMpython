# -*- coding: utf-8 -*-

import math
import numpy as np




## E_0real and E_0imag are real vectors
## Check if Wave is linear polarization
def isWaveLinearPol(E_0real, E_0imag):
    cross = np.cross(E_0real, E_0imag)
    if(np.equal(cross, 0).all()):
        return True
    else:
        return False

## Check if Wave is Circular polarization
def isWaveCircularPol(E_0real, E_0imag):
    if(np.equal(np.linalg.norm(E_0real), 0)):
        return False
    elif(np.equal(np.linalg.norm(E_0imag), 0)):
        return False
    elif(np.equal(np.dot(E_0real, E_0imag), 0)):
        if(np.equal(np.linalg.norm(E_0real), np.linalg.norm(E_0imag))):
            return True
    else:
        return False

## Check if Wave is not linear or circular polarization
def isWaveOnlyElliptical(E_0real, E_0imag):
    if(isWaveLinearPol(E_0real, E_0imag)):
        return False
    elif(isWaveCircularPol(E_0real, E_0imag)):
        return False
    else:
        return True


def getPolarization(E_0real, E_0imag):
    if(np.equal(E_0real, 0).all() and np.equal(E_0imag, 0).all()):
            print("Both vectors can't be zero.")
            return False ## Error
    if(isWaveLinearPol(E_0real, E_0imag)):
        return "Linear polarized"
    elif(isWaveCircularPol(E_0real, E_0imag)):
        return "Circular polarized"
    else:
        return "Elliptical polarized"

#betaVec
#rVec


#E_0 = E_0real + j * E_0imag

# Polarization is the relationshiå between  E_0real + E_0imag

## Linear polarization



