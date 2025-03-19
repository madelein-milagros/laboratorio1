import time

import matplotlib.pyplot as plt

# Function with logarithmic complexity O(log n)
def logarithmic_complexity(n):
    i = 1
    while i < n:
        i *= 2

# List of n values
n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]
times = []

# Measure execution time for each n
for n in n_values:
    start_time = time.time()
    logarithmic_complexity(n)
    end_time = time.time()
    times.append(end_time - start_time)

# Plotting the results
plt.plot(n_values, times, marker='o')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Logarithmic Complexity O(log n)')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()