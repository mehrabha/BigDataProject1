# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:08:32 2020

@author: mehra
"""

NUM_RESULTS = 10

import csv
from pymongo import MongoClient


class DiseaseDb:
    def __init__(self):
        self.client = MongoClient()
        self.client.drop_database('hetionet_mhafiz')
        self.db = self.client['hetionet_mhafiz']
        
    def find(self, disease_id):
        nodes = self.db['nodes'] # the collection
        disease = nodes.find_one({'id': disease_id})
        
        # Check if disease in collection
        if disease:
            return disease
        else:
            return None
    
    def loadDataFromTSV(self, filesrc1, filesrc2):
        nodes = self.db['nodes'] # the collection
        
        # open nodes file and convert to dict
        print('Reading nodes.tsv...', end = '')
        infile = open(filesrc1)
        nodes_dicts = csv.DictReader(infile, dialect='excel-tab')
        
        nodes_dict = {}
        for row in nodes_dicts:
            nodes_dict[row['id']] = row
        print('DONE', end = '\n\n')
        
        # open edges file
        print('Reading edges.tsv...', end = '')
        infile2 = open(filesrc2)
        edges_dict = csv.DictReader(infile2, dialect='excel-tab')
        #infile2.close()
        print('DONE', end = '\n\n')
        
        
        # Search for relations:
        #   CtD, CpD
        #   DuG, DaG, DdG
        #   DlA
        print('Finding relations...', end = '')
        for row in edges_dict:
            if row['metaedge'] == 'CtD':
                # add compound to disease
                compound_id = row['source']
                compound = nodes_dict[compound_id]
                disease_id = row['target']
                disease = nodes_dict[disease_id]
                
                if 'treatments' in disease:
                    disease['treatments'].append(compound['name'])
                else:
                    disease['treatments'] = [compound['name']]
                    
            if row['metaedge'] == 'CpD':
                # add compound to disease
                compound_id = row['source']
                compound = nodes_dict[compound_id]
                disease_id = row['target']
                disease = nodes_dict[disease_id]
                
                if 'palliatives' in disease:
                    disease['palliatives'].append(compound['name'])
                else:
                    disease['palliatives'] = [compound['name']]
                    
            if row['metaedge'] in {'DuG', 'DaG', 'DdG'}:
                # add gene to disease
                disease_id = row['source']
                disease = nodes_dict[disease_id]
                gene_id = row['target']
                gene = nodes_dict[gene_id]
                
                if 'genes' in disease:
                    disease['genes'].append(gene['name'])
                else:
                    disease['genes'] = [gene['name']]
                    
            if row['metaedge'] == 'DlA':
                # add anatomy to disease
                disease_id = row['source']
                disease = nodes_dict[disease_id]
                anatomy_id = row['target']
                anatomy = nodes_dict[anatomy_id]
                
                if 'anatomy' in disease:
                    disease['anatomy'].append(anatomy['name'])
                else:
                    disease['anatomy'] = [anatomy['name']]             
        print('DONE', end = '\n\n')
        
        # insert dict to nodes collection
        print('Adding nodes to database...', end = '')
        for key in nodes_dict:
            nodes.insert(nodes_dict[key])
        print('DONE', end = '\n\n')