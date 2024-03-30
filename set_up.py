import numpy as np
import matplotlib.pyplot as plt

def invalid_points(n, i, j):
    points = set()

    # Condition 1 : x = 0 to n-1, y = j
      # squares in the same column
    points.update([(x, j) for x in range(n)])

    # Condition 2 : x = i, y = 0 to n-1
      # squares in the same row
    points.update([(i, y) for y in range(n)])

    # Condition 3 : x = 0 to n-1, y = (i+j)-x
      # squares in same negative diagonal
    points.update([(x, i + j - x) for x in range(n)])

    # Condition 4 : x = 0 to n-1, y = x - (i - j)
      # squares in same positive diagonal
    points.update([(x, x - i + j) for x in range(n)])

    # Remove (i, j)
    points.discard((i, j))

    # Filter p,q such that 0 <= q < n
      # we dont check for p as p belongs to range(n) i.e. 0 to n-1 or i
    points = {(p, q) for p, q in points if q >= 0 and q < n}

    return points


def display_board(arrangement):
    
    #Create a board with all squares black
    board = np.zeros((arrangement.shape[0], arrangement.shape[1], 3))

    # starting from 0,0 make every 2nd square white
    board[::2, ::2] = [1, 1, 1]
    #same as before now starting from 1,1
    board[1::2, 1::2] = [1, 1, 1]

    plt.imshow(board)

    # plot queen in position with value = 1
    for i in range(arrangement.shape[0]):
        for j in range(arrangement.shape[1]):
            if arrangement[i][j] == 1:
                plt.text(j, i, '♕', ha='center', va='center', color='black', fontsize=25, bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle,pad=0.25'))

    plt.xticks([])
    plt.yticks([])
    plt.show()