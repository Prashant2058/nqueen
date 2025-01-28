import numpy as np
import csv
import random

def is_valid(x):
    n = len(x)
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or abs(x[i] - x[j]) == abs(i - j):
                return False
    return True

def random_nqueens(n):
    attempts = 0
    while True:
        attempts +=1
        x = [random.randint(1, n) for _ in range(n)]
        if is_valid(x):
            return x, attempts

def solve_nqueens_las_vegas(n):
    solution = None
    
    while solution is None:

        solution, attempts = random_nqueens(n)
    
    return solution, attempts

results = {}
num_runs = 1000

for n in range(4, 21):
    total_attempts = 0

    for _ in range(num_runs):
        _, attempts = solve_nqueens_las_vegas(n)
        total_attempts += attempts

    avg_attempts = total_attempts // num_runs
    results[n] = avg_attempts

    print(f"N = {n}: Average attempts = {avg_attempts}")

with open('las_vegas_traditional_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["N", "Average Attempts"])
    for n, avg_attempts in results.items():
        writer.writerow([n, avg_attempts])

print("Results have been written to 'las_vegas_results.csv'")