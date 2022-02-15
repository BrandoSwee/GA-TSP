# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 15:41:48 2022

@author: Brandon
"""

import random
import numpy as np
import copy

###############################
### inputs are two parents of equal length ASSUMED
def OXCross(path1, path2):
    Arr = []
    for i in range(len(path1) - 1):
    	Arr.append(i + 1)
    num1 = 0
    num2 = 0
    num = random.randint(0, len(path1) - 2)
    num1 = Arr[num]
    Arr[num] = 0
    while True:
        num = random.randint(0,len(path1) - 2)
        if(Arr[num] != 0):
            num2 = Arr[num]
            break
    if(num1 > num2):
        temp = num1
        num1 = num2
        num2 = temp
    #########
    ## test
    #num1 = 5
    #num2 = 15
    ### Setting up variables
    p1part1 = path1[:num1]
    p1part2 = path1[num1:num2]
    p1part2compare = copy.deepcopy(p1part2)
    p1part3 = path1[num2:]
    
    p2part1 = path2[:num1]
    p2part2 = path2[num1:num2]
    p2part2compare = copy.deepcopy(p2part2)
    p2part3 = path2[num2:]
    ### Setting up holes
    for i in range(len(p1part1)):
        if(p1part1[i] in p2part2compare):
            p1part1[i] = -1
    for i in range(len(p1part2)):
        if(p1part2[i] in p2part2compare):
            p1part2[i] = -1
    for i in range(len(p1part3)):
        if(p1part3[i] in p2part2compare):
            p1part3[i] = -1         
    
    for i in range(len(p2part1)):
        if(p2part1[i] in p1part2compare):
            p2part1[i] = -1
    for i in range(len(p2part2)):
        if(p2part2[i] in p1part2compare):
            p2part2[i] = -1
    for i in range(len(p2part3)):
        if(p2part3[i] in p1part2compare):
            p2part3[i] = -1

    ### Shift values for 1 and 2
    ### In part 3
    for i in range(len(p1part3)):
        if(p1part3[i] == -1):
            NotSet = True
            t = 1
            while(len(p1part3) > i + t):
                if(p1part3[i+t] != -1):
                    p1part3[i] = p1part3[i + t]
                    p1part3[i + t] = -1
                    NotSet = False
                    break
                t = t + 1
            if(NotSet):
                for j in range(len(p1part1)):
                    if(p1part1[j] != -1):
                        p1part3[i] = p1part1[j]
                        p1part1[j] = -1
                        NotSet = False
                        break
            if(NotSet):
                for j in range(len(p1part2)):
                    if(p1part2[j] != -1):
                        p1part3[i] = p1part2[j]
                        p1part2[j] = -1
                        #NotSet = False
                        break
    ### In part 1
    for i in range(len(p1part1)):
        if(p1part1[i] == -1):
            NotSet = True
            t = 1
            while(len(p1part1) > i + t):
                if(p1part1[i+t] != -1):
                    p1part1[i] = p1part1[i + t]
                    p1part1[i + t] = -1
                    NotSet = False
                    break
                t = t + 1
            if(NotSet):
                for j in range(len(p1part2)):
                    if(p1part2[j] != -1):
                        p1part1[i] = p1part2[j]
                        p1part2[j] = -1
                        #NotSet = False
                        break        
    ### In part 3 of p2
    for i in range(len(p2part3)):
        if(p2part3[i] == -1):
            NotSet = True
            t = 1
            while(len(p2part3) > i + t):
                if(p2part3[i+t] != -1):
                    p2part3[i] = p2part3[i + t]
                    p2part3[i + t] = -1
                    NotSet = False
                    break
                t = t + 1
            if(NotSet):
                for j in range(len(p2part1)):
                    if(p2part1[j] != -1):
                        p2part3[i] = p2part1[j]
                        p2part1[j] = -1
                        NotSet = False
                        break
            if(NotSet):
                for j in range(len(p2part2)):
                    if(p2part2[j] != -1):
                        p2part3[i] = p2part2[j]
                        p2part2[j] = -1
                        #NotSet = False
                        break
    ### In part 1 of p2
    for i in range(len(p2part1)):
        if(p2part1[i] == -1):
            NotSet = True
            t = 1
            while(len(p2part1) > i + t):
                if(p2part1[i+t] != -1):
                    p2part1[i] = p2part1[i + t]
                    p2part1[i + t] = -1
                    NotSet = False
                    break
                t = t + 1
            if(NotSet):
                for j in range(len(p2part2)):
                    if(p2part2[j] != -1):
                        p2part1[i] = p2part2[j]
                        p2part2[j] = -1
                        #NotSet = False
                        break                  
    child1 = p1part1 + p2part2compare + p1part3
    child2 = p2part1 + p1part2compare + p2part3
    #print(child1)
    #print(child2)
    return child1, child2
### Used for testing oxcross                
if __name__ == "__main__":
    path = [24, 29, 0, 10, 7, 6, 28, 21, 22, 26, 25, 9, 16, 5, 3, 15, 11, 18, 27, 17, 2, 20, 23, 19, 4, 1, 8, 12, 13, 14]
    path2 = [8, 7, 1, 20, 2, 25, 28, 3, 15, 26, 24, 0, 22, 14, 16, 17, 11, 9, 23, 6, 18, 13, 21, 12, 4, 10, 5, 19, 27, 29]
    seed = 10
    print(path[:0])
    print(path[29:])
    c1, c2 = OXCross(path, path2)
    print(c1)
    print(c2)