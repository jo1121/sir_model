# solver.py
from model import sir_derivatives

def euler_step(S, I, R, beta, gamma, N, dt):
    """
    One Euler step for the SIR model.
    """
    dS, dI, dR = sir_derivatives(S, I, R, beta, gamma, N)

    S_next = S + dS * dt
    I_next = I + dI * dt
    R_next = R + dR * dt

    return S_next, I_next, R_next
