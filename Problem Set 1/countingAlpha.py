# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 08:21:39 2017

@author: Nishant Srivastava
"""
#Test string
s = 'abcdbeggh'

maxLength = 0
running = s[0]
longest = s[0]

for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        running += s[i + 1]
        if len(running) > maxLength:
            maxLength = len(running)
            longest = running
    else:
        running = s[i + 1]

print ('Longest substring in alphabetical order is: ' + longest)