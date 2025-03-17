# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 03:26:05 2025

@author: zacha
"""

def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not isinstance(num,(int,float)):
        return False
    elif num % divisor ==0:
        return True
    else:
        return False
    


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# Ans: True
# - 7, 3
# Ans: False