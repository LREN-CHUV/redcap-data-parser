#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:43:46 2016

@author: guillaume
"""

class Task:
    """
        Redcap task. Each subject can enter multiple tasks into the redcap
        database.
    
        fields:
        
        - Task number attached to this component
        - Name of this component
        - Short description of this component

        - To which building block your component belongs to ?
        
        - Which other building blocks does your component need ?
        
        - Planned functionalities at X   
        - Short description of potential use case
        
        
    """
    
    def __init__(self):
        
        self.task_number        = ''
        self.name               = ''
        self.short_desc_comp    = ''

        self.short_desc_usecase = ''       
        self.users              = []

        
        self.build_block_belong = [] # ('SOFTWARE', 'Data Factory (DF)', 'Feature Engineering')
       
        self.release             = dict()

 
        self.build_block_data    = dict()        
        self.build_block_soft    = dict()
        self.build_block_serv    = dict()

        """
            key: Planned functionality at M12    value: Report on access restrictions in the MIP 
        """
        self.planned_functionality   = dict()
        
        
        
        
        
        
        
   # def add_functionality(self,name,desc):
   #    
   #   if name in self.release:
   #       self.release[name].append(desc)
   #   else:
   #       self.release[name] = [desc]     

    def add_other_build_block(self,elem):
        """
            
            Result of elem <- Which other building blocks does your components need ?
            
            Parameters
            ----------
            
            elem[0] : DATA or SOFTWARE
                
            elem[1] : Hospital Data or Reference data or Data Factory (DF) 

            elem[2] : string            
            
            Example
            -------
        
        """
        
        if len(elem) == 3:
            
            dtype = elem[0]
            if dtype == 'DATA':
                
                dname = elem[1]     
                desc  = elem[2]

                if dname in self.build_block_data:
                    self.build_block_data[dname].append(desc)
                else:
                    self.build_block_data[dname] = [desc]     
                
            elif dtype == 'SOFTWARE':
            
                dname = elem[1]     
                desc  = elem[2]

                if dname in self.build_block_soft:
                    self.build_block_soft[dname].append(desc)
                else:
                    self.build_block_soft[dname] = [desc]     

            elif dtype == 'SERVICES':
                
                dname = elem[1]     
                desc  = elem[2]

                if dname in self.build_block_soft:
                    self.build_block_serv[dname].append(desc)
                else:
                    self.build_block_serv[dname] = [desc]     

                
            else:
                print '[Warning task.py] add_other_build_bolck: no such type: ', dtype, ' only [DATA | SOFTWARE | SERVICES] supported!'
            
            
        else:
            
            print '[Warning task.py] add_other_build_bolck: elem == ', len(elem), ' should == 3'
        



    def __str__(self):
        print 'task number: ', self.task_number, '\n'
        print 'task name  : ', self.name, '\n'
        print 'Short description of this component : ', self.short_desc_comp, '\n'
        print 'Short description of potential use case  : ', self.short_desc_usecase
        print '\n\n'
        print 'To which building block your component belongs to ?        : ', self.build_block_belong, '\n'
        print 'Which other building blocks does your component need ?     : \n'
        print '      DATA:'
        for key in self.build_block_data:
            print '             ', self.build_block_data[key]
        print '      SOFTWARE:'
        for key in self.build_block_soft:
            print '             ', self.build_block_soft[key]
        
        print '\n\n'
        for key in self.planned_functionality:
            print key, ': ', self.planned_functionality[key]
        
        return '' 
        
        
        
        