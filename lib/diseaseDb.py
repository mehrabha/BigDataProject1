# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:08:32 2020

@author: mehra
"""

import csv
from pymongo import MongoClient


class DiseaseDb:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['hetionet']
        
    def loadDataFromCSV(self, filesrc):
        nodes = self.db['nodes']
        # open file and convert to dict
        print('Reading file...', end = '')
        infile = open(filesrc)
        nodes_dict = csv.DictReader(infile, dialect='excel-tab')
        print('DONE', end = '\n\n')
        # insert dict to nodes collection
        print('Adding entries to database...', end = '')
        for row in nodes_dict:
            nodes.insert_one(row)
        print('DONE', end = '\n\n')