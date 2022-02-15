# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 15:23:26 2022

@author: Brandon
"""
import random
import copy

def scrambleMue(path):
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
        
    pathing1 = path[:val1]
    pathing2 = path[val1:val2]
    pathing3 = path[val2:]
    #print(pathing2)
    temp = copy.deepcopy(pathing2)
    while True:
        random.shuffle(pathing2)
        if(temp != pathing2):
            break
    #print(pathing2)
    fullPath = pathing1 + pathing2 + pathing3
    return fullPath

if __name__ == "__main__":
    path = [12,3,4,5,6]
    path = scrambleMue(path)
    print(path)
        