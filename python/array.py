# array in python

from array import *
a= array("i",[2,4,5])
del a[2]  # delete particular element 
print(a)
print(a[2])

import array as arr
b=arr.array("i",[2,3,4,5,6,7])
del b[4]
b[2:5]=arr.array("i",[1,2,3])   # slicing => change multiple elements
print(b)


import array as arr
a=("i",[2,3,4])
b=("i",[5,6,7])
c=("i")
c=a+b
print(c)





