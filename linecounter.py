# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:23:43 2020

@author: mehra
"""

lines = 0
with open('./data/nodes.tsv') as file:
    for row in file:
        lines += 1

print(lines)