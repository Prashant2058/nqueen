import numpy as np
import random
import csv

def create_boolean_array(n):
    return np.ones((n, n))

def invalid_points(n, i, j):
    points = set()
    points.update([(x, j) for x in range(n)])
    points.update([(i, y) for y in range(n)])
    points.update([(x, i + j - x) for x in range(n) if 0 <= i + j - x < n])
    points.update([(x, x - i + j) for x in range(n) if 0 <= x - i + j < n])
    points.discard((i, j))
    return points

def las_vegas(n):
    attempts = 0
    while True:
        result = create_boolean_array(n)
        valid_space = [i for i in range(0, n*n)]

        for i in range(0, n):
            attempts += 1
            if not valid_space:
                break

            q_pos = random.choice(valid_space)
            valid_space.remove(q_pos)

            x = q_pos // n
            y = q_pos % n

            points = invalid_points(n, x, y)

            for p, q in points:
                result[p, q] = 0
                t = n * p + q
                if t in valid_space:
                    valid_space.remove(t)

        if np.sum(result) == n:
            return result, attempts

    return result, attempts

results = {}

for n in range(4, 21):
    total_attempts = 0
    num_runs = 1000

    for _ in range(num_runs):
        _, attempts = las_vegas(n)
        total_attempts += attempts

    avg_attempts = total_attempts // num_runs
    results[n] = avg_attempts

    print(f"N = {n}: Average attempts = {avg_attempts}")

# Write results to CSV
with open('las_vegas_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["N", "Average Attempts"])
    for n, avg_attempts in results.items():
        writer.writerow([n, avg_attempts])

print("Results have been written to 'las_vegas_results.csv'")
