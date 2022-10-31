# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 13:32:48 2022

@author: dm22aah
"""
import clean_up as clp
import pandas as pd

'''
f = open("big_data.txt", "r")
data = f.read()
print(data)

word_count = data.split()
print('\n Word count : ', len(word_count))

print('\n Letter count: ', len(data))

'''

with open('big_data.txt', 'r') as text:
    all_words = []
    counter = 0 
    ltr = 0
    for line in text:
        words = line.split()
        counter += 1
        for word in words:
            word = clp.clean(word)
            ltr = ltr + len(word)
            all_words.append(word)
            
            
print('Word Count : ' , len(all_words))
print('Letter Count : ', ltr)

