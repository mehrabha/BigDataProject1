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

DISCOVER_QUERY = '''
    MATCH (c:Compound)-[:CuG]->(:Gene)<-[:AdG]-(:Anatomy)<-[:DlA]-(d:Disease {iden: "%s"})
    WHERE NOT (c)-[:CtD]->(d)
    MATCH (c:Compound)-[:CdG]->(:Gene)<-[:AuG]-(:Anatomy)<-[:DlA]-(d:Disease {iden: "%s"})
    WHERE NOT (c)-[:CtD]->(d)
    RETURN DISTINCT c.name
'''