# -*- coding: utf-8 -*-
"""
Created on Wed May  3 19:34:54 2023

"""

import os, time, datetime
import shutil
downloadpath='/Users/*******/Downloads'  # replace with your path to downloads

os.chdir(downloadpath)

#print(os.listdir())
for file in os.listdir():
    stats=os.stat(file)
    time.ctime(stats.st_mtime)
    date_of_created = datetime.datetime.strptime(  time.ctime(stats.st_mtime), "%a %b %d %H:%M:%S %Y") # Convert string to date format
    #print("Date year: {} , month: {} , day: {}".format(str(date_of_created.year),str(date_of_created.month),str(date_of_created.day)))
    
    date_made=""+ str(date_of_created.year)+"_"
    if len(str(date_of_created.month))==1:
        date_made=date_made+"0"+str(date_of_created.month)+"_"
    else:
        date_made=date_made+str(date_of_created.month)+"_"
        
    if len(str(date_of_created.day))==1:
         date_made=date_made+"0"+str(date_of_created.day)
    else:
         date_made=date_made+str(date_of_created.day)
    
    
    if not os.path.exists(date_made):
        os.makedirs(date_made)
    
    shutil.move(downloadpath+"/"+str(file), downloadpath+"/"+date_made)
    
    