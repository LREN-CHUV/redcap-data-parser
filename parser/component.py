#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:12:48 2016

@author: guillaume
"""


from tree import Tree



class Component:
    """
        
        A red cap component
    
    
    """
    
    def __init__(self):
        
        self.survey_timestamp = 'None'
        self.task_leader      = 'None'
        self.subject_ID       = 'None'
        self.tasks            = []

        self.stasks           = dict()
        self.tree             = Tree()

    
    
    def sort(self):
        """
            Tasks are categorises according to task.build_block_belong
             which have three elements, for instance:
                
                 ['SOFTWARE','Data Factory (DF)','Feature Engineering']                 
                 

        """        
       
        for i in range(0,len(self.tasks)):
            if len(self.tasks[i].build_block_belong) == 3:
                self.tree.add_element(self.tasks[i].build_block_belong,i)           
                
                
                
    def __str__(self):
     """
        print statistics of the components         

     """               
     
     print 'Task leader:     ', self.task_leader
     print 'Subject_ID:      ', self.subject_ID
     print 'Number of tasks: ', len(self.tasks)
     for task in self.tasks:
         print ' ', task.name         
         print ' ', task.task_number         
         
     
     return ''
     
     