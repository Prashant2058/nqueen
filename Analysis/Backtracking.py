import numpy as np
import csv

atmpt = 0

def NQueens(k, n, x):
    global atmpt
    for i in range(1, n + 1):  
        if place(k, i, x):
            x[k] = i 
            if k == n:
                return x[1:]
            else:
                result = NQueens(k + 1, n, x)
                if result:
                    return result
    atmpt += 1
    return None

def place(k, i, x):
    for j in range(1, k):
        if x[j] == i or abs(x[j] - i) == abs(j - k):
            return False 
    return True

def solve_nqueens(n):
    x = [0] * (n + 1)  
    return NQueens(1, n, x) 

def create_matrix(arr):
    matrix = np.zeros((len(arr), len(arr)), dtype=int)
    for i in range(len(arr)):
        matrix[i][arr[i]-1] = 1
    return matrix


for n in range(4,21):
    solution = solve_nqueens(n)

    with open('back.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        file.seek(0, 2)  
        if file.tell() == 0:
            writer.writerow(["n", "Attempt"])
        writer.writerow([n, atmpt])