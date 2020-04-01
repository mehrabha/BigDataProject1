# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:08:32 2020

@author: mehra
"""

from lib import diseaseDb

FILE1_DIR = './data/nodes.tsv'
FILE2_DIR = './data/edges.tsv'

OPTIONS = '''
Options:
   [1] Info about a disease
   [2] Treatment options for a new disease
   [3] Exit
'''
OPTIONS2 = '''
Options:
   [1] Find info about another disease
   [2] Return to main menu
'''


print('Welcome to HetioNet!')
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
        searching = '1'
        db = diseaseDb.DiseaseDb()
        db.loadDataFromTSV(FILE1_DIR, FILE2_DIR)
        
        while searching == '1':
            disease_id = input('Enter disease ID: ')
            
            # Search database for disease
            disease = db.find(disease_id)
            
            if disease:
                # Disease found
                print('\nInfo about disease with ID: ' + disease_id)
                print('    Name: ' + disease['name'])
                
                if 'treatments' in disease:
                    # Treatments found
                    print('    Treatments:')
                    for treatment in disease['treatments']:
                        print('      - ', treatment)
                        
                if 'palliatives' in disease:
                    # Palliatives found
                    print('    Palliatives:')
                    for palliative in disease['palliatives']:
                        print('      - ', palliative)
                        
                if 'anatomy' in disease:
                    # Palliatives found
                    print('    Localizes:')
                    for anatomy in disease['anatomy']:
                        print('      - ', anatomy)                

                if 'genes' in disease:
                    print('    Genes:')
                    for gene in disease['genes']:
                        print('      - ', gene)
                print(OPTIONS2)
                searching = input('Select: ')
            else:
                print('Disease with ID:', end = ' ')
                print(disease_id + ' not found in database')
    elif state == 2:
        print('[2] Treatment options for a new disease')
    else:
        print('[3] Exit')
        print('Thank you for using HetioNet!')
        break