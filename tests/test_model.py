# tests/test_model.py
import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from solver import euler_step

def test_population_conservation():
    S, I, R = 990, 10, 0
    beta, gamma = 0.47, 0.09
    N = 1000

    S2, I2, R2 = euler_step(S, I, R, beta, gamma, N, dt=1)

    total_before = S + I + R
    total_after = S2 + I2 + R2

    assert abs(total_before - total_after) < 1e-6
