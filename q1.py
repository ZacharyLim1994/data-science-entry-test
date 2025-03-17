# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 03:01:48 2025

@author: zacha
"""

#q1#
def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if isinstance(x,(int,float)) and isinstance(y,(int,float)):
        return y,x;
    else:
        return -1;


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# ans: -1
# - 9, 17
# ans: (17,9)
