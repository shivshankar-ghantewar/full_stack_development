def show(name):
    print("my name is",name)

person={
    "name":"shiv",
    "Age":22,
    "city":"nanded"
}    

def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

def div(a,b):
    print(a/b)


 # palindrome number
def palindrome(num):
    temp=num
    i = 0
    rev = 0
    while num > 0:
       rem=num%10
       rev=rev*10+rem
       num=num//10
    if(rev==temp):
        print("palindrome")
    else:
        print("not palindrome")    

# armstrong number
def armstrong(num):
    temp=num
    i = 0
    rev = 0
    while num > 0:
       rem=num%10
       rev=rev+rem*rem*rem
       num=num//10
    if(rev==temp):
        print("armstrong")
    else:
        print("not armstrong")
