# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def minimax(position, depth, maximizingPlayer):
    
    if position == depth :
        return position
    
    if maximizingPlayer:
        maxEval = float('-inf') #-infinity
        for child in position:
            eval = minimax(child, depth - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval
    
    else:
        minEval  = float('inf') #+infinity
        for child in position:
            eval = minimax(child, depth - 1, True)
            minEval = min(minEval, eval)
        return minEval