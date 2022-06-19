# -*- coding: utf-8 -*-
"""
Created on Tue May 31 22:34:10 2022
@author: Kunal Soni
@Description:
    Given three arrays
    arr1 = [20,0,0,0,15,6,2,3,9]
    arr2 = [3,4,5,1,3,4]
    arr3 = [9,10,12,11,7,8,8,5,4]
    
    output: sorted array of unique elements
"""

def find_unique(arrList):
    
    unique_arr = arrList[0]
    
    for arr in arrList:
        unique_arr = list(set(unique_arr).union(arr))
    
    return(unique_arr)
    
        
def main():
    
    A = [20,0,90,0,15,6,45,32,21,33,9]
    B = [3,4,51,3,4]
    C = [9,10,12,11,7,88,5,4]
    
    arr = find_unique([A,B,C])
    
    #Merge sort O(NlogN)
    arr.sort()
    
    print(arr)
    
if __name__ == "__main__":
    main()