#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:12:48 2016

@author: guillaume
"""



class Component:
    """
        
        A red cap component
    
    
    """
    
    def __init__(self):
        
        self.title = ''
        self.feature = ''
        self.component = ''
        self.contribution = ''
        self.short_desc = ''
        
        self.data_hosp = []
        self.data_ref = []
        
        self.soft = []
        
        self.release = []
        
        self.use_case = []
        
        
    def add_data(self,dtype,desc):
       """
          Adds a redcap DATA component.
              
       Parameters
       ----------
       
           dtype : string, ('hospital' or 'reference')
           desc  : string, list of people using this data (ex: list of hosptials)
           
       Example
       -------
       
           add_data('hospital','Lille Hospital, Tel Aviv Hospital, Freiburg Hospital')
           
              
       """
       
       if dtype == 'hospital':
           
           self.data_hosp.append(desc)
           
       elif dtype == 'reference':

           self.data_ref.append(desc)
           
       else:
           print 'Error dtype: ' + dtype + ' not supported, only [hospital,reference] currently supported'
           

    def add_soft(self,name,desc):
      """
            Adds a redcap SOFTWARE component
            
       Parameters
       ----------
       
           name : string, software name
           desc  : string, list of people using this data (ex: list of hosptials)
           
       Example
       -------
       
           add_soft('Data Factory (DF)','Data Anonymisation, Workflow Engine, Data Pipeline processes, Data Quality Processes, Data Storage')
        
      """
      
      self.soft.append([name,desc])
    
      
    def add_release(self,name,desc)  :
      """
            Adds a redcap RELEASE component
            
       Parameters
       ----------
       
           name : string, release name
           desc  : string, description
           
       Example
       -------
       
           add_release('Planned functionality at M12','Initial implementation of image factorisation method without distributed computing (MS126).')
        
      """        
      
      self.release.append([name,desc])
      
      

    def add_usecase(self,users,desc):
      """
            Adds a redcap USE CASE component
            
       Parameters
       ----------
       
           uses : list,   list of users
           desc : string, description
           
       Example
       -------
       
           add_usecase('Planned functionality at M12','Initial implementation of image factorisation method without distributed computing (MS126).')
        
      """     
      
      self.use_case.append([users,desc])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
        
        
        
        
        