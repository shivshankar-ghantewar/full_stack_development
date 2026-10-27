# count white spaces
char ="python is programming language"
count = 0
space = " "
i = 0
while i < len(char):
   if char[i] == " ":
        count = count + 1 

   i = i + 1
print("Total count of space=",count)

# count a 
char ="python is programming language"
count = 0
i = 0
while i < len(char):
   if char[i] == "a":
        count = count + 1 

   i = i + 1
print("total count of a=",count)

# print vowels
s="shivshankar"
for ch in s:
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        print(ch)

# string is anagram or not
count=0
str1="silent"
str2="listen"
if(len(str1)==len(str2)):
 for i in range(len(str1)):
    for j in range(len(str2)):
        if(str1[i]==str2[j]):
            count+=1
            str2=str2[:j]+"*"+str2[j+1:]
            break

 if len(str1) == count:
    print("anagram")
 else:
    print("not anagram")  
else:
    print("not anagram")         


# reverse string ex.python
name="python"
reverse=" "
for ch in name:
    reverse=ch+reverse
print(reverse)    


#  "hello how are you" revrese  string 
store=""
reverse=""
greet="hello how are you"
for i in greet:
    if(i!=" "):
        store=store+i
    else:
        reverse=store+" "+reverse
        store=""
reverse=store+" "+reverse
print(reverse)    



#  krishna  o/p: k|r|i|s|h|n|a
name="krishna"
for i in range(len(name)):
    print(name[i],end="")
    if i< len(name)-1:
        print("|",end="")


     
# input=> python o/p: positive and negative index of every character
name="python"
for i in range(len(name)):
    print("char=",name[i],end=" " )        
    print("positive index=",i,end=" ")
    print("negative index=",i-len(name))


# check palindrome or not 
s1="mom"
s2=s1[::-1] # make string reverse
if(s1==s2):
    print("pallindrome")
else:
    print("not pallindrome")    


# lowercase to uppercse
name="hello"
for i in name:
    new=chr(ord(i)-32)
    print(new,end="")

# uppercase to lowercase 
name="HELLO"
for i in name:
    print(chr(ord(i)+32),end="")
  

# occurence of character
a="programming"
my_set=set()

for i in a:
    my_set.add(i)

for k in my_set:
      count=0
      for j in a:
             if k==j:
              count+=1
      print(k,count)        








  