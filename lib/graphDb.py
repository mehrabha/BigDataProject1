import csv
from lib import queries
from py2neo import Graph, Node, Relationship

translator = {'C': 'Compund',
              'D': 'Disease',
              'G': 'Gene',
              'A': 'Anatomy'}
    
class GraphDb:
    def __init__(self):
        print('Initializing Database at port 7687...', end = '')
        self.db = Graph()
        #self.db.delete_all()
        print('DONE', end = '\n\n')
    
    def __del__(self):
        print('Cleaning up database...', end = '')
        self.db.delete_all()
        print('DONE', end = '\n\n')
        
    def loadDataFromTSV(self, filesrc1, filesrc2):
        db = self.db
        # open nodes file and convert to dict
        print('Reading nodes.tsv...', end = '')
        infile = open(filesrc1)
        nodes_dicts = csv.DictReader(infile, dialect='excel-tab')
        print('DONE', end = '\n\n')
        
        # open edges file
        print('Reading edges.tsv...', end = '')
        infile2 = open(filesrc2)
        edges_dict = csv.DictReader(infile2, dialect='excel-tab')
        print('DONE', end = '\n\n')
        
        # create nodes and add to graph
        i = 0
        added = 0
        print('Adding nodes...')
        for row in nodes_dicts:
            # (:kind {name, iden})
            query = queries.MERGE_NODE_QUERY % (row['kind'], row['name'], row['id'])
            db.run(query)
            added += 1
            
            # Print progress
            i += 1
            if i > 1999:
                print('Adding nodes...' + str(added) + ' added')
                i = 0
                # create nodes and add to graph
        print('\n' + str(added) + ' nodes added\n')
        
        ''' Make nodes unique
        print('Adding constraints...', end = '')
        for key in translator:
            query = queries.CONST_QUERY % (translator[key], 'iden')
            db.run(query)
        print('DONE', end = '\n\n')
        '''
        
        # create edges and add to graph
        i = 0
        added = 0
        print('Adding edges...')
        for row in edges_dict:
            edge = row['metaedge']
            a_iden = row['source']
            a_kind = translator[edge[0]]
            b_iden = row['target']
            b_kind = translator[edge[2]]
            
            # (:kind {name})-[edge]->(:kind {name})
            query = queries.CREATE_EDGE_QUERY % (a_kind, 
                                                b_kind, 
                                                a_iden, 
                                                b_iden, 
                                                edge)
            db.run(query)
            added += 1
            
            # Print progress
            i += 1
            if i > 999:
                print('Adding edges...' + str(added) + ' added')
                i = 0
        print('\n' + str(added) + ' edges added\n')    