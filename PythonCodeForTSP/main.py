# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 14:54:56 2022

@author: Brandon
"""
import numpy as np
import random
import copy
import matplotlib.pyplot as plt
from oxcross import OXCross
from insertMutation import insertMutation
from swapMutation import swapMutation
from inversionMutation import inversionMue
from scrambleMutation import scrambleMue

def main():
    SelectedMutation = ""
    ##########
    # Global variables
    population = 500
    Generations = 1000
    ### Make sure these total 1.
    probCross = 0.8 #Crossover ~Made
    probMu = 0.05 # 4 mutations Basics ~Made 
    probRep = 0.15 # reproduction ~Made
    
    #SelectedMutation = "I" # I or i for insert
    #SelectedMutation = "S" # S or s for swap
    #SelectedMutation = "V" # V or v for inversion
    SelectedMutation = "C" # C or c for scramble

    seed = 41
    #seed = 3.8423
    #seed = 674214
    ###########
    random.seed(seed)
    board = np.array([[   0,1339,1439,1421, 159, 977, 139, 776, 737,1109,1956, 263, 771,1075,
        99, 381,1362,1243,1951, 825, 979,1080,1536, 904, 214, 210, 432, 169,
      1887,1270],
     [1422,   0,1536, 711, 959, 713, 934, 617,1642, 531, 168,1573,1607,1865,
      1608, 624, 866, 270,1839, 757, 761,1307,1469, 168,1262,1704, 925, 990,
      1062, 159],
     [1145, 281,   0, 388, 243,1536,1464,1572,1447, 738, 119,1098,1888,1108,
      1637,1578,1318,1430, 413, 888,1577, 620, 921,1839, 176, 867, 621, 481,
       157, 765],
     [1939, 144, 312,   0, 278, 332,1023,1432,1971,1045,1501,1233,1532, 404,
       559,1601,1567,1470,1004,1332,1170,1493, 328, 867,1425,1736,1916, 524,
      1443,1217],
     [ 632,1231, 829,1259,   0, 493, 933, 711,1575, 150,1217,1488,1919, 894,
      1937,1023, 334, 307,1301,1739,1784, 877, 830,1600,1732, 855, 577, 740,
      1464,1577],
     [ 534,1669,1343,1558,1877,   0,1879,1613,1770, 668,1993,1453,1833,1315,
      1058, 551,1221,1621, 281,1573,1927,1219, 522,1247, 313, 777,1173, 542,
      1327,1911],
     [ 506, 124,1911,1309, 712, 817,   0, 952,1984, 170,1664,1169,1686,1872,
       290,1809,1651,1765, 817,1864,1561, 519, 485,1552,1236, 625,1150,1460,
       975, 211],
     [ 411,1187,1277, 992, 315,1113, 610,   0, 312, 697, 489,1769,1186,1998,
      1847, 699,1322, 815, 731, 555,1286, 185,1955, 287,1485, 965, 651, 340,
       535,1040],
     [1117, 703,1298, 598,1974,1366, 106,1829,   0, 166,1679, 806,1362,1739,
       153,1848,1345,1701,1824, 796, 310,1640,1465,1276, 898, 768,1937, 971,
      1329,1776],
     [1863,1790, 858, 915,1751, 393, 284, 456, 883,   0, 469,1235,1613, 564,
       678, 132, 960, 740,1018,1512,1901,1338,1240, 296,1692, 539, 556,1775,
       712,1205],
     [1019, 613,1355, 615,1079, 870, 574, 478,1068, 241,   0,1486,1013, 917,
       881,1479, 726, 357, 146, 738, 610, 913, 925, 547,1815, 770,1577,1056,
      1755,1864],
     [1079, 199,1058, 849,1768, 738,1943, 714, 515,1441, 689,   0,1433,1667,
       614,1837, 768, 564, 778, 945,1058, 175,1160,1386,1071, 811,1387,1164,
       170,1664],
     [ 783, 366,1682, 808,1959, 193, 473, 222, 811, 821, 659,1527,   0, 890,
      1060,1254, 672,1036,1728, 537,1666, 863, 514,1025,1070, 449, 892,1529,
      1026, 722],
     [1519, 253, 553, 455, 499,1120, 941,1436,1976,1182,1564, 187,1298,   0,
      1757, 951,1077, 610,1223, 119, 233, 746, 244,1681,1196,1155, 434, 449,
       853,1516],
     [ 737,1074,1627,1363,1232,1811,1700, 499, 281,1033,1333, 336,1200,1647,
         0, 984,1352, 986, 972, 986,1791, 563, 767, 965, 962,1582, 948,1783,
       163,1267],
     [ 394, 678,1350, 221, 277,1937,1883,1892, 163,1146,1900,1782, 913,1566,
       353,   0,1649,1812,1635, 780,1154, 463, 360,1689,1531,1837,1677, 697,
       821,1729],
     [ 142,1536, 952, 531,1573,1604,1443, 316,1214, 277, 805,1536, 538,1711,
       613,1517,   0,1053,1742,1108, 507, 604,1976,1190,1833,1673,1870, 481,
       323,1701],
     [ 603, 270,1883,1448,1645, 854,1160,1712,1907, 823, 847,1955,1155,1123,
      1740, 539,1560,   0, 653, 808,1251,1686, 264,1861,1422, 221, 734,1770,
       698, 563],
     [1790, 406,1938, 930,1386,1990,1620,1364,1452,1483,1936, 636, 254,1533,
       440,1131, 311,1996,   0,1456, 676, 156, 451,1536, 463, 965,1152,1734,
       817,1421],
     [ 235,1343, 561, 858, 655,1834,1072,1023,1901,1123, 862, 117,1116, 972,
      1471, 254, 595, 182,1221,   0,1984,1136,1945, 622,1175,1234,1230, 978,
       644,1207],
     [1427,1044,1055,1784, 995,1138,1117,1820, 208,1735,1665,1482, 468,1762,
      1814,1039, 904,1169, 841, 188,   0, 477,1123, 961, 945,1552,1499, 830,
      1166, 239],
     [1281,1756, 834, 103,1134, 461,1340, 361, 641, 205, 447,1691, 236, 546,
       666,1180,1066,  99,1845, 198, 445,   0,1553,1639, 770,1083,1592, 314,
      1837,1102],
     [ 965, 250, 265,1170, 986,1244, 893,1936, 250, 107,1985,1133, 982,1864,
      1475, 603, 319, 874,1713, 973,1045,1708,   0, 862,1033, 481,1321, 276,
      1626, 784],
     [1569, 287, 943,1694,1737,1549, 931, 219, 631, 666,1818, 888, 519, 989,
      1928, 562, 323,1951,1121, 162,1161, 159,1192,   0, 758, 823,1236, 142,
      1267, 384],
     [ 720,1076,1824,1028, 853,1587,1772, 293,1577, 209, 420, 788, 453,1812,
      1174,1347, 885, 653,1507, 776, 811, 628, 560, 677,   0,1919, 206,1231,
       436,1991],
     [ 143,1450,1845, 918, 964, 175,1351,1233,1471,1939,1662,1658,1837, 440,
      1232,1513,1505,1685, 192, 932,1845, 337,1451,1650,1916,   0, 541, 970,
      1126,1935],
     [ 914,1091,1657, 601, 644, 915,1476, 285,1981, 535, 543, 367,1819,1343,
      1850,1548, 812, 495, 947,1278,1431, 651, 495, 102,1339,1173,   0,1025,
       183, 247],
     [1623, 950,1838,1158,1233,1749, 459,1946,1803, 729, 578, 181,1967,1162,
      1843,1729,1572, 432, 265,1792, 313, 941,1744, 245,1043,1509,1758,   0,
      1118,1510],
     [ 545, 891, 154,1353, 943, 834,1572,1184,1754,1536, 182, 969,1888,1795,
      1262,1905, 811,1554, 854,1709,1011, 923, 787, 762, 721,1067, 839,1529,
         0, 310],
     [ 909,1092, 836, 222, 903, 894, 115, 157,1731, 650,1456,1339,1991, 733,
       464,1464,1664,1358,1118, 928, 133, 557,1869, 692,1282, 258, 428, 514,
       139,   0]])
    popu = []
    totalFitness = 0
    costTotal = 0
    probabilityofCrossMueRep = [probCross, probMu + probCross,  probMu + probCross + probRep]
    #print(probabiltyofCrossMueRep[0],probabiltyofCrossMueRep[1],probabiltyofCrossMueRep[2])
    ###############################################################################
    ### Generation 0 code
    for i in range(population):
        size = board.shape[0]
        path = []
        for i in range(0, size):
            path.append(i)
        #Shuffle all other numbers in path.
        random.shuffle(path)
        cost = generateCost(board, path)
        myNode = [cost, path]
        costTotal = costTotal + cost
        Fitness = 1 / cost
        totalFitness = totalFitness + Fitness
        popu.append(myNode)
    popu.sort()
    bestIndividual = copy.deepcopy(popu[0])
    inGen = 0
    lowestCost = costTotal
    bestGeneration = 0
    bestGen = copy.deepcopy(popu)
    pltx = []
    pltx.append(0)
    plty = []
    plty.append(costTotal/population)
    #for i in range(len(popu)):
    #    print(popu[i])
    #print(lowestCost)
    for i in range(Generations):
                                                         ### len(popu) also
        popu, costTotal, totalFitness = TestPopulation(popu, population, 
                                           probabilityofCrossMueRep, SelectedMutation,
                                           totalFitness, board)
        #print(lowestCost, costTotal)
        pltx.append(i + 1)
        plty.append(costTotal / population)
        if(lowestCost > costTotal):
            lowestCost = costTotal
            bestGeneration = i + 1
            ### never ended up using this.
            bestGen = copy.deepcopy(popu)
        if(bestIndividual[0] > popu[0][0]):
            bestIndividual = copy.deepcopy(popu[0])
            inGen = i + 1
        
    
    print(f"The best generation was generation: {bestGeneration}")
    print(f"With an average cost of: {lowestCost / population}")
    print(f"Best individual found was: {bestIndividual}")
    print(f"It first appeared in generation: {inGen}")
    plt.plot(pltx, plty)
    plt.show()
    plt.clf()
    #for i in range(len(popu)):
    #    print(popu[i])
    
    ###################################################################################
### returns a Population list, cost total, and the totalFitness of the new population.
### It expects a starting population 
def TestPopulation(popu, population, probabilityofCrossMueRep, SelectedMutation,
                   totalFitness, board):
    fitnessPercent = []
    total = 0
    for i in range(len(popu)):
        calculation = ((1 / popu[i][0]) / totalFitness)
        total = total + calculation
        if(len(fitnessPercent) > 0):
            calculation = calculation + fitnessPercent[len(fitnessPercent) - 1]
        fitnessPercent.append(calculation)
    #print(random.random())
    #print(totalFitness)
    #print(fitnessPercent[0])
    #print(total)
    #print(popu[0][0])
    TotalCrossovers = 0
    TotalMutations = 0
    TotalReproductions = 0
    for i in range(population):
        if(i == population - 1):
            if(TotalCrossovers % 2 == 0):
                TotalReproductions += 1 ## not sure yet
            else:
                TotalCrossovers += 1
        else:
            num = random.random()
            if(num <= probabilityofCrossMueRep[0]):
                TotalCrossovers += 1
            elif(num <= probabilityofCrossMueRep[1]):
                TotalMutations += 1
            else:
                TotalReproductions += 1
    #print(TotalCrossovers, TotalMutations, TotalReproductions)
    ###Select individuals for reproduction.
    ### Maybe upgrade these searches at some point.
    ### Say maybe a binary search?
    
    ### Maybe make half of the reproductions pick best indiviuals in order?
    
    newPaths = []
    RepDone = 0
    ### This part will be the Elitism section of code.
    lowerHalfOfReproductions = int(TotalReproductions/2)
    for i in range(lowerHalfOfReproductions):
        newPaths.append(copy.deepcopy(popu[i][1]))
        #popu[i][0] = -1
        RepDone += 1
    
    
    while True:
        if(TotalReproductions == RepDone):
            break
        num = random.random()
        for j in range(len(fitnessPercent)):
            if(num <= fitnessPercent[j]):
                ### This alone makes me think that I should maybe
                ### recalculate fitnessPercent after choosing one.
                #if(popu[j][0] == -1):
                #    break                        
                #else:
                newPaths.append(copy.deepcopy(popu[j][1]))
                #popu[j][0] = -1
                RepDone += 1
                break
    ### Select individuals for Mutation
    MueDone = 0
    while True:
        if(TotalMutations == MueDone):
            break
        num = random.random()
        for j in range(len(fitnessPercent)):
            if(num <= fitnessPercent[j]):
                #if(popu[j][0] == -1):
                #    break
                #else:
                mutatedPath = []
                if(SelectedMutation == "I" or SelectedMutation == "i"):
                    mutatedPath = insertMutation(copy.deepcopy(popu[j][1]))
                elif(SelectedMutation == "S" or SelectedMutation == "s"):
                    mutatedPath = swapMutation(copy.deepcopy(popu[j][1]))
                elif(SelectedMutation == "V" or SelectedMutation == "v"):
                    mutatedPath = inversionMue(copy.deepcopy(popu[j][1]))
                else:
                    mutatedPath = scrambleMue(copy.deepcopy(popu[j][1]))
                newPaths.append(mutatedPath)
                #popu[j][0] = -1
                MueDone += 1
                break
    ### Pair individuals for Crossover  
    ### A shuffle and then pair next to each other.
    #popu.sort()
    #while True:
    #    if(popu[0][0] == -1):
    #        popu.pop(0)
    #    else:
    #        break
    #print(len(popu))
    #random.shuffle(popu)
    CrossDone = 0
    while True:
        if(CrossDone == TotalCrossovers):
            break
        #path1 = popu.pop(0)
        #path2 = popu.pop(0)
        num = random.random()
        val = -1
        for j in range(len(fitnessPercent)):
            if(num <= fitnessPercent[j]):
                path1 = copy.deepcopy(popu[j])
                val = j
                break
        while True:
            num = random.random()
            breakout = False
            for j in range(len(fitnessPercent)):
                if(num <= fitnessPercent[j]):
                    if(val == j):
                        break
                    path2 = copy.deepcopy(popu[j])
                    breakout = True
                    break
            if(breakout):
                break
        CrossP1, CrossP2 = OXCross(path1[1], path2[1])
        newPaths.append(CrossP1)
        newPaths.append(CrossP2)
        CrossDone = CrossDone + 2
    #Length of newPaths should equal population now.
    newPopulation = []
    newCostTotal = 0
    newTotalFitness = 0
    for i in range(len(newPaths)): 
        cost = generateCost(board, newPaths[i])
        newIndividual = [cost, newPaths[i]]
        newPopulation.append(newIndividual)
        newCostTotal = newCostTotal + cost
        Fitness = 1 / cost
        newTotalFitness = newTotalFitness + Fitness

    newPopulation.sort()
    
    return newPopulation, newCostTotal, newTotalFitness


######################################
## Function from an old program for generating cost.
def generateCost(board, path):
    total = 0
    for i in range(0, len(path) - 1):
        ### [row][column]
        total += board[path[i]][path[i + 1]]
    #We need to return home.
    total += board[path[-1]][path[0]]
    return total
##############################################################    
### Also functions from an old program used for board generation.
### Run the program and use the functions in the console.
def printBoardWithCommas(board):
    print(np.array2string(board, separator=","))
def makeBoard():
    print("How many cities do you want on your board?")
    print("Please choose at least more than 2.")
    citiesNum = input("Number of cities: ")
    citiesNum = int(citiesNum)
    board = np.zeros([citiesNum,citiesNum],dtype=np.int)
    for i in range(0, citiesNum):
        for j in range(0, citiesNum):
            if(i == j):
                board[i][j] = 0
            else:
                board[i][j] = random.randint(99, 2000)
    return board
#############################################################                
                
if __name__ == "__main__":
    main()