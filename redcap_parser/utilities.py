#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:46:48 2016

@author: guillaume
"""
from component import Component
from task import Task
from  __builtin__ import any as b_any

def unicode2ascii(value):
    if isinstance(value,unicode):
       return value.encode('ascii','ignore')
    else:
       return str(value)
       
def remove_quotations(string):
    if string.startswith('"') and string.endswith('"'):
        return string[1:-1]
    else:
        return string
    
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
    return [i for i, x in enumerate(names) if x == name]


def find_all_contains(name,names):
    """
        All names of release contain the following:
            
            'Planned functionalities at'
    """
    return [i for i, x in enumerate(names) if name in x]                
            

def get_data(name,col_names,data_val):
    index = find(name,col_names)    
    if index != -1:
        return data_val[index]
    else:
        print '[Error] Could not find: ', name
        return 'None'
            
            
def row2comp(col_names,data_val):

    comp = Component()
    
    
    comp.subject_ID         = get_data('Participant ID',col_names,data_val)
    comp.survey_timestamp   = get_data('Survey Timestamp',col_names,data_val)
    comp.task_leader        = get_data('Task leader name',col_names,data_val)
     


    task_block_idx      = get_task_idx_blocks(col_names)
   
    tasks               = []

    for idx in task_block_idx:
        s_idx = idx[0]
        e_idx = idx[1]
        #print s_idx, e_idx
        task = rowdata2task(col_names[s_idx:e_idx],data_val[s_idx:e_idx])
        if task.name != 'None':
            tasks.append(task)

    comp.tasks = tasks    
    return comp
            
            
            
            
def rowdata2task(col_names,data_val):
    """
        Converts the a row extracted from a excel sheet to one Component
        
        col_names : column names of excel sheet which correspon to one component.
        data:val  : data values of associated with column names.
         
    """
    
    task = Task()
    
    """
    
        - Task number attached to this component
        - Name of this component

        - To which building block your component belongs to ?
        - Which other building blocks does your component need ?

        - Short description of this component

        - Planned functionalities at X   
        - Short description of potential use case
       
    """
    
    
    # TASK NUMBER
    
    task.task_number = get_data('Task number attached to this component',col_names,data_val)
        
    # TASK NAME
    
    task.name        = get_data('Name of this component',col_names,data_val)
       
    # BUILDING NEEDS (only one of these)
    
    index = find('To which building block your component belongs to ?',col_names)  
    elements = data_val[index].split('>')
    task.build_block_belong = [x.strip() for x in elements]    
        
                               
    # OTHER BUILDING BLOCKS NEEDED (multiple ones!)
    
    indices = find_all('Which other building blocks does your component need ?',col_names)  
    for idx in indices:
        elements = data_val[idx].split('>')
        task.add_other_build_block([x.strip() for x in elements])                                   
                              
                               
    # SHORT DESCRIPTION
        
    task.short_desc_comp = get_data('Short Description of this component',col_names,data_val)

    # PLANNED FUNCTIONALITY       
    
    idx = find_all_contains('Planned functional',col_names)
    
    for i in idx:
        if data_val[i] != 'None':
            task.planned_functionality[col_names[i]] = data_val[i]
            
    # USERS
            
    idx = find_all('Target User',col_names)
    users = ''
    for i in idx:
        users = users + data_val[i] + ' '

    task.users = users        
        
    # SHORT DESCRIPTION OF POTENTIAL USE CASE
       
    task.short_desc_usecase = get_data('Short description of potential use case',col_names,data_val)
                        
    return task
    
def get_task_idx_blocks(col_names):
    task_idx = find_all('Task number attached to this component',col_names)
    task_block_idx = []

    for i in range(0,len(task_idx)-1):
    
        s_idx = task_idx[i]
        e_idx = task_idx[i+1]-1
    
        task_block_idx.append([s_idx,e_idx])

    
    s_idx = task_idx[len(task_idx)-1]
    e_idx = len(col_names)-1
    
    task_block_idx.append([s_idx,e_idx])
    return task_block_idx

            
def rowdata2component(ws,col_names,data_val):
    """
        Converts the a row extracted from a excel sheet to one Component
            
    """
    
    comp = Component()
    
    
    # Extact the various components
    index = find('To which building block your component belongs to ?',col_names)
    if index != -1:
        
        elements = data_val[index].split('>')
        comp.titles = [x.strip() for x in elements]
        """
         SOFTWARE
         Data Factory (DF): 
         Feature Engineering  
        """
                    

    else:
        print '[Warning utilities.py] Could not find: which building block your component belongs to ?'
        

    index = find('Participant ID',col_names)
    if index != -1:
        comp.subject_ID = data_val[index]
    else:
        print '[Warning utilities.py] Could not find:  Participant ID' 
        comp.subject_ID = 'None' 
    
    # Component name
    
    index = find('Name of this component',col_names)
    if index != -1:
        comp.component = data_val[index]
    else:
        print '[Warning utilities.py] Could not find:  Name of this component'

        
        
    # Contributing task(s)    
    index = find('Task number attached to this component',col_names)
    if index != -1:
        comp.contribution = data_val[index]
    else:
        print '[Warning utilities.py] Could not find:  Task number attached to this component'


    # Description
    index = find('Short Description of this component',col_names)
    if index != -1:
        print data_val[index]
        comp.short_desc = data_val[index]
    else:
        print '[Warning utilities.py] Could not find a short description of this component'


    # Dependencies
    indices = find_all('Which other building blocks does your component need ?',col_names)  
    for index in indices:
        
        elements = data_val[index].split('>')
        elements = [x.strip() for x in elements]

        dtype = elements[0]
                            
        #print elements

        if dtype == 'DATA':
            
            if elements[1] == 'Hospital Data':
                comp.add_data('hospital',elements[2])
            elif elements[1] == 'Reference data':
                comp.add_data('reference',elements[2])
            else:
                print 'Error no such DATA > ' +  elements[1] + ' not implemented!'
            
        elif dtype == 'SOFTWARE':
            comp.add_soft(elements[1],elements[2])
        else:
            print 'Error no such element [ ' +  elements[0] + ' ] implemented'
      

    # Releases       
    
    idx = find_all_contains('Planned functional',col_names)
    
    for i in idx:
        if data_val[i] != 'None':
            comp.add_release(col_names[i],data_val[i])
            
            
    # Use Cases            
    idx = find_all('Target User',col_names)
    users = ''
    for i in idx:
        users = users + data_val[i] + ' '
        
    idx = find('Short description of potential use case',col_names)
    desc = data_val[idx]
    
    comp.add_usecase(users,desc)
    
    
    
                        
    return comp
    
    
def get_all_tasks(comps):
    all_tasks = []

    for comp in comps:
        print 'Subject: ', comp.subject_ID, ' num_tasks: ', len(comp.tasks)
        all_tasks.extend(comp.tasks)    
    return all_tasks

    
def has_tasks(summary_data,values,col_idx):
   """
        Check if summary_data has these particular values.    
    
        summary_data: list : N x 4
                
   """                
    
   num_rows = len(summary_data) 
   num_val  = len(values)   
   
   has_v    = [False] * num_val

   for i in range(0,num_rows):
       task = summary_data[i][col_idx] 
       
       print task
       
       for j in range(0,num_val):
           print 'values[', j, ']: ', values[j]
           if values[j] in task:
               has_v[i] = True
               j = num_val
 
    
   return has_v
    
    
def dic2str(dic):
    st = ''
    for key in dic:   
        st = st + str(key) + ': ' + ', '.join(dic[key]) + '   |   '
    return st
    

def get_dependencies(task,dtype=0):

    if dtype == 0:

        dependencies = []

        if task.build_block_data:
            dependencies.extend(task.build_block_data.values()[0])
        
        if task.build_block_soft:
            dependencies.extend(task.build_block_soft.values()[0])

        if task.build_block_serv:
            dependencies.extend(task.build_block_serv.values()[0])

        if task.build_block_model:
            dependencies.extend(task.build_block_model.values()[0])

        if task.build_block_reports:
            dependencies.extend(task.build_block_reports.values()[0])   
            
        return dependencies    
            
    elif dtype == 1:
                   
         print 'dic2str(task.build_block_data): ', dic2str(task.build_block_data)  , 'key'        
         dependencies = ''
         dependencies = dependencies + dic2str(task.build_block_data) + dic2str(task.build_block_soft) + dic2str(task.build_block_serv) + dic2str(task.build_block_model) + dic2str(task.build_block_reports)
      
         return dependencies
         
    else:
        
        return []
    

def summary(comps,stype=0):      
    """
        Gets the summary from task
        
        Parameters
        ----------
        
        comps: list of objects of type Component
        
        stype : type of data summary
        
                - 0 
                - 1
                - 2 : for excel confusion matrix

    """    

    summary_data = []

    if stype == 0:

        for comp in comps:
            for task in comp.tasks:
                # ('SOFTWARE', 'Data Factory (DF)', 'Feature Engineering')
                if len(task.build_block_belong) == 3:
                    dep = get_dependencies(task,dtype=1)    
                    print dep
                    if dep == '':
                        dep = 'None'
                    summary_data.append([ task.build_block_belong[1] , task.build_block_belong[2], task.name, task.task_number, dep])

        

    elif stype == 1:   
        
     # should aways be three   
     #  [Component name ,  Planned functionalities at M18,  Planned functionality at M12, Planned functionalities at M24]
        for comp in comps:
            for task in comp.tasks:
                # ('SOFTWARE', 'Data Factory (DF)', 'Feature Engineering')
                val =  [task.name] + task.planned_functionality.values()
                if ''.join(val) != '': 
                    summary_data.append(val)
                    
                    
    elif stype == 2:
        for comp in comps:
            for task in comp.tasks:
                if len(task.build_block_belong) == 3:
                    
                    dep = get_dependencies(task)                    
                    summary_data.append({ 'name' : task.name, 'build' : task.build_block_belong[1], 'dep': dep })       
                
        # [  Component name |  Build  bl]                
            
    
    return summary_data    
    

    
def get_list_depenencies(summary):
    """
        
        summary[0] : dict
        
            keys: 'name', 'build', 'dep'
            
            summary[0]['name']  = 'Brain morphological features'
            summary[0]['build'] = 'Data Factory (DF)'
            summary[0]['dep']   = ['Lille Hospital', 'Tel Aviv Hospital', 'Milano Hospital', 'Freiburg Hospital', 'CHUV Hospital', 'Data Storage']

    """      

    all_dep = []
    for summ in summary:
        all_dep.extend(summ['dep'])
    
    
    return list(set(all_dep))    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    