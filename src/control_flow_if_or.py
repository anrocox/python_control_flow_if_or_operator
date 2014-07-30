#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 22, 2014

@author: anroco

How to use the or operator in an if statement of Python?

¿Cómo usar el operador or en una sentencia if de Python?
'''

#if expression1 or expression2 or expressionN:
#    statements

#create two boolean objects
a = False
b = False

#the validation is False only if all the expressions generate a value False
if a or b:
    print('a is True or b is True or both are True')
else:
    print('a and b are False')
