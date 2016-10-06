import redcap_parser as rp
import data2docx as d2d
from docx import Document
from docx.shared import Pt
import utilities as util

import time
import datetime

from optparse import OptionParser
import os.path


def parse(filename):
    
    data     = rp.import_csv(filename)
    
    num_rows = len(data)-1
    comps    = []


    for row_id in range(0,num_rows):
    
        col_names, data_val = rp.csv2data(data,row_id)
        comp                = util.row2comp(col_names,data_val)
        comps.append(comp)

        
    all_tasks = []

    for comp in comps:
        print 'Subject: ', comp.subject_ID, ' num_tasks: ', len(comp.tasks)
        all_tasks.extend(comp.tasks)

    print 'total number of tasks: ', len(all_tasks)


    document = Document()

    style = document.styles['Normal']
    font = style.font
    font.name = 'Arial'
    font.size = Pt(6)
    
    d2d.sorted_task2docx(document,all_tasks)
    
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    document.save('redcap_data_' + st + '.docx')    
        
        

if __name__ == '__main__':
    
    parser = OptionParser()

    (options, args) = parser.parse_args()
    
    if len(args) == 1:
        filename = str(args[0])
        
        if os.path.isfile(filename):
            
            if filename.endswith('.csv'):
                
                    parse(filename)
                
            else:
                
                print '[Error] : filename should end with .csv'
            
            
        else:
            
            print '[Error] : path to ', filename, ' does not exist!'

        
        
    else:
        
        print '[Error]: parser only takes one file.csv as input'
    
    
    
    
    

    


   





