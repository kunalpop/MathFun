# -*- coding: utf-8 -*-
"""
@author: Kunal
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):

    if(n==max(r_q,c_q)):
        count  = 2*(n-1) + min(n-r_q,n-c_q) + min(r_q-1,c_q-1)
    else:
        count = 2*(n-1) + min(n-r_q,n-c_q) + min(r_q-1,c_q-1) + min(n-r_q,c_q-1) + min(n-c_q,r_q-1)

    print(min(n-r_q,n-c_q),min(r_q-1,c_q-1),min(n-r_q,c_q-1),min(n-c_q,r_q-1))

    blocks = [0,0,0,0,0,0,0,0]

    for obstacle in obstacles:
        r_obs = obstacle[0]
        c_obs = obstacle[1]

        #Row
        if(r_obs == r_q):
            if(c_obs < c_q):
                if(blocks[0]<(c_obs-1+1)):
                    blocks[0] = (c_obs-1+1)
            else:
                if(blocks[1]<(n-c_obs+1)):
                    blocks[1] = (n-c_obs+1)        
        #Column
        elif(c_obs == c_q):
            if(r_obs < r_q):
                if(blocks[2]<(r_obs-1+1)):
                    blocks[2] = (r_obs-1+1)
            else:
                if(blocks[3]<(n-r_obs+1)):
                    blocks[3] = (n-r_obs+1)
        #Right Diagonal
        elif((c_obs-c_q)==(r_obs-r_q)):
            if(c_q<c_obs and r_q<r_obs):
                if(blocks[4]<min(n-r_obs+1,n-c_obs+1)):
                    blocks[4] = min(n-r_obs+1,n-c_obs+1)
            else:
                if(blocks[5]<min(r_obs-1+1,c_obs-1+1)):
                    blocks[5] = min(r_obs-1+1,c_obs-1+1)
        #Left Diagonal
        elif((c_obs-c_q)==-(r_obs-r_q)):
            if(r_q<r_obs):
                if(blocks[6]<min(c_obs-1+1,n-r_obs+1)):
                    blocks[6] = min(c_obs-1+1,n-r_obs+1)
            else:
                if(blocks[7]<min(n-c_obs+1,r_obs-1+1)):
                    blocks[7] = min(n-c_obs+1,r_obs-1+1)

    print(count,blocks)
    count = count - sum(blocks)

    return(count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
