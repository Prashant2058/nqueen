import numpy as np
import csv

def NQueens(k, n, x, attempts):  
    for i in range(1, n + 1):  
        attempts[0] += 1
        if place(k, i, x):
            x[k] = i 
            if k == n:
                return x[1:]
            else:
                result = NQueens(k + 1, n, x, attempts)
                if result:
                    return result
    return None

def place(k, i, x):
    for j in range(1, k):
        if x[j] == i or abs(x[j] - i) == abs(j - k):
            return False 
    return True

def solve_nqueens(n):
    x = [0] * (n + 1)
    attempts = [0]  # Use a list to store attempts, so it can be passed by reference
    solution = NQueens(1, n, x, attempts)
    return solution, attempts[0]

def create_matrix(arr):
    matrix = np.zeros((len(arr), len(arr)), dtype=int)
    for i in range(len(arr)):
        matrix[i][arr[i]-1] = 1
    return matrix

with open('backtracking_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["n", "Attempts"])

    for n in range(4, 21):
        solution, attempts = solve_nqueens(n)
        writer.writerow([n, attempts])
        print(f"N = {n}, Attempts = {attempts}")
