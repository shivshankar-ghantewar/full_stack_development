# open file
f=open("file.txt","w")
f.write("hello my name is shiv\n")
f.write("hello my name is shiv")
f.close()

 
f=open("file.txt","r")
print("file name=",f.name)
print("readable mode=",f.readable())
print("writable mode=",f.writable())
print("file closed=",f.closed)
f.close()
print("file closed=",f.closed)

# read data
f=open("file.txt","r")
print(f.read())
f.close()

#write data
f=open("file.txt","w")
f.write("hello my name is shiv")
f.close()

#Append data
f=open("file.txt","a")
f.write("i am from nanded")
f.close()

# read line
import os
f=open("file.txt","r")
print(f.readline())
f.close()

# read all lines
import os
f=open("file.txt","r")
print(f.readlines())
f.close()


#create file using x
import os
f=open("file.txt","x")  # create if not exist or if exists gives error
f.close()

# file close
f=open("file.txt","r")
print(f.readline())
f.close()


# remove file
import os 
os.remove("file.txt")



# check if file exists, then delete it 
import os 
if os.path.exists("file.txt"): # check the location of file 
    os.remove("file.txt")
else:    
    print("file not found ")


# with statement => no need to close file manually
with open("file.txt","r") as f:
    content=f.read()
    print(content)

    




