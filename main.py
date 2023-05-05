from numpy import random
import matplotlib.pyplot as plt
import time
from math import sqrt
import numpy as np


def Algorithm1(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        if c[i]:
            j = 2 * i
            while j <= n:
                c[j] = False
                j += i
        i += 1
    return c


def Algorithm2(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        j = 2 * i
        while j <= n:
            c[j] = False
            j += i
        i += 1
    return c


def Algorithm3(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        if c[i]:
            j = i + 1
            while j <= n:
                if j % i == 0:
                    c[j] = False
                j += 1
        i += 1
    return c


def Algorithm4(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        j = 2
        while j < i:
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1
    return c


def Algorithm5(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        j = 2
        while j <= sqrt(i):
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1
    return c


n_values = range(2, 1000)

algorithm1_times = []
algorithm2_times = []
algorithm3_times = []
algorithm4_times = []
algorithm5_times = []

for n in n_values:
    start_time = time.time()
    Algorithm1(n)
    algorithm1_times.append(time.time() - start_time)
    # result1 = Algorithm1(n)
    # print(f"Algorithm1({n}): {result1}. Time: {time.time()-start_time:.6f} seconds.")

    start_time = time.time()
    Algorithm2(n)
    algorithm2_times.append(time.time() - start_time)

    start_time = time.time()
    Algorithm3(n)
    algorithm3_times.append(time.time() - start_time)

    start_time = time.time()
    Algorithm4(n)
    algorithm4_times.append(time.time() - start_time)

    start_time = time.time()
    Algorithm5(n)
    algorithm5_times.append(time.time() - start_time)

# Plot the execution times on a graph
plt.plot(n_values, algorithm1_times, label="Algorithm1")
plt.plot(n_values, algorithm2_times, label="Algorithm2")
plt.plot(n_values, algorithm3_times, label="Algorithm3")
plt.plot(n_values, algorithm4_times, label="Algorithm4")
plt.plot(n_values, algorithm5_times, label="Algorithm5")

plt.xlabel("n")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.show()
