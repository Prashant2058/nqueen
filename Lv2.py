import numpy as np
import random
import set_up as sp

def create_boolean_array(n):
    return np.ones((n , n))

def las_vegas(n):
    a = True
    atmpt = 0
    while(a):
        print(atmpt)
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
        
    return result

result = las_vegas(8)
sp.display_board(result)