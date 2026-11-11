import numpy as np

actual_probabilities = [0.1, 0.7, 0.5]
success_counts = np.zeros(3, dtype=int)
failure_counts = np.zeros(3, dtype=int)

for trial in range(101):
    selected_arm = np.argmax(
        np.random.beta(success_counts + 1, failure_counts + 1)
    )

    if np.random.rand() < actual_probabilities[selected_arm]:
        success_counts[selected_arm] += 1
    else:
        failure_counts[selected_arm] += 1

    if trial % 10 == 0:
        print(f"Trial: {trial:<3} Success/Failure: {list(zip(success_counts, failure_counts))}")