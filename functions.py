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

def getRightOrLeftPol(E_0real, E_0imag, betaVec):
    cross = np.cross(E_0real, E_0imag)
    dot = np.dot(betaVec, cross)
    if(np.less(dot, 0)):
        return "Left-hand polarization"
    elif(np.greater(dot, 0)):
        return "Right-hand polarization"
    else:
        return "Error maybe it's linear or beta is not perpendicular to the electric field?"

def findMajorAndMinorSemiAxes(E_0real, E_0imag):
    E_0real = np.asarray(E_0real)
    E_0imag = np.asarray(E_0imag)
    E_0real_norm = np.linalg.norm(E_0real)
    E_0imag_norm = np.linalg.norm(E_0imag)
    
    if(np.equal(E_0real_norm, E_0imag_norm)):
        phiZero = 0
    else:
        phiZero = (1/2) * (np.arctan((2*np.dot(E_0real, E_0imag)) / (E_0imag_norm**2 - E_0real_norm**2)))
    
    E_1 = E_0real * np.cos(phiZero) - E_0imag * np.sin(phiZero)
    E_2 = -(E_0real * np.sin(phiZero)) - E_0imag * np.cos(phiZero)
    
    E_1_norm = np.linalg.norm(E_1)
    E_2_norm = np.linalg.norm(E_2)

    if(np.greater(E_1_norm, E_2_norm)):
        major = E_1_norm
        minor = E_2_norm
    elif(np.less(E_1_norm, E_2_norm)):
        major = E_2_norm
        minor = E_1_norm
    else:
        major = E_1_norm
        minor = E_1_norm

    AR = major / minor

    return major, minor, AR

def emWavePowerInst(E_field, H_field):
    S = np.cross(E_field, H_field)
    return S

def emWavePowerRMS(E_field, H_field):
    cross = np.cross(E_field, np.conj(H_field))
    S = (1/2) * np.real(cross)
    
    return S



#E_0 = E_0real + j * E_0imag

# Polarization is the relationshiå between  E_0real + E_0imag

## Linear polarization



