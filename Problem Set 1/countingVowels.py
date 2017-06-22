# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 16:35:02 2017
@author: Nishant Srivastava
"""
#Test string for s
s = 'abcdef'

vowelCount = 0
for i in s:
    if i in 'aeiou':
        vowelCount += 1

print('Number of vowels is: ', vowelCount)