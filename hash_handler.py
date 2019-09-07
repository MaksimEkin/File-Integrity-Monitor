#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 20:58:57 2019
hash_handler.py

Handle hash operations

@author: maksimekineren
"""

# LIBRARIES NEEDED
import hashlib
import file_handler


#==============================================================================
# Take SHA256 of each file
# hash is taken in blocks, this is done to ensure large files doens't fail
#==============================================================================
def hash_file_sha256(directory, LOG_FILE):
    
    try:
        # use hash libraries sha 256
        sha256_hash = hashlib.sha256()
        
        # take hash
        with open(directory,"rb") as f:
            
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
                
            # return the hash
            return sha256_hash.hexdigest()
        
    except Exception as e:
        file_handler.log(LOG_FILE, \
                         "Error while taking the hash values")



    