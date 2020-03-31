# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:08:32 2020

@author: mehra
"""

from pymongo import MongoClient
import pandas as pd

class DiseaseDb:
    def _init_(self):
        self.client = MongoClient()
        self.db = self.client['hetionet']
        
    def loadData(csv):
    