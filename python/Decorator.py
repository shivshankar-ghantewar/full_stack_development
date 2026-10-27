# we can extend the functionality without modifies that function.

def decor(func):
    def inner(name):
        if name=="sunny":
            print("hello sunny bad morning")
        else:
            func(name)
    return inner        



@decor
def wish(name):
    print("hello",name,"good mornig")

wish("sunny")    
wish("Bunny")    
wish("funny")    



# example 2
def decor(func):
    def inner(name):
     if name=="sunny":
        print("hello sunny bad morning")
     else:
        func(name)
    return inner   

def wish(name):
    print("hello",name,"good morning")

decorfunction=decor(wish)  

wish("durga") # decorator wont be excuted
wish("sunny") # decorator wont be excuted
decorfunction("durga") # decorator will be excuted
decorfunction("sunny") # decorator will  be excuted


#Decorator Example 

#basic Decorator Example
def my_decorator(func):
    def wrapper():
        print("before function call")
        func()
        print("after function call")
    return wrapper

@my_decorator
def greet():
    print("Hello, python!")

greet()        


# Decorator with Argument
def log_function(func):
    def wrapper(*args,**kwargs):
        print("function is being called")
        result=func(*args,**kwargs)
        print("function finished")
        return result
    return wrapper

@log_function
def add(a,b):
    return a+b
print("sum",add(3,5))

# decorator with return value
def mul_function(func):
    def wrapper(x):
        result =func(x)
        return result*result
    return wrapper

@mul_function
def simple(x):
    return x+2
print(simple(3))


# Decorator with Argument (to Decorator)
def repeat(num):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(num):
                func (*args,**kwargs)
        return wrapper
    return decorator
      
@repeat(3)
def say_hello():
    print("hello")

say_hello()    


# multiple decorator
def decorator1(func):
    def wrapper():
        print("decorator 1")
        func()
        print("end decorator 1")
    return wrapper   

def decorator2(func):
    def wrapper():
        print("decorator 2")
        func()
        print("end decorator 2")
    return wrapper 

@decorator1
@decorator2
def show():
    print("hello")

show()    
