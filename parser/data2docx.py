#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 17:24:32 2016

@author: guillaume
"""

from docx import Document
from docx.shared import Inches
import redcap_parser as rp


def data2word(data_vals,col_names,document):
    """ 
        data_vals   : list 
        
        col_names   : list
    
        document    : word document 
    
    """
    subject_ID = data_vals[0]
    document.add_heading('Subject: ' + subject_ID, level=3)
    p = document.add_paragraph('')
    run = p.add_run()
    run.add_break()    

    for i in range(1,len(col_names)):
        col_name = col_names[i]
        data_val = data_vals[i]
        

        if data_val != 'None':
            run = p.add_run()
            run.font.bold = True
            run.add_text(col_name + '\n')
            run = p.add_run()
            run.font.bold = False
            run.add_text(data_val + '\n\n')

            
            run.add_break()    
   

def save2word_document(ws,index):
    document = Document()

    document.add_heading('redcap_data', 0)
    document.add_paragraph('automatically generated from python')

    num_rows = ws.max_row

    for i in range(1,num_rows):
        print 'subject: ', i
        data_val,col_names = rp.extrat_data_row(ws,i,index)
        data2word(data_val,col_names,document)

    document.save('redcap_python.docx')    
            