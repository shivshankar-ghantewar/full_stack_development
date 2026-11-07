# wrapping up data and methods into a single unit(class) it's called encapsulation.

# encapsulation using private access specifier => Access within same class only
class employee:
    def __init__(self):
        self.__password="ABC123"  # __ for private

e=employee()
# print(e.password)  # Attribute error
print(e._employee__password)


# encapsulation using protected access specifier => Access within same and child class only
class Employee:
    def __init__(self):
        self._salary = 30000  # _ for protected

e = Employee()
print(e._salary) # _ for protected


# encapsulation using public access specifier => access everywhere
class Employee:
    def __init__(self):
        self.salary = 30400  

e = Employee()
print(e.salary)


