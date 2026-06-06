# f =  open('handling access.py','r') # read file 
# text=f.read()
# print(text)
# f.close()

#append file 
# f =  open('handling access.py','a')
# f.write('what is your name\n')
# f.close()


#with 
# with open('handling access.py','a') as f:
#     f.write("i am Arun")

#readlines()
# f= open('handling access.py','r')

# while True:
   
#     line = f.readline()
#     print(line)
#     if not line:
#         break

#for marks.py file

# f= open('marks.py','r')
# i=0

# while True:
#     i=i+1
   
#     line = f.readline()
   
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]

#     print(f"marks of student {i} in maths is: {m1}")
#     print(f"marks of student {i} in english is: {m2}")
#     print(f"marks of student {i} in chemistry is: {m3}")

# seek()

f=open('marks.py','r')
print(type(f))
f.seek(10)
data = f.read(5)
print(data)
f.close()