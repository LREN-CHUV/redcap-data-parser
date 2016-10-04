import os
import redcap_parser as rp
import data2docx as d2d
from component import Component
import re
from docx import Document



if __name__ == '__main__':
    
    filename = "/home/guillaume/Documents/redhat/data.xlsx"
    ws       = rp.import_excel(filename)
       
    
    com = Component()
    #data_val, col_names = d2d.save2word_document(ws)
    
    
    
    
#%%

col_names, data_val = rp.extrat_row(ws,2)   
    
col_names    
data_val

def find(name,names):
    """
        returns the index of the the first occurence of name in names
    
    """
    
    try:
        index = names.index(name)
    except ValueError:
        index = -1
        
    return index        
    

def find_all(name,names):
    indices = [i for i, x in enumerate(names) if x == name]
    return indices           
  
   

#%% function takes a one row and converts it to an object

def rowdata2component(ws,col_names,data_val):
    """
        Converts the a row extracted from a excel sheet to one Component
            
    """
    
    comp = Component()
    
    
    # Extact the various components
    
    # Component name
    
    index = find('Name of this component',col_names)
    if index != -1:
        comp.component = data_val[index]
        
        
    # Contributing task(s)    
    index = find('Task number attached to this component',col_names)
    if index != -1:
        comp.contribution = data_val[index]


    # Description
    index = find('Short Description of this component',col_names)
    if index != -1:
        print data_val[index]
        comp.short_desc = data_val[index]
    else:
        print '[Error] Could not find a short description of this component'


    # Dependencies
    indices = find_all('Which other building blocks does your component need ?',col_names)  
    for index in indices:
        
        elements = data_val[index].split('>')
        elements = [x.strip() for x in elements]

        dtype = elements[0]
                            
        print elements

        if dtype== 'DATA':
            
            if elements[1] == 'Hospital Data':
                comp.add_data('hospital',elements[2])
            elif elements[1] == 'Reference data':
                comp.add_data('reference',elements[2])
            else:
                print 'Error no such DATA > ' +  elements[1] + ' not implemented!'
            
        elif dtype == 'SOFTWARE':
            com.add_soft(elements[1],elements[2])
        else:
            print 'Error no such element [ ' +  elements[0] + ' ] implemented'
            
                    
    return comp
    
#%% component -> word document


def one_line_2_docx(p,name,value=''):
    """
        Prints to word document format:
            
            <b>name</b>value\n
    
    """
    # print component    
    p.add_run(name).bold = True
    if value != '':
        p.add_run(value)
    p.add_run('\n')
    

def dependencies2docx(wdoc,data_hosp,data_ref,soft):
    """
        
    Takes Data and software information and puts it into a table
    
    Prameters
    ---------
     
    wdoc: python-docx word document object
    data_hosp: DATA > Hospital Data > [] list
    data_ref : DATA > Reference Data > [] list

    """
    
    table = wdoc.add_table(rows=3, cols=3)
    
    data_hosp = ', '.join(data_hosp)
    data_ref  = ', '.join(data_ref)
    
    print data_hosp
    
    # Hospital Data
    row = table.rows[0]
    row.cells[0].text = 'DATA'
    row.cells[1].text = 'Hospital'
    row.cells[2].text = data_hosp

    # Reference Data
    row = table.rows[1]
    row.cells[1].text = 'Reference'
    row.cells[2].text = data_ref

    # Reference Data
    row = table.rows[2]
    row.cells[0].text = 'SOFTWARE'



def releases2docx(wdoc):
    pass
    
    
    

    
def component2docx(document,comp):
    
    p = document.add_paragraph()
    
    one_line_2_docx(p,'Component: ',            comp.component)
    one_line_2_docx(p,'Contributing task(s): ', comp.contribution)
    one_line_2_docx(p,'Description: ',          comp.short_desc)
    
    # Prior Dependencies table:
    one_line_2_docx(p,'Dependencies:')
    
    #  add table
    dependencies2docx(document,comp.data_hosp,comp.data_ref,comp.soft)
        
   
    
    
    
    

    
#%% Test word document to component


document = Document()

document.add_heading('redcap_data', 0)
document.add_paragraph('automatically generated from python')
    

component2docx(document,comp)
   

document.save('test.docx')    

 
    
 #%%

 
comp = rowdata2component(ws,col_names,data_val)


#%%

def get_question_type(str1):
    if len(re.findall('\\b(select one or many)\\b', str1)) > 0:
        return '(select one or many)'
    elif len(re.findall('\\b(select one)\\b', str1)) > 0:
        return '(select one)' 
    else:
        return "'(choice='"
    

    

def get_question(str1,str2):
    index = str1.find(str2)
    if index > 1:
        return str1[0:index-1]
    else:
        return ''   

def get_answer(str1,str2='choice='):
    len_str1 = len(str1)
    len_str2 = len(str2)
    index = str1.find(str2) + len_str2
    
    if index > 1 & index < len_str1:
        return str1[index+1:len_str1-2]
    else:
        return ''   


#%% extract data from row

col_names = []
data_val  = []

num_col = ws.max_column
row_id  = 2;

for j in range(1,11):
    
    col_name = str(ws.cell(row=1,column=j).value)
    val      =     ws.cell(row=row_id,column=j).value
    
    if isinstance(val,unicode):
        data_j = val.encode('ascii','ignore')
    else:
        data_j = str(val)
        

    if data_j == 'Checked':

        question_type = get_question_type(col_name)        
        question = get_question(col_name,question_type)    
       
        col_name = question
        data_j   = answer           
        append   = True
    elif data_j == 'Unchecked':
        append   = False
    else:
        append   = True
        
    if col_name == 'To which building block your component belongs to ? (select one)':
        col_name = 'To which building block your component belongs to ?'         
        

    if append:  
        col_names.append(col_name)
        data_val.append(data_j)    
   
        #%%
       

           
        
       
         
   

#%%
   

        
        
    
#%% string processing

str1 = "'To which building block your component belongs to ? (select one)'"    
    
    
match = re.findall('\\b(select one)\\b', str1)

        
get_question(str1,'(select one)')
get_answer(str1,'choice=')

#%% test 2

str1 = "Target User (choice='General Public')"

get_question(str1,'(select one or many)')
get_question(str1,'(choice=')

get_answer(str1,'choice=')    
    


#%% macthing regular expression


p = re.compile('\s > \s > \s')

#%%



str1 = 'DATA > Hospital Data > Lille Hospital'


print p.match(str1)