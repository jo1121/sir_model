# model.py

def sir_derivatives(S, I, R, beta, gamma, N):
    """
    Computes derivatives of the SIR model.
    """
    dS = -beta * S * I / N
    dI = beta * S * I / N - gamma * I
    dR = gamma * I

    return dS, dI, dR
