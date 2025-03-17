# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 03:29:27 2025

@author: zacha
"""

def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    while True:
        num = lst.pop(0)
        if num<0:
            return num
        elif len(lst) == 0:
            return "No negatives"


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# Ans: -1
# - [2, 10, 7, 0]
# Ans: 'No negatives'