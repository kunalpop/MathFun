# -*- coding: utf-8 -*-
"""
Created on Tue May 31 22:34:10 2022
@author: Asus
@description: maze problem

entrance -> 0 0 0 0 0 0 0
            0 0 1 1 1 1 0
            0 0 1 0 0 0 0
            0 0 1 0 1 0 1
            1 1 1 0 0 0 0 -> exit
possible path:
entrance -> + + + + + + +
            0 0 1 1 1 1 +
            0 0 1 + + + +
            0 0 1 + 1 0 1
            1 1 1 + + + + -> exit

find shortest path
entrance -> + + + + + + +
            0 0 1 1 1 1 +
            0 0 1 0 0 + +
            0 0 1 0 1 + 1
            1 1 1 0 0 + + -> exit

return the shortest path [(0,0),(0,1),()...(m-1,n-1)]
"""

def check(mat,steps,i,j):
    
    m = len(mat)
    n = len(mat[0])
    
    if((i<m-1) and (mat[i+1][j]==0) and ((i+1,j) not in steps)):
        steps.append((i+1,j))
        i += 1
    elif((j<n-1) and (mat[i][j+1]==0) and ((i,j+1) not in steps)):
        steps.append((i,j+1))
        j += 1
    elif((i>0) and (mat[i-1][j]==0) and ((i-1,j) not in steps)):
        steps.append((i-1,j))
        i -= 1
    elif((j>0) and (mat[i][j-1]==0) and ((i,j-1) not in steps)):
        steps.append((i,j-1))
        j -= 1
    
    return([i,j,steps])

def path(mat):
    m = len(mat)
    n = len(mat[0])
    
    steps = []
    flag = 0
    i=j=0
    while((m-1,n-1) not in steps):
        temp = (i,j)
        [i,j,steps] = check(mat,steps,i,j)
        if(temp==(i,j)):
            flag = 1
            break
    if(flag):
        return([])
    else:
        return(steps)
            
def transpose(mat):
    
    m = len(mat)
    n = len(mat[0])
    
    matrix = []        
    for j in range(n):
        lst = []
        for i in range(m):
            lst.append(mat[i][j])
        matrix.append(lst)
        
    return(matrix)

def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup    

def main():
    mat = [[0,0,0,0,0,0,0],
           [0,0,1,1,1,1,0],
           [0,0,1,0,0,0,0],
           [0,0,1,0,1,0,1],
           [1,1,1,0,0,0,0]]
    
    paths = []
    paths.append(path(mat))
    paths.append(path(transpose(mat)))
    
    arr = paths[1]
    
    carr = []
    
    for coord in arr:
        carr.append(reverse(coord))
    
    paths[1] = carr
    
    if( (len(paths[0])>0) and (len(paths[1])>0) ):
        if( (len(paths[0])>len(paths[1])) ):
            min_len = len(paths[1])
            min_path = paths[1]
        else:
            min_len = len(paths[0])
            min_path = paths[0]
    elif((len(paths[0])>0)):
        min_len = len(paths[0])
        min_path = paths[0]
    elif((len(paths[1])>0)):
        min_len = len(paths[1])
        min_path = paths[1]
    else:
        min_len = 0

    if(min_len==0):
        print("No path found")
    else:
        print("The shortest path: ",min_path)
        print("Shortest path length: ",min_len)           
        
    
if __name__ == "__main__":
    main()
        