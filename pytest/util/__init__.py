# when main is loading util package _init_.py will run
#case 3
print("__init__ is a trigger")

COLOR = 'red'  

#case 4
from .test1 import a, b, x
__all__ = ['a','COLOR'] #only give out a and COLOR
