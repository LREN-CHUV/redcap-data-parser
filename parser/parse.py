import os
import redcap_parser as rp
import data2docx as d2d


if __name__ == '__main__':
    
    filename = "/home/guillaume/Documents/redhat/data.xlsx"
    ws       = rp.import_excel(filename)
    index    = rp.col_not_checked(ws)

    

    
#%% Save data as word document


    data_val, col_names = d2d.save2word_document(ws,index)




