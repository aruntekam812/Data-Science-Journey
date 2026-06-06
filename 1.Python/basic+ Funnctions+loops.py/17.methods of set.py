#union() and update()

s1 = {1,2,3,4,5,6}
s2 = {7,8,1,9,5,10}
print(s1.union(s2))
s2.update(s1)
print(s1,s2)


#inrersection and intersection_update()

s1 = {1,2,3,4,5,6}
s2 = {7,8,1,9,5,10}

print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1,s2)

#symmetric_difference()


s1 = {1,2,3,4,5,6}
s2 = {7,8,1,9,5,10}
print(s1.symmetric_difference(s2))



#difference()

s1={1,2,5,6}
s2 ={3,6,2,7}
print(s1.difference(s2)) 


#isdisjoint()

s1 ={1,2,3,4,5,5}
s2={6,7,8,9,10}
print(s1.isdisjoint(s2))

#issuperset()

s1={1,2,3,4,5,6,7,8,9,10}
s2= {1,2,3,4,5,6}
print(s1.issuperset(s2))


#add()


s1= {"BERLIN","TOKYO","PROFESSOR","RIO"}
s1.add("HELSINKI")
print(s1)

#update()
s1= {"BERLIN","TOKYO","PROFESSOR","RIO"}
s2 ={"HELSINKI","LALA"}
s1.update(s2)
print(s1)


#remove()discard()

s1= {"BERLIN","TOKYO","PROFESSOR","RIO","HELSINKI"}
s1.remove("HELSINKI")
print(s1)

#pop()


s1= {"BERLIN","TOKYO","PROFESSOR","RIO","HELSINKI"}
print(s1.pop())
if "TOKYO" in s1:
    print("yes")
else:
    print("no")

#del() delete entire set

# s1= {"BERLIN","TOKYO","PROFESSOR","RIO","HELSINKI"}
# del s1
# print(s1)


#clear()


s1= {"BERLIN","TOKYO","PROFESSOR","RIO","HELSINKI"}
s1.clear()
print(s1)
