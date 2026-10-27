# import test_module

# name=input("what is your name: ")
# test_module.show(name)

# # accessing particular variable
# import test_module
# age=test_module.person["Age"]
# print(age)

# # accessing particular function
# # from test_module import add
# from test_module import *
# first=int(input("enter first number"))
# second=int(input("enter second number"))

# add(first,second)
# sub(first,second)
# mul(first,second)
# div(first,second)


# renaming the module file
# import test_module as test
# print(test.person["name"])

# palindrome or not
from test_module import palindrome
num=int(input("enter your number: "))
palindrome(num)

# Armstrong or not 
from test_module import armstrong
num=int(input("enter your number: "))
armstrong(num)

