import redcap_parser as rp
import data2docx as d2d
from docx import Document
from docx.shared import Pt
import utilities as util



if __name__ == '__main__':
    
    filename = "/home/guillaume/Documents/redhat/data.xlsx"
    ws       = rp.import_excel(filename)
       

    

    
#%% Test word document to component


col_names, data_val = rp.extrat_row(ws,2)   
comp = util.rowdata2component(ws,col_names,data_val)    

document = Document()

style = document.styles['Normal']
font = style.font
font.name = 'Arial'
font.size = Pt(6)
   

d2d.component2docx(document,comp)
   

document.save('test.docx')    



#%%  Put all cases in one


  

document = Document()
style = document.styles['Normal']
font = style.font
font.name = 'Arial'
font.size = Pt(6)
   
num_rows = ws.max_row


for i in range(2,num_rows):
    
    print i

    col_names, data_val = rp.extrat_row(ws,i)   
    comp = util.rowdata2component(ws,col_names,data_val)  
    d2d.component2docx(document,comp)
   

document.save('test2.docx')    





