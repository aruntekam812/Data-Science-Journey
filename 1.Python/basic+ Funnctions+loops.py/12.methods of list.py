#l.sort()

l = [9,6,4,7,8,3,1]
l.sort()
print(l)

#l.sort(reverse = True)


l = [11,46,1,2,3,4,6]
l.sort(reverse=True)
print(l)


#l.index()

l= [1,2,3,4,5]
print(l.index(5))


#l.count()

l= [1,1,2,3,4,5]
print(l.count(1))



#l.copy()


l= [1,1,2,3,4,5]
print(l)
m=l.copy()
m[1]=0
print(m)


#l.append()

l = [1,2,3,4]
l.append(10)
print(l)


#l.insert()


l=[1,2,3,4,5]
l.insert(1,10)
print(l)


#l.remove()
l=[100,200,800,300,400,500]
l.remove(800)
print(l)


#l.extend()

l=[1,2,3,4,5]
print(l)
m=[6,7,8,9,10]
l.extend(m)
print(l)
n=[11,12,13]
l.extend(n)
print(l)

k=["arun","tekam"]
l.extend(k)
print(l)

a=[1,2]
s=[1000,5000,100000]
z=a+s
print(z)