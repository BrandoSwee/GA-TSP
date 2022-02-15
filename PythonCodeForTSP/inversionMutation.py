# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 15:04:51 2022

@author: Brandon
"""
import random

def inversionMue(path):
    Arr = []
    for i in range(len(path) + 1):
    	Arr.append(i)
    num = random.randint(0,len(Arr) - 1)
    val1 = Arr[num]
    val2 = 0
    Arr[num] = -1
    if(num != 0):
        Arr[num - 1] = -1
    if((len(Arr) - 1) != num):
        Arr[num + 1] = -1
        
    while True:
        num = random.randint(0,len(Arr) - 1)
        if(Arr[num] != -1):
            val2 = Arr[num]
            break
    
    if(val1 > val2):
        temp = val1
        val1 = val2
        val2 = temp
    #print(val1, val2)
    pathing1 = path[:val1]
    flipme = path[val1:val2]
    pathing3 = path[val2:]
    pathing2 = []
    for i in range(len(flipme)-1,-1,-1):
        pathing2.append(flipme[i])
    
    Fullpath = pathing1 + pathing2 + pathing3
    return Fullpath

if __name__ == "__main__":
    path = [12,3,4,5,6]
    ###    0  1 2 3 4 5
    path = inversionMue(path)
    print(path)
        