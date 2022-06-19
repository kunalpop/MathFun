# -*- coding: utf-8 -*-
"""
Created on Jan 19 19:20:12 2021
@author: Kunal Soni
@DEscription:
    -Given mountain peak coordinates(x,y):
        (2,5);(4,6);(7,2)
    -All mountains sloping at 45 degrees
    -All mountain bases on X axis    
    Find the total number of peaks as seen from z axis
"""

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
def all_coords(peaks):
    
    coords = []
    
    for pt in peaks:
        x = pt[0]
        y = pt[1]
        coords.append(Point(x,y))
        #coords.append(Point(x+y,0))
        #coords.append(Point(x-y,0))
        
        
    return(coords)
            
def silhoutte_peaks(peaks):
           
    coords = all_coords(peaks)
    
    n = len(coords)

    L = M = []
    
    for i in range(n):
        L.append(coords[i].y+coords[i].x)#lines of the form y+x
        M.append(-coords[i].y+coords[i].x)#lines of the form y-x
        
    count = 0 
    
    #O(N2)
    for i in range(n):
        for j in range(i+1,n):
            if( (L[i]>L[j]) and (M[i]>M[j]) ):
                count += 1
                
    return(n-count)
        
def main():
    peaks = [(2,5),(4,6),(7,2)]
    
    print("result = ",silhoutte_peaks(peaks))
    
if __name__ == "__main__":
    main()
    
    
