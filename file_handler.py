#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 20:46:33 2019
file_handler.py

Handle file operations

@author: maksimekineren
"""

# LIBRARIES NEEDED
import os
import pickle 
import datetime


#==============================================================================
# Recursively walks the directory tree
# Finds directories and files
# Also finds hidden files (starts with '.')
#==============================================================================
def search_directory_tree(root_dir, IGNORE_LIST, LOG_FILE):
    
    try:
        # hold directories and files
        directories = dict()
        
        # recursively walk to directory tree and get files
        for dirName, subdirList, fileList in os.walk(root_dir):
            
            # remove ignore list from list
            if (IGNORE_LIST):
                for ignore in IGNORE_LIST:
                    
                    # if ignore in the list
                    if (ignore in fileList):
                        fileList.remove(ignore)
                        
            directories[str(dirName)] = fileList
        
        return directories
            
    except Exception as e:
        log(LOG_FILE, \
            "Error while scanning directories and files")
        


#==============================================================================
# Save dictionary of hashes
#==============================================================================
def save_dict(dictionary, file, LOG_FILE):
    
    try:
        # open the file to use to save the dictionary
        initial_scan_file = open(file, "wb")
        
        # use pickle to save the dictionary
        pickle.dump(dictionary, initial_scan_file)
        
        # close the file
        initial_scan_file.close
        
    except Exception as e:
        log(LOG_FILE, \
            "Error while saving the dictionary")



#==============================================================================
# Load dictionary of hashes
#==============================================================================
def load_dict(file, LOG_FILE):
    
    try:
        # open the pickle file to load
        infile = open(file, 'rb')
        
        # use pickle to load the dictionary
        loaded_dict = pickle.load(infile)
        
        # close the file
        infile.close()

        return loaded_dict
        
    except Exception as e:
        log(LOG_FILE, \
            "Error while loading the dictionary")
    
    

#==============================================================================
# Log events
#==============================================================================
def log(log_dir, message):
    
    # get time
    currentDT = datetime.datetime.now()
    
    # log event
    file = open(log_dir, "a+")
    file.write(str(message) + \
               " --- Time: " + \
               str(currentDT.strftime("%Y-%m-%d %H:%M:%S")) + \
               "\n")
    file.close