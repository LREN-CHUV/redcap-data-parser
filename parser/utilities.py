#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:46:48 2016

@author: guillaume
"""
from component import Component

   
    
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
        print '[Error] Could not find: which building block your component belongs to ?'
        

    index = find('Participant ID',col_names)
    if index != -1:
        comp.subject_ID = data_val[index]
    else:
        print '[Error] Could not find:  Participant ID' 
        comp.subject_ID = 'None' 
    
    # Component name
    
    index = find('Name of this component',col_names)
    if index != -1:
        comp.component = data_val[index]
    else:
        print '[Error] Could not find:  Name of this component'

        
        
    # Contributing task(s)    
    index = find('Task number attached to this component',col_names)
    if index != -1:
        comp.contribution = data_val[index]
    else:
        print '[Error] Could not find:  Task number attached to this component'


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