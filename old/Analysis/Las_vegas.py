import numpy as np
import random
import csv


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
    atmpt = 0
    while(a):
        atmpt +=1 
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
        
    return result,atmpt

for n in range(4,50):
    i = 0
    a = []

    result,atmpt = las_vegas(n)
    while i < 1:
        result,atmpt = las_vegas(n)
        i += 1
        a.append(atmpt)
        
    avg = int(sum(a)/len(a))

    with open('lv_single.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        file.seek(0, 2)  
        if file.tell() == 0:
            writer.writerow(["n", "Avg_Attempt"])
        writer.writerow([n, avg])