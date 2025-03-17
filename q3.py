# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 03:18:56 2025

@author: zacha
"""

def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    dct[key]=value
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# Ans: {'name': 'Alice'}
# - {"age": 25}, "age", 26
# Ans: {'age': 26}