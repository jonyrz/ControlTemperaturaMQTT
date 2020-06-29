# import numpy as np

import math


class Habitacion:
    def __init__(self, alpha, beta, gamma, zeta, xi, rho, phi, chi, tau, omega):
        """
        Demasiado grecio
        """
        self.alpha = alpha
        self.beta  = beta 
        self.gamma = gamma
        self.zeta  = zeta 
        self.xi    = xi   
        self.rho   = rho  
        self.phi   = phi  
        self.chi   = chi  
        self.tau   = tau  
        self.omega = omega
        
        # H(t): 0 if t <= 0 else 1
        # enf(t) = (xi e^(rho * t + phi) + chi) * H(t - tau)
        # temp(t) = alpha * sin (beta * t + gamma) + zeta
        # T(t) = temp(t) + enf(t)

        self.H = lambda t: 0 if t <= 0 else 1
        self.enf = lambda t: (self.xi * math.exp(self.rho * t - self.phi) + self.chi) * self.H(t - self.tau) * self.H(-t + self.omega)
        self.temp = lambda t: self.alpha * math.sin(self.beta * t + self.gamma) + self.zeta
        self.T = lambda t: self.temp(t) + self.enf(t)
        

    def read(self, t):
        return self.T(t)
