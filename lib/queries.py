CONST_QUERY = '''
    ADD CONSTRAINT ON (n: %s)
    ASSERT n.%s IS UNIQUE
'''

MERGE_NODE_QUERY = '''
    MERGE (:%s {name: "%s", iden: "%s"})
'''

CREATE_EDGE_QUERY = '''
    MATCH (a: %s), (b: %s)
    WHERE a.iden = "%s" AND b.iden = "%s"
    CREATE (a)-[:%s]->(b)
'''