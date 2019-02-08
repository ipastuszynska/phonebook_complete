# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 14:11:49 2019

@author: iza
"""

from phonebook_database import* 

conn = sqlite3.connect('phonebook.db') 
c = conn.cursor()

create_table_business()
populate_table_business()

create_table_people()  
populate_table_people()  

create_table_coordinates()
populate_table_coordinates_people()

c.close()
conn.close()