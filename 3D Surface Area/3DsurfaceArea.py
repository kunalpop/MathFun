# -*- coding: utf-8 -*-
"""
@author: Kunal Soni
"""
#!/bin/python3

import math
import os
import random
import re
import sys

def contribution_height(current, previous): 
    return abs(current - previous); 
  
def surfaceArea(A): 

    m = len(A)
    n = len(A[0])

    S = 0; 
  
    # Traversing the matrix. 
    for i in range(m):  
        for j in range(n): 
  
            up = 0;  
            left = 0; 
  
            # If its not the topmost row 
            if (i > 0): 
                up = A[i - 1][j]; 
  
            # If its not the leftmost column 
            if (j > 0): 
                left = A[i][j - 1]; 
  
            # Summing up the contribution of S by the current block 
            S = S + contribution_height(A[i][j], up)+contribution_height(A[i][j], left) 
              
            # If its the rightmost block of the matrix it will contribute  
            # area equal to its height as a wall on the right of the figure
            if (i == m - 1): 
                S = S + A[i][j]; 
  
            # If its the lowest block of the matrix it will contribute 
            #area equal to its height as a wall on the bottom of the figure 
            if (j == n - 1): 
                S = S + A[i][j]; 
  
    # Adding the contribution by  
    # the base and top of the figure 
    S = S + n * m * 2;

    return(S) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
