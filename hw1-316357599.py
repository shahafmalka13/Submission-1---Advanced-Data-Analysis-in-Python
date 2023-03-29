# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:10:10 2023

@author: lenovo
"""

## Q num 1
def my_func(x1,x2,x3):
    if type(x1)==int or type(x2)==int or type(x3)==int:
        print('Error: parameters should be float')
    elif type(x1) != float or type(x2) != float or type(x3) != float:
        print('none')
    elif x1+x2+x3 == 0:
            print('Not a number – denominator equals zero')
    else:
        equal=((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
        float(equal)
        print(equal)
my_func(-1.0, 1.0, 0.0)


## Q num 2

def revword(string):
    string = string.lower()[::-1]
    return string
    
def countword(file_name):
    our_file = open(file_name)
    counter = 1
    
    for line in our_file:
        words = line.split(' ')
        if len(words)==1:
            word = words[0].lower().strip()
        else:
            for reword in words:
                reword = revword(reword).strip()
                if reword == word:
                    counter +=1
    print(counter)
        
    
    
    
countword('text.txt')
     