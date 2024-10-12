#!/usr/bin/python3
""" The Pascal Triangle Project"""

def pascal_triangle(n):
    """ Return a list of lists representing Pascal's Triangle"""
    if n <= 0:
        return []

    p_triangle = [0] * n

    for a in range(n):
        # Define rows and initialize the first and last elements as 1
        current_row = [0] * (a + 1)
        current_row[0] = 1
        current_row[-1] = 1
        
        # Fill the internal elements of the row if there are any
        for b in range(1, a):
            current_row[b] = p_triangle[a - 1][b - 1] + p_triangle[a - 1][b]
                
        p_triangle[a] = current_row
        
    return p_triangle
