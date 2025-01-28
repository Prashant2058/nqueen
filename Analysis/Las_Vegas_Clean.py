import numpy as np
import random

def invalid_points(n, i, j):
    points = set()
    points.update([(x, j) for x in range(n)])
    points.update([(i, y) for y in range(n)])
    points.update([(x, i + j - x) for x in range(n)])
    points.update([(x, x - i + j) for x in range(n)])
    points.discard((i, j))
    points = {(p, q) for p, q in points if q >= 0 and q < n}
    return points


def las_vegas(n):
    a = True
    while(a): 
        result = np.ones((n , n))
        valid_space = [ i for i in range( 0 , n*n )]
        
        for i in range(0 , n):
            
            q_pos = random.choice( valid_space )
            valid_space.remove( q_pos )
            
            x = q_pos // n
            y = q_pos % n
            
            points = invalid_points(n , x , y)

            for p , q in points:
                
                result[p, q] = 0
                t = n * p + q
                
                if t in valid_space:
                    valid_space.remove(t)
            
            if len( valid_space ) == 0:
                if i > n-2:
                    a = False
                break
        
    return result

ans = las_vegas(5)
print(ans)