#imported from Spyder IDE
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 16:23:15 2017
@author: Nishant Srivastava
"""
#Test string for s, commented out
#s = 'bobobobb'

bobCount = 0
subString = "bob"

for i in range(len(s)):
    if s[i:].startswith(subString):
        bobCount += 1

print("The number of times 'bob' occurs is: " + str(bobCount))
