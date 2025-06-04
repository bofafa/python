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
