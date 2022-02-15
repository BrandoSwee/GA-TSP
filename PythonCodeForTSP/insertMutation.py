# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 14:32:25 2022

@author: Brandon
"""
import random

def insertMutation(path):
    num = random.randint(0,len(path) - 1)
    value = []
    value.append(path[num])
    #path.remove(path[num])
        ### has problems with empty lists
    path[num] = -1
    newpathp1 = []
    newpathp2 = []
    while True:
        num = random.randint(0,len(path))
        newpathp1 = path[:num]
        if(len(newpathp1) != 0):
            if(newpathp1[-1] != -1):
                newpathp2 = path[num:]
                if(len(newpathp2) != 0):
                    if(newpathp2[0] != -1):
                        break
                else:
                    break
        else:
            newpathp2 = path[num:]
            if(newpathp2[0] != -1):
                break
    fullPath = newpathp1 + value + newpathp2
    fullPath.remove(-1)
#    print(newpathp1)
#    print(value)
#    print(newpathp2)
    return fullPath

if __name__ == "__main__":
    path = [12,3,4,5,6]
    path = insertMutation(path)
    print(path)