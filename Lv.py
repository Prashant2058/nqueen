import numpy as np
import random

def create_boolean_array(n):
    return np.ones((n, n))

def invalid_points(n, x, y):
    """Calculate invalid points for a queen placed at (x, y) on an n x n board."""
    points = []
    for i in range(n):
        # Same row
        points.append((x, i))
        # Same column
        points.append((i, y))
        # Diagonals
        if 0 <= x + i < n and 0 <= y + i < n:
            points.append((x + i, y + i))
        if 0 <= x + i < n and 0 <= y - i < n:
            points.append((x + i, y - i))
        if 0 <= x - i < n and 0 <= y + i < n:
            points.append((x - i, y + i))
        if 0 <= x - i < n and 0 <= y - i < n:
            points.append((x - i, y - i))
    points = list(set(points))  # Remove duplicates
    points.remove((x, y))  # Remove the position of the queen itself
    return points

def display_board(board):
    """Display the board in a readable format."""
    queen_logo = '♛'
    for row in board:
        print(" ".join(queen_logo if cell == 1 else "." for cell in row))

def las_vegas(n):
    while True:
        result = create_boolean_array(n)
        valid_space = [i for i in range(n * n)]
        success = True

        for i in range(n):
            if not valid_space:
                success = False
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

        if success:
            break

    return result


result = las_vegas(8)
display_board(result)
