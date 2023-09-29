# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 19:44:53 2023

@author: user
"""

import heapq

class priorityQueue:
    def __init__(self):
        self.cities = []
    def push(self, city, cost):
        heapq.heappush(self.cities,(cost, city))
    def pop(self):
        return heapq.heappop(self.cities)[1]
    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False
    def check(self):
        print(self.cities)
        
class ctNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)
        
romania = {}

def makehuristikdict():
    h = {}
    file = open("Input file.txt",'r')
    for line in file:
        
        node = line[0].strip()
        ct1 = line[0]
        sld = line[1].strip()
        h[node] = sld
        ct2 = line[2]
        dist = line[3]
        romania.setdefault(ct1,[]).append(ctNode(ct2, dist))
        romania.setdefault(ct2,[]).append(ctNode(ct1, dist))
        
    return h

    
def heuristic(node, values):
    return values[node]

def AStarSearch(start, end):
    path = {}
    distance = {}
    q = priorityQueue()
    h = makehuristikdict()
    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []
    while (q.isEmpty() == False):
        current = q.pop()
        expandedList.append(current)
        if (current == end):
            break
        for new in romania[current]:
            g_cost = distance[current] + int(new.distance)
            #print(new.cit, new.distance, "now: "+ str(distance[current]),g_cost)
            if (new.city not in distance or g_cost < distance[new.city]):
                distance[new.city] = g_cost
                f_cost = g_cost + heuristic(new.city, h)
                #print(f_cost)
                q.push(new.city, f_cost)
                path[new.city] = current
    printoutput(start, end, path, distance, expandedList)
            
def printoutput(start, end, path, distance, expandedlist):
    finalpath = []
    i = end
    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
    print("A-star Agorithm for Romania Map")
    print("\tArad => Bucharest")
    print("========================================================================")
    print("List of Cities that are Expanded:" + str(expandedlist))
    print("Total Number of Cities that are Expanded:" + str(len(expandedlist)))
    print("========================================================================")
    print("Cities in Final path: " + str(finalpath))
    print("Total Number of cities in final path are:" + str(len(finalpath)))
    print("Total Cost:"+ str(distance[end]))
    
def main():
    src = "Arad"
    dst = "Bucharest"
    makehuristikdict()
    AStarSearch(src, dst)
    
if __name__ =="__main__":
    main()
    
            
        