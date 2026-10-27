# import numpy
import numpy
arr=numpy.array([1,2,3,4,5])
print(arr)

# import numpy with alias name
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

# zero-D Array (scalar)
import numpy as np
arr=np.array(42)
print(arr)

# 1-D Array (vector)
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

# 2-D Array (matrix)
import numpy as np
arr=np.array([[2,3],[4,5]])
print(arr)

# multidimensional Array (tensor)
import numpy as np
arr=np.array([[[2,3],[4,4]],
              [[6,3],[7,5]]])
print(arr)


# array functions
import numpy as np
arr=np.array([1.1,2.4,3.0,4.3,5])
print(arr.dtype)  # print datatype of array

# comparision of array
import numpy as np
x=np.array([3,5])
y=np.array([2,5])

print("comparision-greater")
print(np.greater(x,y))

print("comparision-less")
print(np.less(x,y))

print("comparision-greater_equal")
print(np.greater_equal(x,y))

print("comparision-less_equal")
print(np.less_equal(x,y))

# reshaping the arrray
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# two_d=arr.reshape(4,3)   # 4 rows and 3 columns
# two_d=arr.reshape(2,2,3)   # 2 dimensition , 4 rows and 3 columns

# for i in np.nditer(two_d):   # numpy.nditer() is used to iterate through the elements of a NumPy array, including multidimensional arrays.
#     print(i)

# n=np.where(arr==4) # search element 
# print(n)

# n=np.where(arr%2==0) # even element's index number 
# print(n)

print(np.sort(arr))   # sort array
print(np.sort(arr) [::-1])   # reverse sort array








