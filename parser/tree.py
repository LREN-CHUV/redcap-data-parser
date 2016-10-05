#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:09:26 2016

@author: guillaume
"""

class Node:
    
    def __init__(self,name):

        self.child_nodes = []
        self.name        = name
        self.idx         = []
        self.path        = []
        
        
        

class Tree:

    def __init__(self):        

        self.root = Node('root')

    def add_element(self,elements,idx):
        """
        Example
        -------
        
            element: ['SOFTWARE','Data Factory (DF)','Feature Engineering']
            idx: integer
        """
        
        if len(elements) != 3:
            return
            
        # add element 1    
            
        name1 = elements[0]    
        node1 = self.search_child(name1,self.root)
        
        if node1.name == 'empty':
            self.root.child_nodes.append( Node(name1) )
            c_node = self.root.child_nodes[-1]
        else:
            c_node = node1 
            
        # add element 2
            
        name2 = elements[1]    
        node2 = self.search_child(name2,c_node)
        
        if node2.name == 'empty':
            c_node.child_nodes.append( Node(name2) )
            c2_node = c_node.child_nodes[-1]
        else:
            c2_node = node2       
            
     
        # add element 3    
      
        name3 = elements[2]    
        node3 = self.search_child(name3,c2_node)
        
        if node3.name == 'empty':
            c2_node.child_nodes.append( Node(name3) )
            c3_node = c2_node.child_nodes[-1]
            c3_node.idx.append(idx)   
            c3_node.path = elements
        else:
            c3_node = node3                          
            c3_node.idx.append(idx)   
     
            
    def get_leaf_nodes(self):

        leaf_nodes = []
        for child1 in self.root.child_nodes:
               for child2 in child1.child_nodes:
                   for leaf in child2.child_nodes:
                       leaf_nodes.append(leaf)
                       
        return leaf_nodes               

                
        
    def search_child(self,name,node):
         
         num_child = len(node.child_nodes)
        
         for i in range(0,num_child):
             if name == node.child_nodes[i].name:
                 return node.child_nodes[i]
             
         return Node('empty')   
         
                
    
    def depth_first_search(self,name,node):
         """
             Searches for a node with [name] via depth-first-search
         
         """
         
         for child_node in node.child_nodes:
             if child_node.name == 'name':
                 return child_node
             else:
                 return self.depth_first_search(name,child_node)
                 
                 
         return Node('empty')    
             
         
    def print_tree(self):
        
        for child1 in self.root.child_nodes:
            print child1.name, '\n'
            
            for child2 in child1.child_nodes:
                print '  ',  child2.name, '\n'
                
                for leaf in child2.child_nodes:
                    print '    ',  leaf.name, '\t', leaf.idx

            
            
         
         
         
         
         
         
                    