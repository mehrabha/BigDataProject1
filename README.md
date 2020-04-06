# BigDataProject1
Modeling of medical database.
Using python, mongodb and neo4j.

This application uses this network to solve the following problems:
* Find existing information about a disease and the available treatments.
* Find all drugs that can treat a new disease.

Requirements:
- Python
- mongodb
- pymongo
- Neo4j Desktop
- Py2neo

Prerequisite checks:
- ./data/ contains nodes.tsv and edges.tsv files
- Mongodb service is running at default port
- Neo4j service is running at default port
- Read/Write access to data files

To start, simply open a terminal in the base project directory and run command:
	python hetionet.py
