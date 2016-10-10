# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 14:10:49 2016

@author: guillaume
"""

import redcap_parser as rp
import data2docx as d2d
import utilities as util
from docx import Document
from docx.shared import Pt
import time
import datetime

def parse(filename):

    data     = rp.import_csv(filename)

    num_rows = len(data)-1
    comps    = []


    for row_id in range(1,num_rows):

        col_names, data_val = rp.csv2data(data,row_id)
        comp                = util.row2comp(col_names,data_val)
        comps.append(comp)
        
    return comps


def all_task2docxs(comps):
    

    all_tasks = []

    for comp in comps:
        print 'Subject: ', comp.subject_ID, ' num_tasks: ', len(comp.tasks)
        all_tasks.extend(comp.tasks)
        
    return comps    
    print 'total number of tasks: ', len(all_tasks)    
    
    
    document = Document()

    style = document.styles['Normal']
    font = style.font
    font.name = 'Arial'
    font.size = Pt(6)

    d2d.sorted_task2docx(document,all_tasks)

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')

    document.save('redcap_data_' + st + '.docx')
    
    
    