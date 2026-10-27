#exception => unwanted or unexpected event that disturbs normal flow of program is called exception.
# for graceful termination of program
# exception handlilng does not mean repairing the exception.=> Alternative way to continue of program
try:
    print(10/0)
except ZeroDivisionError:
    print("value can't divisible by zero")

# multiple except
try:
    a=int(input("enter a="))
    b=int(input("enter b="))
    print(a/b)
except ZeroDivisionError:
    print("can't divide with zero")
except ValueError:  
    print("only int value") 


# error types
try:
    print(10/0)
except ArithmeticError:    
    print("ArithematicError")
except ZeroDivisionError:
    print("ZeroDivisonError")    

# default except block
try:
    print(10/0)
except ArithmeticError:    
    print("ArithematicError")
except:
    print("ZeroDivisonError") 


#  exception class list
try:
    print(10/0)
except (ArithmeticError,ValueError,Exception):    
    print("ArithematicError")
except:
    print("run") 

# #  exception class list
try:
    print(10/0)
except (ArithmeticError,ValueError,Exception):    
    print("ArithematicError")
except:
    print("run") 
finally:
    print("finally block excuted")        



# user-defined Exception
class TooyoungException(Exception):
    def __init__ (self,args):
        self.msg=args

class TooOldException(Exception):
    def __init__ (self,args):
        self.msg=args

age=int(input("enter your age"))
if age>60:
    raise TooOldException("you are too younger to marry")
elif age<18:
    raise TooyoungException("you will get your best soulmate soon")
else:
    print("you can marry")



# practice 

# zeroDivisionError
try:
    a=10
    b=0
    print(10/0)
except ZeroDivisionError as zde:
       print("Exception:", type(zde).__name__)
       print("Message:", zde)

# valueError
try:
    x=int("hello") 
    print(x)
except ValueError as ve:
       print("Exception:", type(ve).__name__)
       print("Message:", ve)     

# TypeError
try:
    x="10"+5 
    print(x)
except TypeError as te:
       print("Exception:", type(te).__name__)
       print("Message:", te) 

# NameError
try:
    print(name) 
except NameError as ne:
       print("Exception:", type(ne).__name__)
       print("Message:", ne)  

#IndexError
try:
    numbers=[10,20,30]
    print(numbers[5])
except IndexError as ie:
       print("Exception:", type(ie).__name__)
       print("Message:", ie)  

#keyError
try:
    student={"name":"rohit","age":23}
    print(student["marks"])
except KeyError as ke:
       print("Exception:", type(ke).__name__)
       print("Message:", ke)   

# FilenotfoundError
try:
    f=open("data.txt","r")
    print(f.read())
    f.close() 
except FileNotFoundError as fnfe:
       print("Exception:", type(fnfe).__name__)
       print("Message:", fnfe)                        

# Attribute Error
try:
     number=10
     number.append(20)
except AttributeError as ae:
        print("Exception:", type(ae).__name__)
        print("Message:", ae)  

#ImportError
try:
     from math import xyz
except ImportError as ie:
        print("Exception:", type(ie).__name__)
        print("Message:", ie)      

#overflowError
try:
     import math
     print(math.exp(10000))  
except OverflowError as oe:
        print("Exception:", type(oe).__name__)
        print("Message:", oe)                     




# Automatically detect exception
try:
    print(10 / 0)

except Exception as e:
    print("Exception:", type(e).__name__)
    print("Message:", e)  




