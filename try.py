import set_up as sp
import numpy as np

arrangement = np.array([[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]])
sp.display_board(arrangement)

n = 8
i = 1
j = 3
result = sp.invalid_points(n, i, j)
print("Points:", result)
