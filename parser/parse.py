import os
import redcap_parser as rp
import data2docx as d2d


if __name__ == '__main__':
    
    filename = "/home/guillaume/Documents/redcap/data.xlsx"
    ws       = rp.import_excel(filename)
    

   
    

    data_val, col_names = d2d.save2word_document(ws)
    
    
    
#%%

col_names, data_val = rp.extrat_row(ws,1)   
    
col_names    
data_val

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
    