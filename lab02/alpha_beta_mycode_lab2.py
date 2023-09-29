# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# alpha-beta pruning    #python code

import math

import random

#Student_Id = input("Enter your student ID: ")
Student_Id = '17564039'
print()

if "0" in Student_Id:
    Student_Id = Student_Id.replace("0", "8")
    
if len(Student_Id) != 8:
    raise ValueError("Incorrect format - must be 8 digit")

min_required = int(Student_Id[-1] + Student_Id[-2]) # 56

max_achieved = int(min_required * 1.5) # 84

mid_l = int(Student_Id[3]) # value in 4th position #8

mid_h = int(Student_Id[4]) # value in 5th position #5

values1 = random.sample(range(mid_h , max_achieved+1), 8)

#print(values1)

# Returns optimal value for current player
#(Initially called for root and maximizer)
def minimax(values, nodeIndex, position, alpha, beta, maximizingPlayer):
    
    
    # Terminating condition. i.e
    # leaf node is reached    
    if position == 3: # depth = 3
        return values[nodeIndex]
    
    if maximizingPlayer:    #Optimus Prime's turn
        
        maxEval = float('-inf') #-infinity #-1000
        
        # Recur for left and right children
        for child in range(0, 2):
            
            eval = minimax(values, (nodeIndex *2 + child), position + 1, alpha, beta, False)
            
            maxEval = max(maxEval, eval)
            
            alpha = max(alpha, maxEval)
            
            # Alpha Beta Pruning - cutting off unwanted edge
            if beta <= alpha:
                break
            
        return maxEval
    
    else:   #Megatron's Turn
        minEval  = float('inf') #+infinity #1000
        
        # Recur for left and
        # right children        
        for child in range(0, 2):
            
            eval = minimax(values, (nodeIndex *2 + child), position + 1, alpha, beta, True)
            
            minEval = min(minEval, eval)
            beta = min(beta, minEval)
           
            # Alpha Beta Pruning
            if beta <= alpha:
                break
            
        return minEval
    
#initial call
# Tester Code
if __name__ == "__main__":
    count = 0
    points = []
  
    #values1 = [66, 74, 14, 73, 19, 26, 32, 40] 
    result = minimax(values1, 0, 0, float('-inf'), float('inf'), True)
    
    if result >= min_required:
        Won = 'Optimus Prime'
        count = count + 1
    else:
        Won = 'Megatron'
            
      
    
    print("Generated 8 random points between the minimum and maximum point limits:")
    print(str(values1)[1:-1])
    print("Total points to win:", min_required)    
    print("Achieved point by applying alpha-beta pruning =", result)
    print("The winner is "+ Won)
    print()
    

    
    for i in range(mid_l):
        result = minimax(values1, 0, 0, float('-inf'), float('inf'), True)
    
        if result >= min_required:
            Won = 'Optimus Prime'
            count = count + 1  
        else:
            Won = 'Megatron'
            
            
        points.append(result) 
        random.shuffle(values1)
    
    print("After the shuffle:")
    print("List of all points values from each shuffles:")
    print(points)
    print("The maximum value of all shuffles:", max(points))
    print("Won",count,"times out of",mid_l," number of shuffles")