# Print a greeting message twice
print("Hello World!")
print("Hello World!")

# Variable assignments
x = 1
y = 1

# Variable naming conventions
# _name = 1  # Valid: Variable names start with a letter or underscore
# Avoid overwriting built-in variables like __name__
__name__ = 1  # Warning: __name__ is a built-in, avoid reassigning
# In Python, variables are dynamic and unprotected (e.g., print = 10 is risky)

# Print the value of x
print(x)  # Outputs: 1

# Print memory addresses of x and y
print(id(x), id(y))  # id() shows memory address; x and y share the same address for 1

# Conditional statement
if x > 0:
    print("yes")
    print("yes")

''' .string    for documenation '''
#Floating-point arithmetic
#Integers in Python have no size limit, ideal for data analysis
#Floats represent decimal numbers but may have precision issues

print(0.5 - 0.4)  # Outputs: 0.1
'''
print("boolean")
1 = True
2 = False
print(1 == True)
print(0 == False)
print(1 != False)
print(0 != True)'''


# string

name= 'mary'
age = 6
print ('hi ' + name + '. you are ' + str(age) + ' years old.' )
print (f'hi { name }. you are {age} years old.')

txt = '50a00'
x = txt.isdigit()
print(x) #true



# Data type 

print (str(1))
print (int ('1'))
print (int (float('1.1')))
print (float('1')) #1.0
print (float (1), float('1.1'), float(True), float(False)) #1.0 1.1 1.0 0.0
print (bool(1), bool(2.1), bool('a'), bool(''))  #ture = 1, false =  0 empty
print (bool(None), bool(0), bool(-1))


#list
name = ['John', 'peter', 'ann', 'dave']
print (id(name), type(name))
print (name[0])
name2 = ["john", [1,2,3,4]]
print (name2 [1][1]) # find list of list
name2 [1][0] = 20
print (name2)
name3 = ['john', ['john', ['a','b','c'], [[1,2,3]], None], [1, [True, ['john','a', [6,7,8]]],3,4], None] # fine 2
print(name3 [1][0][2]) # h - string is also a list
print(name3 [1][2][0][1]) #2

#tuple
# can not change tuple value
# list and tuple different, list can change the value
t= 1,2,3 # tuple no need ( )
print (t)

t2 = 1,
print (t2)

a,b = 1,2
print(a,b) # 1 2


c,d = [1,2,3], [4,5,6]
print(c,d) #[1,2,3] [4,5,6]
print (d) #[4,5,6]

a,b = 1,2
a,b = a+b, a*b #3 2
a,b = [a,b], [b,a] #[3,2] [2,3]
#a,b = a #3 2
print(a) # 3
a, a = a #it was a,a = 3,2  overwrite a to 2 
print (a) #2
print (a, b) #2, [2,3]


#set  - random, cut of the same numnber, only number in order, give out unique value, filter out
s = {1,2,3,4,5,6,7,1,2,1,2,1,2,3,3,4,4,4,5,6,6,7,7}
print(s) #{1, 2, 3, 4, 5, 6, 7}
s2 =  {1,2,3,'a',4,5,6,7,1,2,1,'b',2,1,2,3,3,4,4,4,'c',5,6,6,7,7}
print(s2) #{1, 2, 3, 4, 5, 6, 7, 'c', 'a', 'b'}

# put the list to set, filter out 
s2 =  [1,2,3,'a',4,5,6,7,1,2,1,'b',2,1,2,3,3,4,4,4,'c',5,6,6,7,7]

#print(set(s2)) # data type is set
print(list(set(s2))) #data type is list


print('----- Object -------------')
# python list = [array] , think of link list, the list holding the address


#Dictionary 
''' car = { "color" : "red"  < ---- dictionary --- lookup the label, find the label then find the value
            "wheel" : 4      <- all the datatype ok  on the lefe side, except list
            "speed" : 200}   <-- all the dataype ok on the right side
                '''

color = 'color'
wheel = 'wheel'
speed = 'speed'

car = { 
    color : "red", # left side color  ---> key       right side "red" -----> value
    wheel : 4,     
    speed : 200,
    (1,0) : 2}  ##tuple must have ( )

print(car) #{'color': 'red', 'wheel': 4, 'speed': 200}

car[color] = 'blue'
print(car) # {'color': 'blue', 'wheel': 4, 'speed': 200}
car['door'] = 5 # add item on the list
print(car)
del car [(1,0)] # delete item from the list
print (car)


print('-------')

def a(): 
    x = 1
    y = 2
    z = 3
    print (x, y, z)
    return 6
 
a() # 1 2 3 

print(a()) # 1 2 3        6

print('-------')
#funtion is a expression

def c (x,y,z):
    result = x + y + z
    print (result)
    return (result)    #must have return, can not none + none

print (c,c(1,2,3)+ c(4,5,6)) #1 2 3       4 5 6      <function b at 0x100f377e0> 21 <- 6 + 15

c(1,2,4) 

print('------------------')

def b(c):
    return c

def a(x,y,z =3 +b(1)):
    result = x + y + z
    print ( x, y, z)
    return result 

print (a(1,2))  # 1 2 4       7

print('---------------------')

def a(c): #註冊 A 先
    print ('I am for funtion a')
    return c()
def b(): #註冊 b 先
    print ('I am for funtion b')
    return a

a(b)



print('-------------------------')
def a(): #註冊 A 先
    print ('I am for funtion a')
    return b
def b():
    print ('I am for funtion b')
    return a

a()()()()

print('--------------------------')

def a():
    print ('I am for funtion a')

car = {
        'color' : 'red',
        'run' : a
    }
car['run']()  #I am for funtion a

print('--------------------------')

def a():
    print ('I am for funtion a')

car = {
        'color' : 'red',
        'build' : a() #build 裝埋funtion a's result,
    }
print(car['build'])  #I am for funtion a , none

print("----------- 12 June -----------------")
x = 10
if x <= 9:
    print("x is less than and equal to 9")
elif x> 9 and x == 10:
    print("x is equal to 10")
else :print ("x is larger than 10")

print("----------- truthy value -----------------")
x = 1 and 0 and True and [1] and {1} and {"1" :1} and 1.1 and (1,)
print (x)


print("----------- default value -----------------")
default = "TST"
city = ''
city = city or print ("please inout city") or default
print (city)


print("----------- while loop -----------------")
x = 10
while (x):
    x= x -1 # <---- controller
    if x  == 7:
        continue
    print(x)
    if x == 4:
        break 
else:
    print ("exit when while is false")


print("-----------for loop-----------------")
for i in range(3):       #(0,3,1)
    print(i) #range(start, end - 1, step)

print("-----------range (start : end - 1: step)----------------")
for i in range(1,5,2): 
    print(i) #range(start, end - 1, step)

print("----------- Range 2-----------------")
for i in [1,2,3,4]:
    print(i)



print("----------- while loop , break-----------------")
def a (x):
    return x
b = 1
while (a(b)):
    print(b)
    b = b + 1
    if b == 10:     #if
        break       #break


print("----------- slice ----------------")
l = [1,2,3,4,5,6,7,8,9,10,11,12]
x = l[0:4:1]
start,end,step = 0,9,3
s = slice (start,end,step)
x = l[s]
print (x)


print("----------- backward----------------")
#      0,   1,   2,  3,  4,  5,  6,  7,  8,  9, 10, 11
l = [  1,   2,   3,  4,  5,  6,  7,  8,  9, 10, 11, 12]
#    -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1
x = l[-4 : -9 : -1]
print(x)

print("----------- del list item----------------")
l = [  1,   2,   3,  4,  5,  6,  7,  8,  9, 10, 11, 12]
del l[3:6]
print (l)


print("----------- 18 June : try , except---------------")
try:
    x = 1
    y = "0"
    z = x/y
    print(z)
except ZeroDivisionError:
    print(" Division error, please fix Y value")
except TypeError:
    print("please check data type, values must be number type")
else:
    print("no error")
finally:   #file closed
    print("this line will run, not matter what")


print("-----------range (start : end - 1: step)----------------")


print("#1")
lst = [0,1,2,3,4,5]
print (lst[1:4]) #1,2,3
print("#2")
lst = [0,1,2,3,4,5]
print (lst[:3]) #0,1,2
print("#3")
lst = ["a","b","c","d"]
print (lst[2:]) #c,d
print("#4")
lst = [10,20,30,40,50]
print (lst[:-2]) #3號位停  10,20,30
print("#5")
lst = ["apple", "banana", "cherry", "date"]
print(lst[-2:]) #cherry, date
print("#6")
lst = [0,1,2,3,4,5]
print(lst [::2]) #0,2,4
print("#7")
lst = ["p","y","t","h","o","n"]
print(lst [::-1]) #n, o, h, t, y, p
print("#8")
lst = [0,1,2,3,4,5]
print (lst[4:1:-1]) #4,3,2
print("#9")
lst = [0,1,2,3,4,5]
print (lst[-2:-5:-1]) #4,3,2
print("#10")
lst = [10,20,30,40]
print (lst[::-2]) #40,20
print("#11")
lst = [0,1,2]
print (lst[5:]) #[]
print("#12")
lst = ["a","b","c","d"]
print (lst[3:1]) #[]
print("#13")
lst = [0,1,2,3,4,5]
print (lst[3:0:-1]) #3,2,1
print("#14")
s = "hello"
print (s[::-1]) # olleh
print("#15")
lst = [0,1,2,3,4,5,6]
print (lst[::3]) #0,3,6
print("#16")
lst = [0,1,2,3,4,]
print (lst[-3:4]) #2,3

print("1. create a list of numbers from 0 to 9 using 'rang()'")
print(list(range(10)))



print("2. create a list of  even numbers from 2 to 20 using rang()")
print(list(range(2,21,2)))

print("3. create a list of numbers from 10 to 1 in descending order using rang()")
print(list(range(10,0,-1)))

print("4. create a list of odd numbers from 1 to 20 using rang()")
print(list(range(1,21,2)))

print("5. create a list of multiples of 5 from 5 to 50 using rang()")
print(list(range(5,51,5)))

print("6. create a list of numbers from -10 to 0 in descending order using rang()")
print(list(range(-10,0,1)))

print("7. create a list of numbers from 0 -100 that are divisible 10 using rang()")
print(list(range(0,101,10)))

print("8. creat a list of number from 1 to 10, but skip 5 using 'range()' and list comprehension.")
print([i for i in range(1, 11) if x != 5])
ll = []
def temp():
    for i in range(1,11):
        if i !=5: 
         ll.append(i)


print("9. creat a list of square of numbers from 1 to 10")
print([i**2 for i in range(1,11)])

print("10. creat a list of numbers from 100 to 10 in step of -10 using range")
print(list(range(100,9,-10)))

print("11. create 'range() to generate a list of first 10 positive integer")
print(list(range(1,11)))

print("12. generate a list of the first 10 multiples of 3 using 'range()")
print(list(range(3,31,3)))

print("13. creat a list of numbers from 50 to 60 using range")
print(list(range(50,61,1)))

print("14. generate a list of negative even number from -1 to -20 using 'range()")
print (list(range(-2,-21,-2 )))

print("15. use range() to creat3e a list of number from 0 to 100, stepping by 25")
print (list(range(0,101,25 )))

print("16. create a list of numbers from 5 to 15 using range()")
print(list(range(5,16)))

print("17. generate a list of number from 1 to 10, but only include multiples of 2 or 3 using 'range()' and list comprehension.")
print ([ i for i in range(0,10) if i%2 ==0 or i%3==0])

print("18. generate a list of number from 10 to 100, that are divisible by 10 using range.")
print(list(range(10,101,10)))

print("19. generate a list of number from 1 to 100, that are divisible by 5 but not by 3 using range().")
print([ i for i in range(1,101) if i%5 ==0 and i%3 !=0])

print("20. use range() to generate a list of the first 10 perfect squares")
print([i**2 for i in range(1,11)])


print("-------truthy value---------")
if 0:
    print("truth")
elif 1:
    print("second true")
else: 
    print("false")

print("-------fuction---------")
def a():
    print ("hello")

#nothing happen because we didnt call the fuction

a() # hello, after call fuction, it print hello

print("-------fuction 2---------")
def a(x):
    x = 1 # fuction has an arguments, call fuction must have arguments
    print("hello")
a(x)

print("-------fuction 3---------")
def a(x=1): # another way to put the arguments
    print("hello")
a(x)

print("-------fuction 3---------")
def a(x=1): # another way to input arguments
    x=2
    print("hello")
a(x)


print("-------if--------")
if 10 + 1 ==11:
    print("hello")
else:
    print("false")


print("-------if not--------")
if not 1 == 11: # == go first, 11= 1 -> flase -> "not" flase -> truth -> print hello  
    print("hello")
else:
    print("flase")


print("------true or flase-------")
y = 6
x =(y != 10) # y not = 10 -> true
print(x) #true

print(list(range(1, 11, 2)))
