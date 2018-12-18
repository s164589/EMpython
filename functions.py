# -*- coding: utf-8 -*-
##
##  Author:     Emil Svendsen
##  Date:       14/11-2018
##  Last edit:  20/11-2018

import numpy as np

##                                                                                                              Polarization
###############################################################################################################################
## E_0real and E_0imag are real vectors
## Works with H_0real and H_0imag as well
## Check if Wave is linear polarization
def isWaveLinearPol(E_0real, E_0imag):
    cross = np.cross(E_0real, E_0imag)
    if(np.equal(cross, 0).all()):
        return True
    else:
        return False

###############################################################################################################################
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

###############################################################################################################################
## Check if Wave is not linear or circular polarization
def isWaveOnlyElliptical(E_0real, E_0imag):
    if(isWaveLinearPol(E_0real, E_0imag)):
        return False
    elif(isWaveCircularPol(E_0real, E_0imag)):
        return False
    else:
        return True

###############################################################################################################################
## Returns waves polarization
## Test
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

###############################################################################################################################
## Only works with Electric field
def getRightOrLeftPolE_field(E_0real, E_0imag, betaVec):
    cross = np.cross(E_0real, E_0imag)
    dot = np.dot(betaVec, cross)
    if(np.less(dot, 0)):
        return "Left-hand polarization"
    elif(np.greater(dot, 0)):
        return "Right-hand polarization"
    else:
        return "Error maybe it's linear or beta is not perpendicular to the electric field?"

###############################################################################################################################
## Only works with Magnetic field
def getRightOrLeftPolH_field(H_0real, H_0imag, betaVec):
    cross = np.cross(H_0real, - H_0imag)
    dot = np.dot(betaVec, cross)
    if(np.less(dot, 0)):
        return "Left-hand polarization"
    elif(np.greater(dot, 0)):
        return "Right-hand polarization"
    else:
        return "Error maybe it's linear or beta is not perpendicular to the field?"

###############################################################################################################################
## Finds major axis, minor axis and axial ratio 
def findMajorAndMinorSemiAxis(E_0real, E_0imag):
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

    if(isWaveLinearPol(E_0real, E_0imag)):
        AR = "Infinity"
        minor = 0
    else:
        AR = major / minor

    return major, minor, AR

##                                                                                                              TE/TM polarization
###############################################################################################################################
## Find TE or TM polarization
def TeTmPolarization(E_0, betaVec, nVec):
    if(np.equal(np.cross(nVec, betaVec), 0).all()):
        # Normal incident
        return "Normal incident"
    elif(np.equal(np.dot(E_0, nVec), 0)):
        # Perpendicular polarization
        return "TE, perpendicular polarization"
    elif(np.equal(np.dot(np.cross(betaVec, E_0), nVec), 0)):
        # Parallel polarization
        return "TM, parallel polarization"
    else:
        return "Something in between"

###############################################################################################################################
## Find gamma perpendicular with respect to the electric field
def getGammaPerpendicular(betaVec, nVec, eta1, eta2):
    betaVec_norm = np.linalg.norm(betaVec)
    nVec_norm = np.linalg.norm(nVec)
    cosVi = np.divide(np.dot(betaVec, nVec), (betaVec_norm * nVec_norm))
    Vi = np.arccos(cosVi)
    Vt = np.arcsin((eta2 / eta1) * np.sin(Vi))
    num = eta2 * cosVi - eta1 * np.cos(Vt)
    denum = eta2 * cosVi + eta1 * np.cos(Vt)
    gamma = num / denum
    return gamma

###############################################################################################################################
## Find tau perpendicular
def getTauPerpendicular(betaVec, nVec, eta1, eta2):
    betaVec_norm = np.linalg.norm(betaVec)
    nVec_norm = np.linalg.norm(nVec)
    cosVi = np.divide(np.dot(betaVec, nVec), (betaVec_norm * nVec_norm))
    Vi = np.arccos(cosVi)
    Vt = np.arcsin((eta2 / eta1) * np.sin(Vi))
    num = 2 * eta2 * cosVi
    denum = eta2 * cosVi + eta1 * np.cos(Vt)
    tau = num / denum
    return tau

###############################################################################################################################
## Find E-field transmit
def getE_TransmitPerpendicular(E_0i, betaVec, nVec, eta1, eta2):
    tau = getTauPerpendicular(betaVec, nVec, eta1, eta2)
    E_0t = np.multiply(tau, E_0i)
    return E_0t

###############################################################################################################################
## Find E-field transmitted power
def getTransmittedPowerDensityPerpendicular(E_0i, betaVec, nVec, eta1, eta2):
    tau = getTauPerpendicular(betaVec, nVec, eta1, eta2)
    tauSq = np.linalg.norm(tau)**2
    betaVec_norm = np.linalg.norm(betaVec)
    nVec_norm = np.linalg.norm(nVec)
    cosVi = np.divide(np.dot(betaVec, nVec), (betaVec_norm * nVec_norm))
    Vi = np.arccos(cosVi)
    Vt = np.arcsin((eta2 / eta1) * np.sin(Vi))
    T = tauSq * (eta1 / eta2) * (np.cos(Vt) / cosVi)
    return T


##                                                                                                              Power
###############################################################################################################################
## Finds instant power 
def emWavePowerInst(E_field, H_field):
    S = np.cross(E_field, np.conj(H_field))
    return S

###############################################################################################################################
## Finds RMS power
def emWavePowerRMS(E_field, H_field):
    cross = np.cross(E_field, np.conj(H_field))
    S = (1/2) * np.real(cross)
    
    return S

###############################################################################################################################
## Find power with E-field or the norm of E-field, intrinsic impedance and beta vector
def findPower_EfieldEtaBetaEV(E_field, eta, betaVec):
    betaNormalizedVec = np.divide(betaVec, np.linalg.norm(betaVec))
    S = np.multiply((1/2) * (np.linalg.norm(E_field)**2) / eta, betaNormalizedVec)
    return S

##                                                                                                              Utilities
###############################################################################################################################
## Splits a field into real and an imaginary part
def splitRealImag(Field_0):
    Field_0real = np.real(Field_0)
    Field_0imag = np.imag(Field_0)

    return Field_0real, Field_0imag


###############################################################################################################################
## Finds Up (phase velocity) with mu and epsilon 
## OBS LOSSLESS or low losses
def findUp_MuEp(mu_r, epsilon_r):
    mu_zero = 4 * np.pi * 10**(-7)
    epsilon_zero = 8.854 * 10**(-12)
    Up = 1 / np.sqrt(mu_zero * mu_r * epsilon_zero * epsilon_r)
    return Up


###############################################################################################################################
## Finds Frequency with mu, epsilon and betaVec.  !OBS! LOSSLESS (sigma = 0) => alpha = 0
def findFreq_MuEpBeta(mu_r, epsilon_r, betaVec):
    Up = findUp_MuEp(mu_r, epsilon_r)
    beta_norm = np.linalg.norm(betaVec)
    freq = (Up * beta_norm) / (2 * np.pi)
    return freq

###############################################################################################################################
## Finds E_0 with betaVec, omega, epsilon and H_0.  !OBS! LOSSLESS (sigma = 0) => alpha = 0
def findE0_BetaOmegaEpH0(betaVec, omega, epsilon_r, H_0):
    epsilon_zero = 8.854 * 10**(-12)

    cross = np.cross(betaVec, H_0)
    minusCross =  np.multiply((-1) , cross)
    E_0 = np.divide(minusCross , (omega * epsilon_zero * epsilon_r))
    return E_0
    
###############################################################################################################################
## omega = 2 * pi * f
def findOmega_Freq(freq):
    omega = 2 * np.pi * freq
    return omega

###############################################################################################################################
## Find lambda with frequency, mu and epsilon !!OBS!! Lossless!! Ulaby s. 123
def findLambdaWaveLenght(freq, mu_r, epsilon_r):
    mu_zero = 4 * np.pi * 10**(-7)
    mu = mu_zero * mu_r
    epsilon_zero = 8.854 * 10**(-12)
    epsilon = epsilon_zero * epsilon_r
    
    up = 1 / np.sqrt(mu * epsilon) ## ONLY LOSSLESS!!!
    lambdaWaveLenght = up / freq
    return lambdaWaveLenght


###############################################################################################################################
## Check quality of conductor or dielectric
def qualityOfConDie(sigma, omega, epsilon_r):
    epsilon_zero = 8.854 * 10**(-12)
    medium = sigma / (omega * epsilon_zero * epsilon_r)

    if(medium < 10**(-2)):
        return "Low-loss dielectric"
    elif(medium > 10**2):
        return "Good conductor"
    else:
        return "Quasi-conductor"

###############################################################################################################################
## Find intrinsic impedance with mu, epsilon, sigma and omega
def findInIm(mu_r, epsilon_r, sigma, omega):
    mu_zero = 4 * np.pi * 10**(-7)
    epsilon_zero = 8.854 * 10**(-12)
    epsilon = epsilon_zero * epsilon_r
    mu = mu_zero * mu_r

    squareRoot = np.sqrt(mu / epsilon) 
    minSqRt = (1 - 1.j * (sigma / (omega * epsilon)))**(-1/2)

    intrinsicImp = squareRoot * minSqRt
    return intrinsicImp

###############################################################################################################################
## Find intrinsic impedance with mu, epsilon. 
#### OBS lossless
def findInImLossLess(mu_r, epsilon_r):
    mu_zero = 4 * np.pi * 10**(-7)
    epsilon_zero = 8.854 * 10**(-12)
    epsilon = epsilon_zero * epsilon_r
    mu = mu_zero * mu_r

    intrinsicImp = np.sqrt(mu / epsilon) 
    return intrinsicImp

###############################################################################################################################
## Find skin depth with alpha
def findSkinDepth_alpha(alpha):
    deltaS = 1 / alpha
    return deltaS

###############################################################################################################################
## Find alpha with mu, epsilon, sigma and omega
def findAlpha(mu_r, epsilon_r, sigma, omega):
    mu_zero = 4 * np.pi * 10**(-7)
    epsilon_zero = 8.854 * 10**(-12)
    epsilon = epsilon_zero * epsilon_r
    epsilon2 = sigma / omega
    mu = mu_zero * mu_r

    del1 = (mu * epsilon) / 2
    del2 = (np.sqrt(1 + (epsilon2 / epsilon)**2) - 1)
    alpha = omega * (del1 * del2)**(1/2)
    return alpha

############################################################################################################################### 
## Find beta with mu, epsilon, sigma and omega
###### OBS ikke testet
def findBeta(mu_r, epsilon_r, sigma, omega):
    mu_zero = 4 * np.pi * 10**(-7)
    epsilon_zero = 8.854 * 10**(-12)
    epsilon = epsilon_zero * epsilon_r
    epsilon2 = sigma / omega
    mu = mu_zero * mu_r

    del1 = (mu * epsilon) / 2
    del2 = (np.sqrt(1 + (epsilon2 / epsilon)**2) + 1)
    beta = omega * (del1 * del2)**(1/2)
    return beta


############################################################################################################################### 
## Find surface risistance (R_s) with mu, sigma and frequency
def findSurfaceRis(mu_r, sigma, freq):
    mu_zero = 4 * np.pi * 10**(-7)
    mu = mu_zero * mu_r

    R_s = np.sqrt((np.pi * freq * mu) / sigma)
    return R_s

############################################################################################################################### 
## Is the surface thick enough (infinite thick)
def isSurfaceInfinite(thickness, delta_s):
    if(thickness > delta_s * 5):
        return "Yes, surface can be considered as infinite thick"
    else:
        return "No, surface is too thin"

############################################################################################################################### 
## Find complex refraction n_c with mu, epsilon, sigma and omega
def findComRefraction(mu_r, epsilon_r, sigma, omega):
    epsilon_zero = 8.854 * 10**(-12)

    epsilon_c_r = epsilon_r - 1.j*(sigma / (omega * epsilon_zero))
    n_c = np.sqrt( mu_r * epsilon_c_r )
    return n_c

############################################################################################################################### 
## Find epsilon with mu and index of refraction
def findEpsilon(mu_r, n):
    epsilon_r = (n**2) / mu_r
    return epsilon_r

############################################################################################################################### 
## Find H-field with intrinsic impedance, betaEigenVec and E-field
###### OBS ikke testet
def findHfield(intImp, betaEVec, E_field):
    cross = np.cross(betaEVec, E_field)
    H_field = np.multiply((1 / intImp), cross) 
    return H_field

##                                                                                                              Antenna
############################################################################################################################### 
## Find effective Area with lambda and Directivity
def findAe(Lambda, D):
    Ae = ((Lambda**2) * D) / (4 * np.pi)
    return Ae

############################################################################################################################### 
## Find Directivity with pattern solid angle (Omega_P)
## !OBS! ikke testet
def findDirectivity(Omega_P):
    D = (4 * np.pi) / Omega_P
    return D

############################################################################################################################### 
## Find radiation efficiency (xi) with R_rad and R_loss. Ulaby s. 416
def findRadiationEfficiency(R_rad, R_loss):
    xi = R_rad / (R_rad + R_loss)
    return xi


############################################################################################################################### 
## Find R_loss with freq, a, l, mu and sigma. Ulaby s. 416
def findR_loss(freq, a, l, mu_c, sigma_c):
    mu_zero = 4 * np.pi * 10**(-7)
    mu = mu_zero * mu_c
    factor = l / (2 * np.pi * a)
    Rloss = factor * np.sqrt((np.pi * freq * mu) / sigma_c)
    return Rloss


############################################################################################################################### 
## Find R_in with R_rad and R_losses. Ulaby s. 416
## !OBS! ikke testet
def findR_in(R_rad, R_loss):
    R_in = (R_rad + R_loss)
    return R_in

############################################################################################################################### 
## Find P_t with I_0 and R_in. Ulaby s. 416
## !OBS! ikke testet
def findP_t(I_0, Rin):
    Pt = (1/2) * (I_0**2) * Rin
    return Pt

############################################################################################################################### 
## Find R_rad with l and lambda. Ulaby s. 417
## !OBS! ikke testet
def findR_rad(l, Lambda):
    R_rad = 80 * (np.pi**2) * (l, Lambda)
    return R_rad

############################################################################################################################### 
## Find Antenna gain with radiation efficiency (xi) and Directivity
def findAntennaGain(xi, D):
    Gain = xi * D
    return Gain

############################################################################################################################### 
## Find Antenna gain in dB with radiation efficiency (xi) and Directivity
def findAntennaGain_dB(xi, D):
    Gain = xi * D
    Gain_dB = 10*np.log10(Gain)
    return Gain_dB

############################################################################################################################### 
## Find received power with transmitter gain, receiver gain, lambda, distance (R) and transmitter power (Pt) Ulaby s. 428
## Remember gain is not in dB
def findReceivedPower(gainT, gainR, Lambda, R, Pt):
    factor = gainT * gainR * Pt
    sq = (Lambda / (4 * np.pi * R))**2
    Prec = factor * sq
    return Prec 

############################################################################################################################### 
## Find received power with transmitter gain, receiver gain, lambda, distance (R) and transmitter power (Pt) Ulaby s. 428
def findReceivedPower_dB(gainT_dB, gainR_dB, Lambda, R, Pt):
    gainR = 10**(gainR_dB / 10)
    gainT = 10**(gainT_dB / 10)
    factor = gainT * gainR * Pt
    sq = (Lambda / (4 * np.pi * R))**2
    Prec = factor * sq
    return Prec 


