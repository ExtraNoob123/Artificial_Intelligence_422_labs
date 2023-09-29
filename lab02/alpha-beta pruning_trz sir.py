# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# alpha-beta pruning    #python code

# Returns optimal value for current player
#(Initially called for root and maximizer)
def minimax(values, nodeIndex, position, alpha, beta, maximizingPlayer):
    
    
    # Terminating condition. i.e
    # leaf node is reached    
    if position == 3: # depth = 3
        return values[nodeIndex]
    
    if maximizingPlayer:
        
        maxEval = float('-inf') #-infinity #-1000
        
        # Recur for left and right children
        for child in range(0, 2):
            
            eval = minimax(values, (nodeIndex *2 + child), position + 1, alpha, beta, False)
            
            maxEval = max(maxEval, eval)
            
            alpha = max(alpha, eval)
            
            # Alpha Beta Pruning
            if beta <= alpha:
                break
            
        return maxEval
    
    else:
        minEval  = float('inf') #+infinity #1000
        
        # Recur for left and
        # right children        
        for child in range(0, 2):
            
            eval = minimax(values, (nodeIndex *2 + child), position + 1, alpha, beta, True)
            
            minEval = min(minEval, eval)
            beta = min(beta, eval)
           
            # Alpha Beta Pruning
            if beta <= alpha:
                break
            
        return minEval
    
#initial call
# Driver Code
if __name__ == "__main__":
  
    values1 = [3, 5, 6, 9, 1, 2, 0, -1] 
        
    print("The optimal value is :", minimax(values1, 0, 0, float('-inf'), float('inf'), True))


