import numpy as np

n = 10
means = np.random.rand(n)
counts = np.zeros(n)
values = np.zeros(n)

for t in range(1000):
    ucb = values + 2 * np.sqrt(
        np.log(t + 1) / (counts + 1e-5)
    )
    arm = np.argmin(counts) if 0 in counts else np.argmax(ucb)

    reward = np.random.randn() + means[arm]
    counts[arm] += 1
    values[arm] += (reward - values[arm]) / counts[arm]

print("Total reward:", round(np.sum(values * counts), 2))