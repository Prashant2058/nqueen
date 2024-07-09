import numpy as np
import random
import set_up as sp
import csv

def create_boolean_array(n):
    return np.ones((n , n))

def las_vegas(n):
    a = True
    atmpt = 0
    while(a):
        atmpt +=1 
        result = create_boolean_array(n)
        valid_space = [ i for i in range( 0 , n*n )]
        
        for i in range(0 , n):
            
            q_pos = random.choice( valid_space )
            valid_space.remove( q_pos )
            
            x = q_pos // n
            y = q_pos % n
            
            points = sp.invalid_points(n , x , y)

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

for n in range(4,21):
    i = 0
    a = []

    result,atmpt = las_vegas(n)
    while i < 1000:
        result,atmpt = las_vegas(n)
        i += 1
        a.append(atmpt)
        
    avg = int(sum(a)/len(a))

    with open('lv.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        file.seek(0, 2)  
        if file.tell() == 0:
            writer.writerow(["n", "Avg_Attempt"])
        writer.writerow([n, avg])