# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 19:48:24 2023

@author: user
"""

tree = {'A': [['E', 75], ['C', 118], ['Si', 140]],
        'B': [['E', 75], ['Si', 151]],
        'C': [['A', 118], ['G', 111]],
        'D': [['Z', 85], ['N', 98], ['H', 142]],
        'E': [['B', 71], ['A', 75]],
        'F': [['Q', 87]],
        'G': [['C', 111], ['L', 70]],
        'H': [['D', 142], ['Q', 92]],
        'L': [['G', 70], ['V', 75]],
        'N': [['D', 98], ['T', 86]],
        'O': [['Si', 99], ['Z', 211]],
        'P': [['R', 97], ['S', 138], ['Z', 101]],
        'Q': [['H', 92], ['F', 87]],
        'R': [['Si', 80], ['S', 146], ['P', 97]],
        'S': [['D', 120], ['R', 146], ['P', 138]],
        'T': [['L', 75], ['S', 120]],
        'Si': [['B', 151], ['A', 140], ['R', 80], ['O', 99]],
        'Gu': [['Z', 90]],
        'Z': [['O', 211], ['P', 101], ['Gu', 90], ['D', 85]]} 


heuristic = {'A': 366, 'B': 380, 'C': 329, 'D': 80, 'E': 374, 'F': 234, 'G': 244, 'H': 199, 'L': 241, 'N': 151, 
             'O': 176, 'P': 100, 'Q': 226, 'R': 193, 'S': 160, 'T': 161, 'V': 242, 'Si': 253, 'Gu': 77, 'Z': 0}

cost = {'A': 0}     #total cost for nodes visited

def AStarSearch():
    global tree, heuristic
    closed = []
    opened = [['A', 366]]
    
    '''find the visited nodes // closed'''
    while True:
        fn = [i[1] for i in opened]
        chosen_index = fn.index(min(fn))
        node = opened[chosen_index][0]
        closed.append(opened[chosen_index])
        del opened[chosen_index]
        if closed[-1][0] == 'G':
            break
        for item in tree[node]:
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue 
            cost.update({item[0]: cost[node] + item[1]})
            fn_node = cost[node] + heuristic[item[0]] + item[1]
            temp = [item[0], fn_node]
            opened.append(temp)
            
            
    '''find the optimal sequence'''
    trace_node = 'G'
    optimal_sequence = ['G']
    for i in range(len(closed)-2, -1, -1):
         check_node = closed[i][0]
         if trace_node in [children[0] for children in tree[check_node]]:
             children_costs = [temp[1] for temp in tree[check_node]]
             children_nodes = [temp[0] for temp in tree[check_node]]
             
             if cost[check_node] + children_costs[children_nodes.index(trace_node)] == cost[trace_node]:
                 optimal_sequence.append(check_node)
                 trace_node = check_node
    
    #print(opened)
    optimal_sequence.reverse()
    return closed, optimal_sequence
    
if __name__ == '__main__':
    visited_nodes, optimal_nodes = AStarSearch()
    print('visited nodes: ' + str(visited_nodes))
    print('optimal nodes sequence: ' + str(optimal_nodes))
    
    
    
    