import random
import matplotlib.pyplot as plt

analytical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

def monte_carlo_simulation(trials: int):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        s = dice1 + dice2
        sums_count[s] += 1

    probabilities = {
        s: count / trials for s, count in sums_count.items()
    }
    return probabilities


def plot_probabilities(simulated, analytical):
    sums = list(simulated.keys())
    sim_values = list(simulated.values())
    ana_values = [analytical[s] for s in sums]

    plt.figure(figsize=(10, 6))
    plt.bar(sums, sim_values, width=0.4, label="Monte-Carlo", align='center')
    plt.plot(sums, ana_values, color='red', marker='o', label="Analytical")

    plt.xlabel("Сума на двох кубиках")
    plt.ylabel("Ймовірність")
    plt.title("Порівняння Monte-Carlo та аналітичних ймовірностей")
    plt.legend()
    plt.grid(axis='y')
    plt.show()


N = 100000

simulated_probs = monte_carlo_simulation(N)
plot_probabilities(simulated_probs, analytical_probabilities)