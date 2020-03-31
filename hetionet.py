# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:08:32 2020

@author: mehra
"""

from lib import diseaseInfo

MESSAGE = '\nWelcome to HetioNet!'
OPTIONS = '''
Options:
    [1] Info about a disease
    [2] Treatment options for a new disease
    [3] Exit
'''

print(MESSAGE)
while True:
    print(OPTIONS)
    state = None
    
    while state == None:
        # Check input
        state = input('Select: ')
        try:
            state = int(state)
        except ValueError:
            print('Input must be an integer.')
        
    if state == 1:
        diseaseInfo.getDiseaseById()
    elif state == 2:
        print('[2] Treatment options for a new disease')
    else:
        print('[3] Exit')
        print('Thank you for using HetioNet!')
        break