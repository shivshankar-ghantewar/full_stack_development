a=input("enter your digit: ")  #input
print(a) # output

# variable assignment
e="hello"
print(e)

# munltiple variable assignment 
b,c,d=1,2,3
print(b,c,d)

# indentation
age=19
if age>18:
    print("your are eligible")
else:
    print("your not are eligible")

# comments
# single line comment
  
'''
this is
multiple  line 
comment   
'''

# print pass student's name
marks={
    "amit":78,
    "neha":32,
    "raj":45,
    "priya":28,
    "sam":50
}  

for name,mark in marks.items():
    if mark >35:
     print(name)


# escape string 
# "\hi\"    => print double quote in output
txt= "\"string\" is the collection  of characters "
print(txt)

# datatypes in python

# numeric => int ,float,complex
a=5
print(type(a))
b=5.4
print(type(b))
c=5j
print(type(c))

# boolean  => true, false
a,b=5,0
print(type(a>b))
print(a>b)
print(a<b)

# sequential => List,tuple
first=[10,20,30]  # changable
first[0]=50
print(first)

second=(10,20,30)  # unchangable
# second[0]=50 => error because unchangable
print(type(second))


# container => set,dictionary

first={10,20,10}  # duplicate not allowed
print(first)
print(type(first))

second={
   "name":"shiv",
   "age":23
}

print(second["name"])


# operators in python => Arithematic,relational, Assignment,Logical,Bitwise,Membership,identity

# Arithematic operator
a,b=5,3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)  # floor =>result ko neeche wale nearest integer ki taraf round karne ke liye
print(a%b)
print(a**b)  # power

# relational operator
a,b=5,5
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)
print(a!=b)

# Logical operator
a,b=5,5
print(a>b and a==b)
print(a>b or a==b)
print(not a==b)

# bitwise operator => and,or,xor,complement,right shift, left shift

# Assignment operator
a,b=5,2  # assign
a+=3
print(a)
a-=3
print(a)
a*=3
print(a)
a/=3
print(a)
a%=3
print(a)
a**=3
print(a)
a//=3
print(a)

# membership operator 

seq =[1,2,3,4,5,6]

for i in seq:
   print(i)

print(10 not in seq)

# indentity operator
a=10
print(type(a) is int)
print(type(a) is not int)

# control flow  
# conditional statement => if, if-else, if-else ladder, Nested if



#loop statement => for loop, while loop

list1 = [1, "hi", "Python", 2]
print(type(list1))
print (list1)
# List slicing
print (list1[2:])
# List slicing
print (list1[0:2])

  
# list methods
fruits=["apple","banana","guava"]

fruits.sort()  #The sort() method sorts the list ascending by default
print(fruits)

fruits.reverse()   # Reverses the order of the list
print(fruits)


fruits.pop(1)  #Removes the element at the specified position
print(fruits)

fruits.insert(1,"orange")  # Adds an element at the specified position
print(fruits)

x=fruits.index("banana")  #Returns the index of the first element with the specified value
print(x)

fruits.append("mango")  # add element at last

x=fruits.copy()  # copy whole list
print(x)

count=fruits.count("banana")  # Returns the number of elements with the specified value
print(count)

print(fruits)


fruits.clear()  # Removes all the elements from the list

# map()
def mycube(x):
 return x*x*x
list1 = [1,2,3,4,5]
newlist1 = list(map(mycube,list1))  #  each item in an iterable
print(newlist1)


# tuple 

tuple1=(1,2,4,3,5,7,8,6,9)

print(tuple(sorted(tuple1)))  # sort array
print(tuple(reversed(tuple1))) # reverse the tuple
print(tuple1.index(5))  # index of the first ocurrence of the element.
print(tuple1.count(2))  # Gives the count of element repeated in the tuple as an output
print(sum(tuple1))  # Gives the sum of element in the tuple as an output
print(max(tuple1))  # Gives the largest element in the tuple as an output.
print(min(tuple1)) # Gives the smallest element in the tuple as an output
print(len(tuple1)) #This function returns the number of elements present in a tuple.


# Dictionary 
d = {1:'Abc', 2:'Lmn', 3:'Pqr', 4:'Xyz'}
# Printing dictionary
print (d)
# Accesing value using keys
print("1st name is "+d[1])
print("2nd name is "+ d[2])
print (d.keys())
print (d.values())

# dictionnay method
my = {"name":'shiv', "Age":23, "city":'Nanded', "course":'python'}

my.setdefault ("city","pune")  # default value

my.update({"place":"nanded"})   # update value

my["place"]="dattawadi"   # insert new element

print(my.popitem())   # remove last item

print(my.items())   # print dict as tuple form

print(sorted(my.keys()))  # sort keys
print(sorted(my.items()))   # sort dictionary

print(my.pop("course"))  # delete particular  item

new_dict=my.copy()  # copy dictionary
print(new_dict)

print(my.get("name")) # Get the value of the item

# set => unique elements
# creating empty set
# set1=set()  

myset={2,"shiv",3,"gaurav"} 
# myset.add(30)  #add element

# myset.remove(3)  #remove element

# myset.pop() # remove random element

# myset.discard("gaurav") # remove item

myset2={1,"arjun",4,"gajanan",2}

# myset.update(myset2)   #  updates the current set, by adding items from another set .

# c=myset.union(myset2)     # union all items

# c=myset.intersection(myset2)    # difference from first set

# b={"gajanan"}
# print(b.issubset(myset2))   # subset  or not

# differnce=myset.symmetric_difference(myset2)   # returns different items from both set
# print(differnce)

# myset.intersection_update(myset2)   # remove unmatched items
# print(myset)



# functions

def student(name):
   print("hello",name)

student("shiv")    # required argument


def student(name,age,city):
   print("name=",name)
   print("age=",age)
   print("city=",city)

student(age=20,city="nanded",name="shiv")   # keyword argument 


def student(name,city,age=20):
   print("name=",name)
   print("age=",age)
   print("city=",city)

student(name="shiv",city="nanded")   # default argument


# variable length argument

# *Args => store in tuple form
def student(name,*marks):
   print("name=",name)
   print("marks=",marks)

student("shiv",23,23,34,34) 

# ** kwargs => store in the form of dictionary
def student(name,**marks):
   print("name=",name)
   print("marks=",marks)

student("shiv",math=23,eng=45,science=78) 

# return statement

def sum(a,b):
   c=a+b 
   return c           # return the c
print(sum(10,20)) 

def sum(a,b):
   c=a+b            # return not present => none
print(sum(10,20))  

# lamba => single line code
sum=lambda x,y: x+y 
print(sum(10,20))

# recursion function
def fact(n):
   if(n==1):
      return 1
   else:
      return n*fact(n-1)

print(fact(4))   


# pass statement => placehlder(empty) for future use
def demo():
   pass

demo()


# string
str1='hello'  # single quote
print(str1)
str2="hello"  # double quote
print(str2)

str3=''' this 
is a multiline
string'''
print(str3)

# positive indexing and slicing => starts from 0
school="Alard"
print(school[3])
print(school[3:5])

# negative indexing and slicing  => starts from -1
school="Alard"
print(school[-3])
print(school[-5:-1])


# Escape character

sting="this is a \"separate\" string"
print(sting)

# string functions

name="gaurav panchal"
print(name.capitalize())
print(name.isupper())
print(name.islower())
print(len(name))
print(name.replace("panchal","patil"))
print(name.index("v"))
print(name.partition("av"))   # separate the word
print(name.split()) # separate the words
print(name.count("a"))

str='*'
new="hello"
print(str.join(new))



















