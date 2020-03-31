# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:08:32 2020

@author: mehra
"""

OPTIONS = '''
Options:
    [ENTER] Return to main menu
'''

def getDiseaseById():
    id = input('Enter disease id: ')
    print('Info about disease with ID ', id)
    input(OPTIONS)