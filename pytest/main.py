
def a():
  print("I am from main.py function a")

def b():
  print("I am from main.py function b")

# a()
# b()

  #import test
  #a()
  #b()


#case 1: simple imoirt module
  #test.b()
  #test.a()
  #print(test.x)
  #print(test._y)

#case 1.1: simple imported module
#imoirt test as T
#t.a()
#t.b()
#print(t.x)
#print(t.__y)


#case 2
#from test import a,b,x,_y
#a()
#b()
#print(x, _y)

#from test import a as ta, b as tb, x as tx, _y as t_y

#def a():
#    print("I am from main.py function a")

#def b():
#    print("I am from main.py function b")

#a()
#b()
#ta()
#tb()
#print(tx, t_y)

#case 3: imoirt nideyke frim sy-folder wuhout _init_
# from util.test1 import *
# a()
# b()
# print(x)


#case 4: load module based on sub-folder name
# from util import a, b, x, COLOR

# a()
# b()
# print(COLOR, x)

#case 4.1 
from util import *
a()
b()
print(COLOR)

#========================
#input
name = input('please input your name:')
print (name)
age = input("please input your age:")
age = float(age) *365.25
print(age)