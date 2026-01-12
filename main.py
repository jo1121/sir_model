# main.py
from simulation import run_simulation
from visualization import plot_results

def main():
    print("=== Ebola SIR Epidemic Simulator ===")

    # User input
    N = int(input("Total population: "))
    I0 = int(input("Initial infected individuals: "))
    beta = float(input("Infection rate (beta): "))
    gamma = float(input("Recovery rate (gamma): "))
    days = int(input("Simulation days: "))

    S0 = N - I0
    R0 = 0

    S, I, R = run_simulation(S0, I0, R0, beta, gamma, days)

    plot_results(S, I, R, title="Ebola SIR Model")

if __name__ == "__main__":
    main()
