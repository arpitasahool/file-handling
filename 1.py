'''f=open('test.txt','r')
new=f.read()
print(new)
f.close()
print()

f=open("test.txt",'r')
data=f.read()
words=data.split()
dict={}
for i in words:
    dict[i]=words.count(i)
print(dict)
print()


#Q3. Write a Python program to copy the contents of a file to another file 
with open('test.txt','r') as f1:
    with open('test1.txt','w') as f2:
       f2.write(f1.read())

#Q4. Write a Python program to combine each line from first file with the corresponding line in second file.
l1=[]
l2=[]
s=str()
with open('test.txt','r') as f1:
    with open('test1.txt','r') as f2:
       l1+=f1.readlines()
       l2+=f2.readlines()
       for i,j in zip(l1,l2):
           print(i)
           print(j)
           s+=i+j#making one string of info
with open('test2.txt','w') as f3:
      f3.write(s)

'''
#Q5. Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
a=int(input("enter range"))
with open('test3.txt','w') as f:
   for i in range(a):
      x=int(input("Enter number: "))
      f.write("%d "%(x))

with open('test3.txt','r') as f:
   data=f.readlines()
  # print(data)
   for no in data:
      l=no.split()
   l.sort()

with open('test4.txt','w') as f:
   for i in l:         
      f.write("%s "%(i))
