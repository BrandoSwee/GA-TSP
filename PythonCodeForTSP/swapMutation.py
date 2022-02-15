# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 14:56:02 2022

@author: Brandon
"""
import random

def swapMutation(path):
    Arr = []
    for i in range(len(path)):
    	Arr.append(i)
    num = random.randint(0,len(path) - 1)
    val1 = Arr[num]
    val2 = 0
    Arr[num] = -1
    while True:
        num = random.randint(0,len(path) - 1)
        if(Arr[num] != -1):
            val2 = Arr[num]
            break
    temp = path[val1]
    path[val1] = path[val2]
    path[val2] = temp
    return path
    
if __name__ == "__main__":
    path = [12,3,4,5,6]
    path = swapMutation(path)
    print(path)