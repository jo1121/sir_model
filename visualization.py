# visualization.py
import matplotlib.pyplot as plt

def plot_results(S, I, R, title="SIR Model Simulation"):
    plt.figure(figsize=(8, 5))
    plt.plot(S, label="Susceptible", linewidth=2)
    plt.plot(I, label="Infected", linewidth=2)
    plt.plot(R, label="Recovered", linewidth=2)

    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
