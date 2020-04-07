import csv
from lib import queries
from py2neo import Graph, Node, Relationship

translator = {'C': 'Compound',
              'D': 'Disease',
              'G': 'Gene',
              'A': 'Anatomy'}
    
class GraphDb:
    def __init__(self):
        print('Initializing Database at port 7687...', end = '')
        self.db = Graph()
        print('DONE', end = '\n\n')
    
    def empty(self):
        print('Cleaning up database...', end = '')
        self.db.delete_all()
        print('DONE', end = '\n\n')
        
    def newTreatments(self, diseaseID):
        db = self.db
        print('Running query...', end = '')
        
        if len(diseaseID) > 0:
            query = queries.DISCOVER_QUERY % (diseaseID, diseaseID)
        else:
            query = queries.DISCOVER_ALL_QUERY
            
        treatments = db.run(query).data()
        print('DONE', end = '\n\n')
        
        if treatments:
            print('Suitable drugs found for disease with ID: ', diseaseID)
            for treatment in treatments:
                if len(diseaseID) > 0:
                    print('    - ' + treatment['c.name'])
                else:
                    # Print treatments with drugs:
                    print('    - ' + treatment['c.name'], end = ' ')
                    print('for disease: ' + treatment['d.name'])
        else:
            print('No suitable drugs found for disease with ID: ', diseaseID)
        
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
        discarded = 0
        print('Adding edges...')
        for row in edges_dict:
            edge = row['metaedge']
            
            if len(edge) > 3:
                edge = 'GgG'
            
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
            if edge in {'CrC', 'DlA', 'CuG', 'CdG', 'AuG', 'AdG', 'CtD'}:
                db.run(query)
                added += 1
                i += 1
            else:
                discarded += 1
                
            if i > 1999:
                print('Adding edges...' + str(added) + ' added', end = ', ')
                print(str(discarded) + ' discarded')
                i = 0
        print('\n' + str(added) + ' edges added\n')    