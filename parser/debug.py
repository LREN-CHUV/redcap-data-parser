#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:11:32 2016

@author: guillaume
"""

import redcap_parser as rp
import data2docx as d2d
from docx import Document
from docx.shared import Pt
import utilities as util

if __name__ == '__main__':
    
    filename = "/home/guillaume/Documents/redhat/data3.csv"
    data     = rp.import_csv(filename)
        
    
    row_id = 0
    col_names, data_val = rp.csv2data(data,row_id)
    comp                = util.row2comp(col_names,data_val)


#%%

# Extracting components

num_rows            = len(data)-1
comps               = []


for row_id in range(0,num_rows):
    
    col_names, data_val = rp.csv2data(data,row_id)
    comp                = util.row2comp(col_names,data_val)
    
    print 'comp(', row_id,') has ', len(comp.tasks) ,' tasks'
    comps.append(comp)
       
    
#%% Print

print ' '
for comp in comps:
    print comp    
    print ' '
    
#%% import csv






    