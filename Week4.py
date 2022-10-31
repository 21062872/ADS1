# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 13:32:48 2022

@author: dm22aah
"""
import clean_up as clp
import pandas as pd

f = open("big_data.txt", "r")
data = f.read()
print(data)

word_count = data.split()
print('\n Word count : ', len(word_count))

print('\n Letter count: ', len(data))