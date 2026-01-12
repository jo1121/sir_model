# simulation.py
from solver import euler_step

def run_simulation(S0, I0, R0, beta, gamma, days, dt=1):
    N = S0 + I0 + R0

    S, I, R = [S0], [I0], [R0]

    for _ in range(days):
        s, i, r = euler_step(S[-1], I[-1], R[-1], beta, gamma, N, dt)
        S.append(s)
        I.append(i)
        R.append(r)

    return S, I, R
