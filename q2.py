# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 03:07:03 2025

@author: zacha
"""

#Q2#

def find_and_replace(lst, find_val, replace_val):

    
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    return [replace_val if x == find_val else x for x in lst]


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# ans: [1, 5, 3, 4, 5, 5]
# - ["apple", "banana", "apple"], "apple", "orange"
# ans: ['orange', 'banana', 'orange']

